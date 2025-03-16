#!/bin/bash

pkill -f unbound
unbound -d
dig @localhost kau.se +noall
