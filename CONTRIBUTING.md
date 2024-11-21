# 貢献者ガイド
futarin-api を開発するにあたっての注意事項を記述していく。

## 目次
futarin-api の開発方針について
- [ブランチ戦略](#ブランチ戦略)
- [プルリクエスト](#プルリクエスト)
- [静的解析](#静的解析)
- [テスト](#テスト)
- [GitHub Actions](#github-actions)
- [Issue](#issue)
- [ライセンス](#ライセンス)

## ブランチ戦略
本リポジトリでは、GitHub Flow を採用しています。
プルリクエストは基本的に`main`ブランチへマージされます。
**`main`ブランチは常にリリース可能な状態が保証されます。**
参考：https://docs.github.com/ja/get-started/using-github/github-flow

### ブランチ命名規則
開発時は必ずmainからブランチをきってください。mainに直接pushすることがないように！
ブランチ名の例："feat/#1_hoge"
- feat: ブランチの特徴
  - 新機能：feat
  - 修正：fix
- /#1_hoge
  - issue番号
  - memo
```
git checkout main
git pull
git checkout -b feat/#1_hoge
```

## プルリクエスト
全てのコード変更は[プルリクエスト](https://github.com/futaringoto/futarin-api/pulls)を介して行います。
### プルリクエストを送る
以下の手順で作成します。
- [環境構築](#環境構築)
- リポジトリをクローンする
- ブランチを切る [ブランチ戦略](#ブランチ戦略)参照
- コードを編集する
- [静的解析を実行する](#静的解析)
- [コードのテストを行う](#コードをテストする)
- リモートへプッシュして、`main`ブランチへのプルリクエストを作成する

## 環境構築
開発環境はすべて`docker compose`で完結するよう実装されています。
```
git clone git@github.com:shun-harutaro/nft-nenga.git
cd futarin-api
```
環境変数を設定してください。詳しくは[README](https://github.com/futaringoto/futarin-api/blob/main/README.md)へ
```
docker compose build
```
> [!IMPORTANT]
> Dockerfileを更新した際は、キャッシュが使われないよう、`docker compose build --no-cache`でビルドしましょう

## コード実行
```
docker compose up
```
> [!TIP]
> ホットリロードを採用しています。pythonファイルの変更が保存されると再度自動でビルドが走ります


## コードの編集
### パッケージ
パッケージ管理に`npm`,`uv`を採用しています。
#### パッケージの追加(フロントエンド)
```
docker compose exec frontend npm i `パッケージ名`
docker compose exec frontend npm i -D `パッケージ名` # 開発依存の追加
```
#### パッケージの追加(バックエンド)
```
docker compose exec backend uv add `パッケージ名`
docker compose exec backend uv add --dev `パッケージ名` # 開発依存の追加
```
#### パッケージの更新(フロントエンド)
```
docker compose exec frontend npm update
```
#### パッケージの更新(バックエンド)
```
docker compose exec backend uv sync --update
```

## 静的解析
自動リントと自動整形を採用しています。
### リント

### 整形

## テスト

## GitHub Actions
まだない
### Workflows

### Variable
| name               | description         |
| :----------------- | :------------------ |

### Secrets
| name | description |
| :--- | :---------- |

## Issue
不具合の報告、機能要望は、[Issue](https://github.com/futaringoto/futarin-api/issues)に報告してください。

## ライセンス
本リポジトリはMITライセンスです。
