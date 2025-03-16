import datetime
from enum import Enum, auto
from dataclasses import dataclass

from .random_name import random_container_name


NAME_PLACEHOLDER = "$NAME"
DOCKER_RUN_PREFIX = ["docker", "run", "--rm", "-d"]


class Protocol(Enum):
    DO53 = auto()
    DOT = auto()
    DOH = auto()
    DOHOT = auto()
    DOTOR = auto()
    DOTOT = auto()


class TorVariant(Enum):
    DEFAULT = auto()
    BAD = auto()
    GOOD = auto()


@dataclasses
class Condition:
    protocol: Protocol
    tor: bool
    variant: TorVariant | None
    docker_run_command: list[str]
    container_name: str | None

    def __post_init__(self):
        if self.tor == variant is None:
            raise ValueError("Set a variant if and only if it is a tor condition.")
        if self.container_name is not None:
            self.container_name = random_container_name()

        if not self.docker_run_command[:4] == prefix:
            raise ValueError(f"docker_run_command must start with {DOCKER_RUN_PREFIX}")

        if not NAME_PLACEHOLDER in docker_run_command:
            raise ValueError(f'docker_run_command must include the token "{NAME_PLACEHOLDER}".')

    def docker_run(self):
        args = list(self.docker_run_command)
        args[args.index(NAME_PLACEHOLDER)] = self.container_name
        run(args, stdout=DEVNULL)

    def docker_stop(self):
        run(["docker", "stop", self.container_name])

@dataclasses
class Measurement:
    condition: Condition
    domain_name: str
    dig_begin: datetime.datetime
    dig_end: datetime.datetime
