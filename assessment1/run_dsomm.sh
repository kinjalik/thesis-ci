#!/bin/bash
docker run \
    -v $(pwd)/meta.yaml:/srv/assets/YAML/meta.yaml \
    -v $(pwd)/generated.yaml:/srv/assets/YAML/generated/generated.yaml \
    -p 8080:8080 wurstbrot/dsomm
