FROM bwits/pdf2htmlex-alpine

COPY ./repositories /etc/apk/repositories

RUN apk update

RUN apk --update --no-cache add \
    build-base \
    openssl \
    gcc \
    g++ \
    musl \
    linux-headers \
    make \
    gfortran \
    python3 \
    python3-dev \
    python2 \
    python2-dev

WORKDIR /workspace

WORKDIR /api

COPY ./api /api

RUN pip3 install --upgrade pip \
    && pip3 install -r requirements.txt