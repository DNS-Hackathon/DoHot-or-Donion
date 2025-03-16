from random import normalvariate


def query(*_, **__):
    return max(0, normalvariate(12, 1))
