#!/bin/bash

cd ./lyric-generation
./run.sh

cd ../melody-generation
./run.sh

cd ..
python3 mixed.py
play mixed.wav
