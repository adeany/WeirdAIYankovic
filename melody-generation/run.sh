#!/bin/bash

if [ "$(expr substr $(uname -s) 1 10)" == "MINGW64_NT" ]; then
    # Running under 64 bits Windows NT platform
	shopt -s expand_aliases
	source ~/.bashrc
fi

printf "\n******** Cleaning up *********\n"
rm *.abc
rm *.mid
rm *.wav

printf "\n******** Generating random ABC notation *********\n"
cd char-rnn-tensorflow
python3 sample.py  > ../melody_tmp.abc
cd ..
echo -e "X : 1\n K : D\n$(cat melody_tmp.abc)" > melody_tmp.abc
sed 's/\\n/\n/g' < melody_tmp.abc > melody.abc
cat melody.abc

printf "\n******** Convert ABC to MIDI *********\n"
cd abcmidi
make
./abc2midi ../melody.abc
cd ..

printf "\n******** Convert MIDI to WAV *********\n"
brew install timidity
timidity melody1.mid -Ow

printf "\n\n******** Done making masterpiece and playing it! *********\n"
play melody1.wav
