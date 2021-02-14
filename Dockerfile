FROM tensorflow/tensorflow:latest-devel

WORKDIR /app

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . .
