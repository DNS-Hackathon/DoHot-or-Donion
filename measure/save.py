from enum import Enum
from dataclasses import fields

from .models import Condition, Measurement
from .settings import CONDITIONS


def fieldnames():
    condition = CONDITIONS[0]
    return list(
        row(
            Measurement(
                conditions=CONDITIONS[0],
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
