FROM python:3.12

WORKDIR /app

RUN curl -s https://packagecloud.io/install/repositories/ookla/speedtest-cli/script.deb.sh | bash \
    && apt-get install speedtest \
    && speedtest --accept-license

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY ./speedtest /app/speedtest

CMD ["uvicorn", "speedtest:app", "--host", "0.0.0.0", "--port", "8000"]
