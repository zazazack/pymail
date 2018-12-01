FROM python:latest

LABEL maintainer="Zachary Wilson <wilsonze@gmail.com>"

ENV PYTHONUNBUFFERED 1
RUN apt-get update && apt-get install -y \
  git \
  telnet \
  && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir pipenv

WORKDIR /usr/src

COPY . .

RUN pipenv install --dev --system

CMD ["python", "-m", "pymail"]
