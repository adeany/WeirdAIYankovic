#!/bin/bash

cd char-rnn-tensorflow
python3 sample.py | sed 's/\\n/\n/g' > ../melody.abc
cat ../melody.abc

