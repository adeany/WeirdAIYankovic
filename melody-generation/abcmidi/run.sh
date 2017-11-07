# convert abc file to wav


make

echo "converting to midi"
./abc2midi cooley.abc

brew install timidity

echo "convert to wav"
timidity cooley1.mid -Ow

play cooley1.wav

