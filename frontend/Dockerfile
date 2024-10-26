# ベースイメージ
FROM node:18

# 作業ディレクトリの設定
WORKDIR /app

# 必要なファイルをコピー
COPY package.json yarn.lock ./
RUN yarn install

# ソースコードをコピー
COPY . .

# 開発サーバーの起動
CMD ["yarn", "vite", "--host", "--port", "3001"]