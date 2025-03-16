from argparse import ArgumentParser
from functools import partial

from .settings import DEFAULTS, MAX_REPLICATE


def ui(function):
    kwargs = vars(parser.parse_args())
    for key, default in DEFAULTS.items():
        if kwargs[key] is None:
            kwargs[key] = default
    try:
        return function(**kwargs)
    except ValueError as exception:
        parser.error(str(exception))


def at_least(minimum: int, text: str) -> int:
    value = int(text)
    if value < minimum:
        raise ValueError("There must be at least two relays.")
    return value


parser = ArgumentParser()
parser.add_argument(
    "-p",
    "--protocol",
    action="append",
    choices=DEFAULTS["protocol"],
)
parser.add_argument(
    "-T",
    "--tor",
    action="append",
    choices=DEFAULTS["tor"],
)
parser.add_argument(
    "-s",
    "--target-dns-server",
    action="append",
)
parser.add_argument(
    "-r",
    "--max-replicate",
    type=partial(at_least, 1),
    default=MAX_REPLICATE,
    help="Run the same query multiple times. The first one may take longer because of no caches, and the rest should be with caches.",
)
parser.add_argument(
    "-c",
    "--queries-per-circuit",
    type=partial(at_least, 1),
    action="append",
)
parser.add_argument(
    "-t",
    "--type",
    action="append",
    choices=DEFAULTS["type"],
)
parser.add_argument(
    "-d",
    "--domain-type",
    choices=DEFAULTS["domain_type"],
    action="append",
)


if __name__ == "__main__":
    from pprint import pprint

    ui(lambda **kwargs: pprint(dict(**kwargs)))
