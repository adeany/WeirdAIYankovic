

#script to convert generated melody.abc to wav
cd abcmidi
make
echo "converting to midi"
./abc2midi ../melody.abc
brew install timidity


echo "convert to wav"
cd ..
timidity melody*.mid -Ow
play melody*.wav

