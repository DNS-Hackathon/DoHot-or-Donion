#!/bin/bash

queryfile=$2

if [ $1 = 'do53' ]; then
    resolver=1.1.1.1
    port=53
elif [[ $1 == "dohot"* || $1 == "doh" ]]; then
    resolver=172.17.0.1
    port=1337
fi

if [ $1 = 'dohot-worst' ]; then
    echo "$(date +"%Y-%m-%dT%H:%M:%S"): Starting DoHoT Worst (20sec)"
    docker run --rm -d -p 1337:53/tcp -p 1337:53/udp --name dohot-container dohot-image > /dev/null
    sleep 20
elif [ $1 = 'dohot-best' ]; then
    echo "$(date +"%Y-%m-%dT%H:%M:%S"): Starting DoHoT Best (20sec)"
    docker run --rm -d -p 1337:53/tcp -p 1337:53/udp --name dohot-container \
        -e ENTRY_NODES="se" \
        -e EXIT_NODES="se" \
        -e HOPS="2" \
        dohot-image > /dev/null
    sleep 20
elif [ $1 = 'doh' ]; then
    echo "$(date +"%Y-%m-%dT%H:%M:%S"): Starting DoH (20sec)"
    docker run --rm -d -p 1337:53/tcp -p 1337:53/udp --name doh-container doh-image > /dev/null
    sleep 20
fi

echo "$(date +"%Y-%m-%dT%H:%M:%S"): Test query"
dig @localhost -p 1337 jonathanmagnusson.com | grep HEADER

echo "$(date +"%Y-%m-%dT%H:%M:%S"): Running dnsperf: $queryfile"
docker run --rm -v $(pwd)/$queryfile:/tmp/domains.txt \
	dnsperf -d /tmp/domains.txt -s $resolver -p $port -Q 100 -t 10

if [[ $1 == "dohot"* ]]; then
    echo "$(date +"%Y-%m-%dT%H:%M:%S"): Stopping DoHoT"
    docker stop dohot-container
elif [ $1 = 'doh' ]; then
    echo "$(date +"%Y-%m-%dT%H:%M:%S"): Stopping DoH"
    docker stop doh-container
fi
