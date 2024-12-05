from web3 import Web3
import os
from dotenv import load_dotenv
import json

# 環境変数をロード
load_dotenv()

NFT_NETWORK_URL = "https://polygon-rpc.com/"
NFT_ACCOUNT_ADDRESS = os.getenv("NFT_ACCOUNT_ADDRESS")
NFT_PRIVATE_KEY = os.getenv("NFT_PRIVATE_KEY")

web3 = Web3(Web3.HTTPProvider(NFT_NETWORK_URL))
web3.eth.default_account = web3.to_checksum_address(NFT_ACCOUNT_ADDRESS)

web3 = Web3(Web3.HTTPProvider(NFT_NETWORK_URL))
web3.eth.default_account = web3.to_checksum_address(NFT_ACCOUNT_ADDRESS)

# ABI と バイトコードをロード
with open("HackuNFT_abi.json", "r") as abi_file:
    abi = json.load(abi_file)

with open("HackuNFT_bytecode.json", "r") as bytecode_file:
    bytecode = json.load(bytecode_file)["bytecode"]

# コントラクトインスタンスを作成
contract = web3.eth.contract(abi=abi, bytecode=bytecode)

def deploy_contract():
    try:
        # アドレスをチェックサム形式に変換
        owner_address = web3.to_checksum_address(NFT_ACCOUNT_ADDRESS)

        # ガス価格を動的に取得
        gas_price = web3.eth.gas_price
        print(f"Current Gas Price: {gas_price}")

        # デプロイトランザクションを構築
        transaction = contract.constructor(owner_address).build_transaction({
            "from": owner_address,
            "chainId": 137,  # Polygon MainnetのチェーンID
            "gas": 3000000,
            "gasPrice": gas_price,
            "nonce": web3.eth.get_transaction_count(owner_address),
        })

        # トランザクションを署名
        signed_tx = web3.eth.account.sign_transaction(transaction, private_key=NFT_PRIVATE_KEY)

        # トランザクションを送信
        tx_hash = web3.eth.send_raw_transaction(signed_tx.raw_transaction)
        print(f"Transaction hash: {tx_hash.hex()}")

        # トランザクションの承認を待機 (タイムアウトを延長)
        tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash, timeout=300)
        print("Contract deployed successfully!")

        # デプロイされたコントラクトのアドレスを取得
        contract_address = tx_receipt.contractAddress
        print(f"Contract Address: {contract_address}")

        return contract_address
    except Exception as e:
        print(f"Error during deployment: {str(e)}")
        return None

# デプロイを実行
deploy_contract()