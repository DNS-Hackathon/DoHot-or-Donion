from subprocess import DEVNULL, run
from logging import getLogger
from time import sleep

from .settings import TOR_PROTOCOLS
from .random_domain_name import random_domain_name
from .models import Condition

logger = getLogger(__name__)


DOCKER_RUN = {
    "dohot-worst": ["docker", "run", "--rm", "-d", "-p", "1337:53/tcp", "-p", "1337:53/udp", "--name", "dohot-container", "dohot-image"],
    "dohot-best": ["docker", "run", "--rm", "-d", "-p", "1337:53/tcp", "-p", "1337:53/udp", "--name", "dohot-container", "-e", "ENTRY_NODES=se", "-e", "EXIT_NODES=se", "-e", "HOPS=2", "dohot-image"],
    "doh": ["docker", "run", "--rm", "-d", "-p", "1337:53/tcp", "-p", "1337:53/udp", "--name", "doh-container", "doh-image"],
    "dotot-worst": ["docker", "run", "--rm", "-d", "-p", "1337:8053/tcp", "-p", "1337:8053/udp", "--name", "dotot-container", "dotot-image"],
    "dotot-best": ["
docker", "run", "--rm", "-d", "-p", "1337:8053/tcp", "-p", "1337:8053/udp", "--name", "dotot-container", "-e", "ENTRY_NODES=se", "-e", "EXIT_NODES=se", "-e", "HOPS=2", "dotot-image"],
}


def measure(condition: Condition):
    if condition.tor:
        resolver = "172.17.0.1"
        port = 1337
    else:
        resolver = "1.1.1.1"
        port = 53
    logger.info(f"Starting {protocol}")
    run(DOCKER_RUN[protocol], stdout=DEVNULL)
    logger.info("Sending random NXDOMAIN query")
    run(["dig", f"@{resolver}", "-p", str(port), random_domain_name()

    run(["docker", "stop dohot-container
elif [ $1 = 'doh' ]; then
    echo "$(date +"%Y-%m-%dT%H:%M:%S"): Stopping DoH"
    docker stop doh-container
elif [[ $1 = "dotot"* ]]; then
    echo "$(date +"%Y-%m-%dT%H:%M:%S"): Stopping DoToT"
    docker stop dotot-container
fi
