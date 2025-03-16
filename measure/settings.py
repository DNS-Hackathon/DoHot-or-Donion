MAX_REPLICATE = 64
TOR_PROTOCOLS = ["dohot", "dotot", "dotor", "donion"]
DEFAULTS = {
    "tor": ["none", "fast", "default"],
    "protocol": ["hosts", "dns", "dot", "doh"] + TOR_PROTOCOLS,
    "target_dns_server": ["9.9.9.9"],
    "domain_type": ["existing", "random"],
    "queries_per_circuit": [1, 10, 100],
    "type": ["A"],
}
