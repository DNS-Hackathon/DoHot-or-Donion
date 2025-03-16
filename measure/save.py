import datetime

from .models import Measurement
from .settings import CONDITIONS


def fieldnames():
    return list(
        row(
            Measurement(
                condition=CONDITIONS[0],
                domain_name="example.com",
                dig_begin=datetime.datetime.now(),
                dig_end=datetime.datetime.now(),
                dig_out="foo",
            )
        )
    )


def row(measurement):
    return {
        "protocol": measurement.condition.protocol.name,
        "variant": (
            None
            if measurement.condition.variant is None
            else measurement.condition.variant.name
        ),
        "tor": "TRUE" if measurement.condition.tor else "FALSE",
        "dig_begin": measurement.dig_begin,
        "dig_end": measurement.dig_end,
        "dig_out": measurement.dig_out,
    }
