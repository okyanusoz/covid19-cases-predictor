# NOTE: This is mostly for GitHub Actions, and produces a big image.
FROM tensorflow/tensorflow:latest-devel

WORKDIR /app

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . .
