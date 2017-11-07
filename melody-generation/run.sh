#!/bin/bash

cd char-rnn-tensorflow
python3 sample.py | sed 's/\\n/\n/g' > ../melody.abc
cat ../melody.abc


cd ../abcmidi

make

echo "converting to midi"
./abc2midi ../melody.abc

brew install timidity

echo "convert to wav"
timidity melody1.mid -Ow

play melody1.wav



