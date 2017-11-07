#!/bin/bash

# Required to run it on my machine, sorry (David)
shopt -s expand_aliases
source ~/.bashrc

python /char-rnn-tensorflow/sample.py > melody.abc
python read_abc.py melody.abc --syn_e
