#!/bin/bash

ARTIST=$1


printf "\n\n********Generating Lyrics*********\n\n"
#Weird Al Yankovic / Bob Dylan
python3 lyric_generator.py --artist Lady Gaga > input.txt

cat input.txt; 


printf "********Above are the Generated Lyrics*********\n\n"; 


printf "********Generating Voice for Text*********\n\n"; 
python3 txt2speech.py


printf "********Auto-tuning Voice*********\n\n"
python3 changePitch.py

printf "\n\n********Done making masterpiece and playing it!*********\n\n"
play out.wav
