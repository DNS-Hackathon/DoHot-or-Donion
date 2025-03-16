from sys import stdout
from logging import basicConfig, WARNING
from csv import DictWriter

from .__init__ import measure

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
    for record in measure():
        writer.writerow(record)
except BrokenPipeError:
    pass
