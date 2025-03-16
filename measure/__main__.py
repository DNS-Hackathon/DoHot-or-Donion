from sys import stdout
from logging import basicConfig, WARNING
from csv import DictWriter
from argparse import ArgumentParser

from .resolve import resolve
from .save import fieldnames, row
from .settings import CONDITIONS

basicConfig(level=WARNING)

parser = ArgumentParser()
parser.add_argument("-r", "--replicates", type=int, default=100)
parser.add_argument("-s", "--wait-for-container-start", type=int, default=20)
args = parser.parse_args()

writer = DictWriter(stdout, fieldnames=fieldnames())
try:
    writer.writeheader()
    for _ in range(args.replicates):
        for condition in CONDITIONS:
            measurement = resolve(
                condition, wait_for_container_start=args.wait_for_container_start
            )
            writer.writerow(row(measurement))
except BrokenPipeError:
    pass
