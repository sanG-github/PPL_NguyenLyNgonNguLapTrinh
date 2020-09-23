#!/bin/bash

cd $(dirname $0)

docker run -it --rm \
  -v "$(pwd)/initial:/app" \
  ppl-ass1:v1 bash test.sh