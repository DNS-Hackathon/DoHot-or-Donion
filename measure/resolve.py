import datetime
from subprocess import check_output, CalledProcessError
from logging import getLogger
from time import sleep

from .random_name import random_domain_name
from .models import Condition, Measurement

logger = getLogger(__name__)


def resolve(
    condition: Condition,
    resolver: str = "172.17.0.1",
    port: int = 1337,
    wait_for_container_start: int = 20,
):
    domain_name = random_domain_name()
    logger.info("Starting %s", condition.protocol)
    condition.docker_run()
    sleep(wait_for_container_start)
    logger.info("Sending random NXDOMAIN query for %s", domain_name)
    dig_begin = datetime.datetime.now()
    try:
        dig_out = check_output(
            ["dig", f"@{resolver}", "-p", str(port), domain_name]
        ).decode("utf-8")
    except CalledProcessError:
        dig_out = None
    dig_end = datetime.datetime.now()
    condition.docker_stop()
    return Measurement(
        condition=condition,
        domain_name=domain_name,
        dig_begin=dig_begin,
        dig_end=dig_end,
        dig_out=dig_out,
    )
