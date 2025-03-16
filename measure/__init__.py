from logging import getLogger
from itertools import product

from .settings import TOR_PROTOCOLS
from .circuit_counter import circuit_counter
from .query import query

logger = getLogger(__name__)


def anonymous_dns(
    max_replicate: int,
    domain_type: list[str],
    protocol: list[str],
    queries_per_circuit: list[int],
    target_dns_server: list[str],
    type: list[str],
    tor: list[str],
):
    for (
        the_queries_per_circuit,
        the_domain_type,
        the_protocol,
        the_target_dns_server,
        the_type,
        the_tor,
    ) in product(
        queries_per_circuit, domain_type, protocol, target_dns_server, type, tor
    ):
        is_tor_config = the_tor == "none"
        is_tor_protocol = the_protocol in TOR_PROTOCOLS
        if is_tor_config != is_tor_protocol:
            continue
        counter = circuit_counter(the_queries_per_circuit)
        for the_replicate in range(1, 1+max_replicate):
            if the_queries_per_circuit > 1 and the_replicate > 1:
                logger.debug(
                    "Skipping combination of queries_per_circuit and maximuim replicates both greater than 1"
                )
                continue

            if protocol in TOR_PROTOCOLS:
                next(counter)
            logger.info(
                f"TODO: Request {the_type} record for {the_domain_type} domain by {the_protocol} from {the_target_dns_server}, tor configuration {the_tor}"
            )
            domain = "example.com"
            yield {
                "queries_per_circuit": the_queries_per_circuit,
                "domain_type": the_domain_type,
                "protocol": the_protocol,
                "target_dns_server": the_target_dns_server,
                "type": the_type,
                "tor": the_tor,
                "replicate": the_replicate,
                "domain": domain,
                "duration": query(),
            }
