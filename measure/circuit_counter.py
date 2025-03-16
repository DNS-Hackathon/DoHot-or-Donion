from logging import getLogger

logger = getLogger(__name__)


def circuit_counter(queries_per_circuit):
    index = 0
    while True:
        if index >= queries_per_circuit:
            logger.debug("Creating a new tor circuit")
            logger.info("TODO: Get new circuit.")
            index = 0
        yield index
