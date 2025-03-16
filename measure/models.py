import datetime
from enum import Enum, auto
from dataclasses import dataclass
from subprocess import run, DEVNULL

from .random_name import random_container_name


NAME_PLACEHOLDER = "$NAME"
DOCKER_RUN_PREFIX = ["docker", "run", "--rm", "-d"]


@dataclass
class Protocol(Enum):
    DO53 = auto()
    DOT = auto()
    DOH = auto()
    DOHOT = auto()
    DOTOR = auto()
    DOTOT = auto()


@dataclass
class Variant(Enum):
    DEFAULT = auto()
    BAD = auto()
    GOOD = auto()


@dataclass
class Condition:
    protocol: Protocol
    tor: bool
    variant: Variant | None
    docker_run_command: list[str]
    container_name: str | None = None

    def __post_init__(self):
        if self.tor == (self.variant is None):
            raise ValueError("Set a variant if and only if it is a tor condition.")
        if self.container_name is None:
            self.container_name = random_container_name()

        if self.docker_run_command[:4] not in (DOCKER_RUN_PREFIX, ["false", "$NAME"]):
            raise ValueError(f"docker_run_command must start with {DOCKER_RUN_PREFIX}")

        if NAME_PLACEHOLDER not in self.docker_run_command:
            raise ValueError(
                f'docker_run_command must include the token "{NAME_PLACEHOLDER}".'
            )

    def docker_run(self):
        args = list(self.docker_run_command)
        args[args.index(NAME_PLACEHOLDER)] = self.container_name
        run(args, stdout=DEVNULL, check=True)

    def docker_stop(self):
        run(["docker", "stop", self.container_name], check=True, stdout=DEVNULL)


@dataclass
class Measurement:
    condition: Condition
    domain_name: str
    dig_begin: datetime.datetime
    dig_end: datetime.datetime
    dig_out: str | None
