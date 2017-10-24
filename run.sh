#!/bin/bash

ARTIST=$1


printf "\n\n********Generating Lyrics*********\n\n"
python3 lyric_generator.py  > input.txt

cat input.txt; 


printf "********Above are the Generated Lyrics*********\n\n"; 


printf "********Generating Voice for Text*********\n\n"; 
python txt2speech.py


printf "\n\n********Auto-tuning Voice*********\n\n"
mv out.wav previous_out.wav
python3 changePitch.py


printf "\n\n********Done making masterpiece and playing it!*********\n\n"
play out.wav