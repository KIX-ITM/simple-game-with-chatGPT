FROM python:3.11.5

# Time Zone
# タイムゾーン、ロケール設定
ENV TZ="Asia/Tokyo" \
    LANG="C.UTF-8" \
    LANGUAGE="ja_JP:ja" \
    LC_ALL="C.UTF-8"

WORKDIR /home/simple-game-api/app

COPY ./simplegame_api /home/simple-game-api/app

RUN pip install --no-cache-dir --upgrade -r requirements.txt

CMD ["uvicorn", "main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "80"]