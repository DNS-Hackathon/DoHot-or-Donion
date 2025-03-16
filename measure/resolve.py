from subprocess import DEVNULL, run
from logging import getLogger
from time import sleep

from .settings import TOR_PROTOCOLS
from .random_name import random_domain_name
from .models import Condition, Measurement

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
    domain_name = random_domain_name()
    if condition.tor:
        resolver = "172.17.0.1"
        port = 1337
    else:
        resolver = "1.1.1.1"
        port = 53
    logger.info(f"Starting {protocol}")
    run(DOCKER_RUN[protocol], stdout=DEVNULL)
    logger.info(f"Sending random NXDOMAIN query for {domain_name}")
    dig_begin = datetime.datetime.now()
    run(["dig", f"@{resolver}", "-p", str(port), domain_name])
    dig_end = datetime.datetime.now()
    run(["docker", "stop", condition.container_name])
    return Measurement(
        condition=condition,
        domain_name=domain_name,
        dig_begin=dig_begin,
        dig_end=dig_end,
    )
