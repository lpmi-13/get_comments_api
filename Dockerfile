from python:3.8-alpine

COPY requirements.txt /
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app
WORKDIR /app

EXPOSE 8000

RUN addgroup -S appgroup && adduser -S appuser -G appgroup
USER appuser

CMD gunicorn -w 4 --bind 0.0.0.0:$PORT app:app
