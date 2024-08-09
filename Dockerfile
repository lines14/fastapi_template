FROM python:3.12-alpine

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apk update && apk add alpine-sdk gcc musl-dev python3-dev libffi-dev openssl-dev

RUN addgroup -g 1000 mygroup && adduser -u 1000 -G mygroup -S myuser

RUN chown -R myuser:mygroup /app

ENV PATH=$PATH:/home/myuser/.local/bin

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

RUN pip install "fastapi[standard]"

COPY . .

RUN chmod -R 777 /app

USER myuser

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
