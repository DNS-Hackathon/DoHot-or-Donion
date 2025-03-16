from sys import stdout
from logging import basicConfig, WARNING
from csv import DictWriter

from .resolve import resolve
from .save import fieldnames, row
from .settings import CONDITIONS

basicConfig(level=WARNING)

writer = DictWriter(stdout, fieldnames=fieldnames())
try:
    writer.writeheader()
    for condition in CONDITIONS:
        measurement = resolve(condition)
        writer.writerow(row(measurement))
        break
except BrokenPipeError:
    pass
