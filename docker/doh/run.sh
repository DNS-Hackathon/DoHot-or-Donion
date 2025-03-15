#!/bin/bash

docker stop doh-container
docker rm doh-container
docker build -t doh-image .
docker run --rm --name doh-container \
    -p 127.0.0.1:1337:53/udp \
    -p 127.0.0.1:1337:53/tcp \
    doh-image
