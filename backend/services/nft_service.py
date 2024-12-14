from fastapi import FastAPI, File, UploadFile, HTTPException
import requests
import json
import os
from datetime import datetime
from web3 import Web3
from schemas.nft_schema import NFTMetadata
from utils.config import (
    get_nft_acount_address,
    get_pinata_api_key,
    get_pinata_secret_api_key,
    get_nft_private_key
)
from models.nft import Nft
from cruds.nft import (
    create_nft,
    get_nft,
    update_nft,
    delete_nft,
)

PINATA_API_KEY = get_pinata_api_key()
PINATA_SECRET_API_KEY = get_pinata_secret_api_key()
NFT_ACCOUNT_ADDRESS = get_nft_acount_address()
NFT_PRIVATE_KEY = get_nft_private_key()

NFT_NETWORK_URL = "https://polygon-rpc.com/"

web3 = Web3(Web3.HTTPProvider(NFT_NETWORK_URL))
web3.eth.default_account = get_nft_acount_address()

# ABIとバイトコードの読み込み
with open("/app/services/HackuNFT_abi.json", "r") as abi_file:
    abi = json.load(abi_file)  # JSONとして読み込む


contract_address = "0xfB40b73E6cEe109Ae7614e621ffA841Dd1EB1584"  # デプロイ済みのコントラクトアドレス
contract = web3.eth.contract(address=contract_address, abi=abi)


async def upload_image_to_pinata(upload_file: UploadFile):
    try:
        file_content = await upload_file.read()
        headers = {
            "pinata_api_key": PINATA_API_KEY,
            "pinata_secret_api_key": PINATA_SECRET_API_KEY,
        }

        files = {"file": (upload_file.filename, file_content)}
        response = requests.post(
            "https://api.pinata.cloud/pinning/pinFileToIPFS", headers=headers, files=files)

        if response.status_code == 200:
            response_data = response.json()
            ipfs_hash = response_data["IpfsHash"]
            return f"https://gateway.pinata.cloud/ipfs/{ipfs_hash}"
        else:
            raise HTTPException(
                status_code=500, detail=f"Failed to upload file: {response.text}"
            )
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error occurred: {str(e)}")


def upload_metadata_to_pinata(metadata):
    try:
        headers = {
            "pinata_api_key": PINATA_API_KEY,
            "pinata_secret_api_key": PINATA_SECRET_API_KEY,
            "Content-Type": "application/json",
        }

        metadata_dict = json.loads(metadata.json(by_alias=True))
        response = requests.post(
            "https://api.pinata.cloud/pinning/pinJSONToIPFS", headers=headers, json=metadata_dict)

        if response.status_code == 200:
            response_data = response.json()
            ipfs_hash = response_data["IpfsHash"]
            return f"https://gateway.pinata.cloud/ipfs/{ipfs_hash}"
        else:
            raise HTTPException(
                status_code=500, detail=f"Failed to upload metadata: {response.text}")
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error occurred: {str(e)}")


def mint_nft(metadata_url, private_key):
    try:
        gas_price = web3.eth.gas_price
        nonce = web3.eth.get_transaction_count(NFT_ACCOUNT_ADDRESS, "pending")

        transaction = contract.functions.createNFT(metadata_url).build_transaction({
            "from": NFT_ACCOUNT_ADDRESS,
            "chainId": 137,
            "gas": 5000000,
            "gasPrice": gas_price,
            "nonce": nonce,
        })
        signed_txn = web3.eth.account.sign_transaction(
            transaction, private_key=private_key)
        tx_hash = web3.eth.send_raw_transaction(signed_txn.raw_transaction)
        tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)

        return tx_receipt
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error occurred during NFT minting: {str(e)}")


def get_metadata_from_transaction(tx_hash: str):
    try:
        tx_receipt = web3.eth.get_transaction_receipt(tx_hash)

        token_id_hex = tx_receipt.logs[0]["topics"][3]
        token_id = int(token_id_hex.hex(), 16)

        token_uri = contract.functions.tokenURI(token_id).call()

        response = requests.get(token_uri)
        if response.status_code == 200:
            metadata = response.json()
            return {
                "tokenId": token_id,
                "transactionHash": tx_hash,
                "metadata": metadata,
            }
        else:
            raise HTTPException(
                status_code=500, detail=f"Failed to retrieve metadata: {response.text}"
            )
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error occurred: {str(e)}")


def get_balance():
    web3 = Web3(Web3.HTTPProvider(NFT_NETWORK_URL))
    balance = web3.eth.get_balance(NFT_ACCOUNT_ADDRESS)
    return {"balance": {balance},
            "currency": "POL"}


def create_metadata(filename: str, image_url: str):
    meta_data = nft_metadata = NFTMetadata(
                    name=filename,
                    description="2024年 NFT with 神により、生成されたおみくじです。",
                    image=image_url,
                    attributes=[
                        {"trait_type": "Year", "value": "2024"},
                        {"trait_type": "Grade", "value": "Super"},
                    ],
                )
    return meta_data

def generate_name_with_user(user_id: str) -> str:
    current_time = datetime.now().strftime("%Y%m%d%H%M%S")
    return f"NFT_{user_id}_{current_time}"
