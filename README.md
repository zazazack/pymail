---
  title: README
  author: Zachary Wilson
  date: 2018-11-20T11:56:00-0600
---

# pymail

Send mail with Python for fun and profit.

## Features

## Prerequisites

- [Docker CE](https://docs.docker.com/install/)

## Installation

### Stable

    $ docker pull zwilson/pymail:latest
    $ docker run zwilson/pymail:latest

### Development

    $ git clone https://github.com/zazazack/pymail.git
    $ cd pymail/
    $ docker-compose up -d

## Usage

### Send a message

#### From `stdin`

```sh
$ pymail send \
  --to_addrs foo@example.com \
  -h subject="Hello, Foo!" # header \
  "Hello, world!" # message
```

#### From a file

```sh
$ pymail send \
  --to "bar@example.com" \
  --cc "baz@example.com" \
  < message.txt
```

### View messages

```
# TODO: view messages
```

## References

- [`email`](https://docs.python.org/3/library/email.html)
- [`smtplib`](https://docs.python.org/3/library/smtplib.html)
- [`imaplib`](https://docs.python.org/3/library/imaplib.html)
- [`poplib`](https://docs.python.org/3/library/poplib.html)
- [Packaging](https://packaging.python.org/guides)
