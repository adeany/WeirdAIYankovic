#!/bin/bash

printf "\n******** Generating Lyrics *********\n"
if [ $# == 0 ]; then
	python3 lyricGenerator.py --artist Chvrches
else
	python3 lyricGenerator.py --artist "$@"
fi

printf "\n\n******** Printing generated Lyrics *********\n"
cat lyrics.txt

printf "\n\n******** Running TTS *********\n"
python3 txt2speech.py

printf "\n\n******** Auto-tuning Voice *********\n"
python3 changePitch.py

printf "\n\n******** Done making masterpiece and playing it! *********\n"
play lyrics_pitched.wav
