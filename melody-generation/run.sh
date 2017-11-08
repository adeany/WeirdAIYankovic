#!/bin/bash
#full run to generate and play melody


printf "clean up\n\n"
rm *.mid
rm *.wav


cd char-rnn-tensorflow
python3 sample.py  > ../melody1.abc


cd ..

echo -e "X = 1\n$(cat melody1.abc)" > melody2.abc

sed 's/\\n/\n/g' < melody2.abc > melody.abc

cat melody.abc


#convert abc file to wav

./convert.sh


