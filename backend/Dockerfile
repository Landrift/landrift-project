# ベースイメージ
FROM python:3.9

# 作業ディレクトリの設定
WORKDIR /app

# 依存関係のインストール
COPY requirements.txt .
RUN pip install -r requirements.txt

# ソースコードをコピー
COPY . .

# Djangoサーバーの起動
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]