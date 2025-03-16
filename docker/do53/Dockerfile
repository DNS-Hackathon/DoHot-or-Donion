FROM ubuntu
SHELL ["/bin/bash", "-c"]

RUN apt update && apt upgrade -y && apt install -y \
    vim netcat-traditional net-tools unbound dnsutils
RUN rm -rf /var/lib/apt/lists/*

WORKDIR /etc/unbound
COPY unbound.conf .
COPY bootup.sh .
CMD ["./bootup.sh"]
