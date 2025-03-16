FROM ubuntu
SHELL ["/bin/bash", "-c"]

RUN apt update && apt upgrade -y && apt install -y \
     vim netcat-traditional net-tools \
    software-properties-common \
    stubby  \
    ldnsutils # for drill


ENV ENTRY_NODES=
ENV EXIT_NODES=
ENV EXCLUDE_NODES=
ENV HOPS=3

WORKDIR /etc/stubby/
COPY stubby.yml /etc/stubby/stubby.yml

#HEALTHCHECK --interval=120s --timeout=30s --start-period=10s CMD drill @127.0.0.1 -p 8053 getdnsapi.net || exit 1

CMD ["/usr/bin/stubby", "-v", "7", "-C", "/etc/stubby/stubby.yml"]
