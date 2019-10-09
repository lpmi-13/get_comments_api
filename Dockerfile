from python:3.6-alpine

COPY requirements.txt /
RUN pip install -r requirements.txt

COPY . /app
WORKDIR /app

EXPOSE 8000

CMD gunicorn -w 4 --bind 0.0.0.0:8000 app:app
