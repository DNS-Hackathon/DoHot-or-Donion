#!/bin/bash

docker stop do53-container
docker rm do53-container
docker build -t do53-image .
docker run --rm --name do53-container \
    -p 127.0.0.1:1337:53/udp \
    -p 127.0.0.1:1337:53/tcp \
    do53-image
