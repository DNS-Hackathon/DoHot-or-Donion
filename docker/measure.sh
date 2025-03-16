#!/bin/bash

#queryfile=$2

resolver=172.17.0.1
port=1337

if [ $1 = 'do53' ]; then
    echo "$(date +"%Y-%m-%dT%H:%M:%S"): Starting Do53"
    docker run --rm -d -p 1337:53/tcp -p 1337:53/udp --name do53-container do53-image > /dev/null
elif [ $1 = 'doh' ]; then
    echo "$(date +"%Y-%m-%dT%H:%M:%S"): Starting DoH"
    docker run --rm -d -p 1337:53/tcp -p 1337:53/udp --name doh-container doh-image > /dev/null
elif [ $1 = 'dot' ]; then
    echo "$(date +"%Y-%m-%dT%H:%M:%S"): Starting DoT"
    docker run --rm -d -p 1337:8053/tcp -p 1337:8053/udp --name dot-container dot-image > /dev/null

elif [ $1 = 'dohot-default' ]; then
    echo "$(date +"%Y-%m-%dT%H:%M:%S"): Starting DoHoT Default"
    docker run --rm -d -p 1337:53/tcp -p 1337:53/udp --name dohot-container dohot-image > /dev/null
elif [ $1 = 'dohot-best' ]; then
    echo "$(date +"%Y-%m-%dT%H:%M:%S"): Starting DoHoT Best"
    docker run --rm -d -p 1337:53/tcp -p 1337:53/udp --name dohot-container \
        -e ENTRY_NODES="se" \
        -e EXIT_NODES="se" \
        -e HOPS="2" \
        dohot-image > /dev/null

elif [ $1 = 'dotot-default' ]; then
    echo "$(date +"%Y-%m-%dT%H:%M:%S"): Starting DoToT Default"
    docker run --rm -d -p 1337:8053/tcp -p 1337:8053/udp --name dotot-container dotot-image > /dev/null
elif [ $1 = 'dotot-best' ]; then
    echo "$(date +"%Y-%m-%dT%H:%M:%S"): Starting DoToT Best"
    docker run --rm -d -p 1337:8053/tcp -p 1337:8053/udp --name dotot-container \
        -e ENTRY_NODES="se" \
        -e EXIT_NODES="se" \
        -e HOPS="2" \
        dotot-image > /dev/null
fi

#queryfile=$2
#echo "$(date +"%Y-%m-%dT%H:%M:%S"): Running dnsperf: $queryfile"
#docker run --rm -v $(pwd)/$queryfile:/tmp/domains.txt \
#	dnsperf -d /tmp/domains.txt -s $resolver -p $port -Q 100 -t 10

dname="DNSHACKATHON-$(mktemp -u XXXXXXXX).se"
echo "$(date +"%Y-%m-%dT%H:%M:%S"): Sending random NXDOMAIN query ($dname)"
dig @$resolver -p $port $dname +tries=20 | grep "Query time"

if [ $1 = 'doh' ]; then
    echo "$(date +"%Y-%m-%dT%H:%M:%S"): Stopping DoH"
    docker stop doh-container > /dev/null &
elif [ $1 = 'dot' ]; then
    echo "$(date +"%Y-%m-%dT%H:%M:%S"): Stopping DoT"
    docker stop dot-container > /dev/null &
elif [[ $1 == "dohot"* ]]; then
    echo "$(date +"%Y-%m-%dT%H:%M:%S"): Stopping DoHoT"
    docker stop dohot-container > /dev/null &
elif [[ $1 = "dotot"* ]]; then
    echo "$(date +"%Y-%m-%dT%H:%M:%S"): Stopping DoToT"
    docker stop dotot-container > /dev/null &
fi
