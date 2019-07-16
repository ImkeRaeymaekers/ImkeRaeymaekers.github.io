#! /bin/bash

ROOT="$( cd "$(dirname "$0")/.." ; pwd -P )"
mkdir -p $ROOT/tmp

source $ROOT/venv/bin/activate
python $ROOT/src/generate_urbanus_strips.py > $ROOT/src/tmp/urbanus_strips.markdown && cp $ROOT/src/tmp/urbanus_strips.markdown $ROOT/src/content/posts/urbanus_strips.markdown

