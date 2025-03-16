from sys import stdout
from logging import basicConfig, WARNING
from csv import DictWriter

from .ui import ui
from .__init__ import anonymous_dns


basicConfig(level=WARNING)

writer = DictWriter(
    stdout,
    fieldnames=[
        "queries_per_circuit",
        "domain_type",
        "protocol",
        "target_dns_server",
        "type",
        "tor",
        "replicate",
        "domain",
        "duration",
    ],
)

try:
    writer.writeheader()
    for record in ui(anonymous_dns):
        writer.writerow(record)
except BrokenPipeError:
    pass
