FROM ubuntu
SHELL ["/bin/bash", "-c"]

RUN apt update && apt upgrade -y
RUN apt install -y tor vim netcat-traditional net-tools 
RUN apt install -y software-properties-common
RUN apt install -y python3 python3-venv python3-dev
RUN apt remove -y python3-cryptography
RUN apt install -y stubby proxychains4
RUN apt install -y ldnsutils # for srill
#RUN apt install -y dnsutils tcpdump 
RUN apt install -y python3-stem
RUN apt install -y python3-pip
RUN pip install carml --break-system-packages

RUN rm -rf /var/lib/apt/lists/*


ENV ENTRY_NODES=
ENV EXIT_NODES=
ENV EXCLUDE_NODES=
ENV HOPS=3

WORKDIR /etc/stubby/
COPY stubby.yml /etc/stubby/stubby.yml
COPY proxychains4.conf /etc/proxychains4.conf
COPY torrc_template /etc/tor/torrc
COPY relays.py .
COPY bootup.sh .

HEALTHCHECK --interval=120s --timeout=30s --start-period=10s CMD drill @127.0.0.1 -p 8053 getdnsapi.net || exit 1

CMD ["./bootup.sh"]
