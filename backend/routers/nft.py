from fastapi import APIRouter,UploadFile
import os
from fastapi import APIRouter, HTTPException
from schemas.nft_schema import NFTMetadata
from services.nft_service import upload_to_pinata

router = APIRouter()

@router.post(
    "/nft",
    tags=["NFT"],
    summary="画像のアップロードとNFTの発行",
    response_model=NFTMetadata,
)
async def mint_nft(upload_file: UploadFile
):
    image_url = await upload_to_pinata(upload_file)
    nft_metadata = NFTMetadata
    nft_metadata.name = upload_file.filename
    nft_metadata.description = "NFT with GOD により、生成されたおみくじです。"
    nft_metadata.image = image_url
    return nft_metadata


@router.post(
    "/nft/get",
    tags=["NFT"],
    summary="NFT画像の確認",
    response_model=NFTMetadata,
)
async def get_nft(upload_file: UploadFile, 
                   file_name: str,
):
    pass