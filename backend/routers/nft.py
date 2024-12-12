from fastapi import APIRouter,UploadFile,Body
import os
from fastapi import APIRouter, HTTPException
from schemas.nft_schema import NFTMetadata
from services.nft_service import (
    upload_image_to_pinata,
    get_balance,
    upload_metadata_to_pinata,
    mint_nft,
    get_metadata_from_transaction,
    create_metadata,
    generate_name_with_user
)
from services.line import get_user_id_from_cookie
from utils.config import (
    get_nft_private_key
)

NFT_PRIVATE_KEY = get_nft_private_key()

router = APIRouter()

@router.post(
    "/nft",
    tags=["NFT"],
    summary="画像のアップロードとNFTの発行",
)
async def mint(upload_file: UploadFile):
    image_url = await upload_image_to_pinata(upload_file)
    nft_name = generate_name_with_user(get_user_id_from_cookie())
    nft_metadata = create_metadata(nft_name=nft_name,user_id=get_user_id_from_cookie(),image_url=image_url)
    metadata_url = upload_metadata_to_pinata(nft_metadata)
    tx_receipt = mint_nft(metadata_url,NFT_PRIVATE_KEY)
    tx_hash = tx_receipt.transactionHash.hex()
    try:
        token_id_hex = tx_receipt.logs[0]["topics"][3]  # トークンIDのHexBytes
        token_id = int(token_id_hex.hex(), 16)  # 16進数を整数に変換
    except (KeyError, IndexError) as e:
        raise HTTPException(status_code=500, detail=f"Failed to retrieve token ID: {str(e)}")
    response_data = {
        "name": nft_metadata.name,
        "description": nft_metadata.description,
        "image": nft_metadata.image,
        "attributes": nft_metadata.attributes,
        "transactionHash": tx_hash,
        "tokenId": token_id
    }
    return response_data

@router.get(
    "/nft/metadata/{tx_hash}",
    tags=["NFT"],
    summary="トランザクションハッシュからメタデータと画像を取得",
)
async def get_nft_metadata(tx_hash: str):
    try:
        result = get_metadata_from_transaction(tx_hash)
        return result
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error occurred: {str(e)}")


@router.get(
    "/nft/balance",
    tags=["NFT"],
    summary="NFTアカウントの残高確認",
)
async def balance():
    try:
        balance = get_balance()  
        return balance  
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error occurred: {str(e)}")