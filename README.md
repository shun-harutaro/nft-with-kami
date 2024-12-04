# nft-nenga

## 目次
- [貢献者ガイド(CONTRIBUTING.md)](#貢献者ガイドcontributingmd)
- [動作環境（確認済み）](#動作環境確認済み)
- [動作確認](#動作確認)
- [APIエンドポイント](#apiエンドポイント)
- [ディレクトリ構成](#ディレクトリ構成)
- [ライセンス](#ライセンス)

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
echo "OPENAI_ASSISTANT_ID=[openAI assistant id]" >> .env
echo "OPENAI_THREAD_ID=[openAI thread id]" >> .env
echo "GOOGLE_MAPS_API_KEY=[google maps api key]" >> .env
echo "LINE_CLIENT_ID=[line client id]" >> .env
echo "LINE_CLIENT_SECRET=[line client secret]" >> .env
```

3. Dockerイメージのビルド
```
docker compose build
```

4. コンテナ起動
```
docker compose up
```
Detachモード
```
docker compose up -d
```

5. localhost で開いてみましょう <br>
frontend: http://localhost:3000 <br>
backend: http://localhost:8000

6. コンテナの停止
```
docker compose down
```

## APIエンドポイント
未定義

## ディレクトリ構成
- api (application - FastAPI)
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
│   │   └── gpt.py
│   ├── schemas
│   │   ├── __init__.py
│   │   └── text.py
│   ├── services
│   │   ├── __init__.py
│   │   └── gpt.py
│   ├── tests
│   │   └── __init__.py
│   ├── uploads
│   ├── utils
│   │   ├── __init__.py
│   │   └── config.py
│   └── uv.lock
├── compose.yml
└── frontend
    ├── Dockerfile
    ├── README.md
    ├── eslint.config.js
    ├── index.html
    ├── jsconfig.json
    ├── package-lock.json
    ├── package.json
    ├── public
    │   └── favicon.ico
    ├── src
    │   ├── App.vue
    │   ├── assets
    │   │   ├── base.css
    │   │   └── main.css
    │   ├── components
    │   │   ├── LoginButton.vue
    │   │   └── Test.vue
    │   ├── composables
    │   │   └── useAuth.js
    │   ├── main.js
    │   ├── router.js
    │   ├── utils
    │   │   └── oauth2.js
    │   └── views
    │       ├── Callback.vue
    │       └── Login.vue
    └── vite.config.js
```

## ライセンス
本リポジトリはMITライセンスです。
