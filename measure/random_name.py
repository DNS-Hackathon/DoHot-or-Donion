from strings import ascii_lowercase
from random import choices


def random_domain_name():
    random = "".join(random.choices(ascii_lowercase, k=36))
    return f"DNSHACKATHON-{random}.se"


def random_container_name():
    return "".join(random.choices(ascii_lowercase, k=12))
