FROM python:3.11.5

# Time Zone
# タイムゾーン、ロケール設定
ENV TZ="Asia/Tokyo" \
    LANG="C.UTF-8" \
    LANGUAGE="ja_JP:ja" \
    LC_ALL="C.UTF-8"

# Docker Image内で実行される作業ディレクトリ(Path)を指定する: ない場合は作ってくれます。
# change dir
WORKDIR /home/simple-game/app

# Flask環境変数: Dockerコンテナ内で、Flaskがアプリケーションを正しく検出し、起動できるようになります。
ENV FLASK_APP=app

# Hostマシンのディレクトリ・ファイル を Container側のPathに COPY(追加)する
COPY ./simplegame /home/simple-game/app

# RUNコマンド: Docker Image内で、コマンドを実行する
# パッケージをキャッシュせずにインストール & -rオプションで、依存パッケージを一括インストール
# --upgrade pipを最新バージョンに更新する
RUN pip install --no-cache-dir --upgrade -r requirements.txt