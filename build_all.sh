#!/bin/sh
set -e
for run in `find . -name run.sh`; do
  dir=$(basename "$(dirname "$run")")
  docker build -t "$dir-image" "$dir"
done
