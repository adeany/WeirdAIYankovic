#!/bin/bash
shopt -s expand_aliases
source ~/.bashrc

ARTIST=$1


printf "******** Generating Lyrics *********\n"
#Weird Al Yankovic / Bob Dylan
python3 lyric_generator.py --artist Lady Gaga

printf "\n******** Printing generated Lyrics *********\n"
cat lyrics.txt

printf "\n\n******** Running TTS *********\n"
python3 txt2speech.py

printf "\n\n******** Auto-tuning Voice *********\n"
python3 changePitch.py

printf "\n\n******** Done making masterpiece and playing it! *********\n"
play out.wav
