# nft-nenga

## 目次
- [Overview](#overview)
- [貢献者ガイド(CONTRIBUTING.md)](#貢献者ガイドcontributingmd)
- [動作環境（確認済み）](#動作環境確認済み)
- [動作確認](#動作確認)
- [APIエンドポイント](#apiエンドポイント)
- [ディレクトリ構成](#ディレクトリ構成)
- [ライセンス](#ライセンス)
- [Authors](#authors)

## Overview
LINE ヤフー社主催、Hack U KOSEN 2024 最優秀賞 ＆ HappyHacking賞 ダブル受賞！！
- [<img src="frontend/public/web-app-manifest-512x512.png">](https://www.canva.com/design/DAGY-nI_Kto/LWnHLOX9T7vyRYSK_wr8gw/view) (created by [KAWAHARA Ryosuke](https://github.com/iamkawaryo))
- [プレゼン動画(準備中)]() (presented by [OKADA Itsuki](https://github.com/okd10))

## 貢献者ガイド(CONTRIBUTING.md)
本リポジトリにコミットする場合、[CONTRIBUTING.md](https://github.com/shun-harutaro/nft-nenga/blob/main/CONTRIBUTING.md)を**必ず確認ください**

## 動作環境（確認済み）
- Ubuntu(WSL2)
  - Docker Desktop (windows)
- macOS(x86-64, arm64)
  - OrbStack
  - ~~Docker Desktop~~ 動作未確認

## 動作確認
1. リポジトリのクローンと移動
```
git clone git@github.com:shun-harutaro/nft-nenga.git
cd nft-nenga
```

2. `.env`の作成
```
touch .env
echo "OPENAI_API_KEY=[openAI api key]" >> .env
echo "GOOGLE_MAPS_API_KEY=[google maps api key]" >> .env
echo "LINE_CLIENT_ID=[line client id]" >> .env
echo "LINE_CLIENT_SECRET=[line client secret]" >> .env
echo "PINATA_API_KEY=[pinata api key]" >> .env
echo "PINATA_SECRET_API_KEY=[pinata api secret]" >> .env
echo "NFT_ACCOUNT_ADDRESS=[nft account address]" >> .env
echo "NFT_PRIVATE_KEY=[nft private key]" >> .env
```

3. 自己署名証明書の発行
```
openssl req -new -newkey rsa:2048 -days 365 -nodes -x509 -keyout localhost-key.pem -out localhost-cert.pem
```

4. Dockerイメージのビルド
```
docker compose build
```

5. コンテナ起動
```
docker compose up
```
Detachモード
```
docker compose up -d
```

6. テーブル作成
```
docker compose exec backend uv run migrate_db.py
```

7. localhost で開いてみましょう <br>
frontend: https://localhost/ <br>
backend: https://localhost/api/

8. コンテナの停止
```
docker compose down
```

## APIエンドポイント
未定義

## ディレクトリ構成
- frontend (Vue.js)
- backend (FastAPI)
- nginx (web-server)
```
.
├── CONTRIBUTING.md
├── LICENSE
├── README.md
├── backend
│   ├── Dockerfile
│   ├── cruds
│   │   └── __init__.py
│   ├── main.py
│   ├── models
│   │   └── __init__.py
│   ├── pyproject.toml
│   ├── routers
│   │   ├── __init__.py
│   │   ├── auth.py
│   │   ├── gpt.py
│   │   ├── location.py
│   │   └── nft.py
│   ├── schemas
│   │   ├── __init__.py
│   │   ├── nft_schema.py
│   │   └── text.py
│   ├── services
│   │   ├── HackuNFT_abi.json
│   │   ├── HackuNFT_bytecode.json
│   │   ├── __init__.py
│   │   ├── compile.py
│   │   ├── gpt.py
│   │   ├── line.py
│   │   ├── nft_contract.py
│   │   ├── nft_service.py
│   │   └── ogp_service.py
│   ├── tests
│   │   └── __init__.py
│   ├── uploads
│   ├── utils
│   │   ├── __init__.py
│   │   └── config.py
│   └── uv.lock
├── compose.yml
├── frontend
│   ├── Dockerfile
│   ├── eslint.config.js
│   ├── index.html
│   ├── jsconfig.json
│   ├── package-lock.json
│   ├── package.json
│   ├── public
│   │   └── favicon.ico
│   ├── src
│   │   ├── App.vue
│   │   ├── assets
│   │   │   ├── base.css
│   │   │   ├── btn_login_base.png
│   │   │   └── main.css
│   │   ├── components
│   │   │   └── LoginButton.vue
│   │   ├── main.js
│   │   ├── plugin
│   │   │   └── axios.js
│   │   ├── router.js
│   │   └── views
│   │       ├── Location.vue
│   │       └── Login.vue
│   └── vite.config.js
└── nginx.conf
```

## ライセンス
本リポジトリはMITライセンスです。

## Authors  
We are やそしまぐみ！！
- [OKADA Itsuki](https://github.com/okd10)
- [KAWAHARA Ryosuke](https://github.com/iamkawaryo)
- [KITAMURA Kotarro](https://github.com/okota7412)
- [SAKAI Yusei](https://github.com/usay1001010)
- [TAKAGI Toru](https://github.com/imtkgtr)
- [NOZAKI Shuntaro](https://github.com/shun-harutaro)
