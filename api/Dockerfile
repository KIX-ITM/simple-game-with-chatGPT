FROM python:3.11.5

# Time Zone
# タイムゾーン、ロケール設定
ENV TZ="Asia/Tokyo" \
    LANG="C.UTF-8" \
    LANGUAGE="ja_JP:ja" \
    LC_ALL="C.UTF-8"

WORKDIR /home/app

COPY ./ /home/app

RUN pip install --no-cache-dir --upgrade -r /home/app/requirements.txt

CMD ["uvicorn", "app.main:application", "--proxy-headers", "--host", "0.0.0.0", "--port", "8000"]