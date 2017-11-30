#!/bin/bash

if [ "$(expr substr $(uname -s) 1 10)" == "MINGW64_NT" ]; then
    # Running under 64 bits Windows NT platform
	shopt -s expand_aliases
	source ~/.bashrc
fi

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
