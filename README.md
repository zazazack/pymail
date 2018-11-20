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
  --from "sender@example.com" \
  --to "recipient@example.com" \
  --subject "Hello, world!" \
  -
```

#### From a file

```sh
$ pymail send \
  --from "foo@example.com" \
  --to "bar@example.com" \
  --cc "baz@example.com" \
  --subject "Hello, world!" \
  --message "./message.txt"
```

### Read messages

#### Recent messages

```sh
$ pymail head  # print the five most recent messages
$ pymail head -n 10 # print 10
```

#### Regex search

```sh
$ pymail search \
  --from "foo@example.com" \
  --to "bar@example.com" \
  --regex "Hello.*"
```

### Configuration

#### View
```sh
$ pymail config
```

### Modify
```sh
$ pymail config set
```

## References

- [`email`](https://docs.python.org/3/library/email.html)
- [`smtplib`](https://docs.python.org/3/library/smtplib.html)
- [`imaplib`](https://docs.python.org/3/library/imaplib.html)
- [`poplib`](https://docs.python.org/3/library/poplib.html)
- [Packaging](https://packaging.python.org/guides)
