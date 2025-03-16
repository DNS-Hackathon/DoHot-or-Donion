from subprocess import DEVNULL, run
from logging import getLogger
from time import sleep

from .settings import TOR_PROTOCOLS
from .random_name import random_domain_name
from .models import Condition, Measurement

logger = getLogger(__name__)


def resolve(condition: Condition):
    domain_name = random_domain_name()
    if condition.tor:
        resolver = "172.17.0.1"
        port = 1337
    else:
        resolver = "1.1.1.1"
        port = 53
    logger.info(f"Starting {protocol}")
    run(DOCKER_RUN[protocol], stdout=DEVNULL)
    sleep(20)
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
