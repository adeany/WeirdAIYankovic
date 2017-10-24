#!/bin/bash
printf "\n\n********Generating Lyrics*********\n\n"
(cd marytts; 
	./gradlew run) & 
(python3 lyric_generator.py > marytts/input.txt; 
	cat marytts/input.txt; 
	printf "******** outputed generated lyrics above*********\n\n"; 
	cd marytts; 
	sleep 10; 
	python txt2wav.py)

#kill the marytts voice server
killall java


printf "\n\n********Auto-tuning Voice*********\n\n"
mv out.wav out2.wav
python3 changePitch.py


printf "\n\n********Done making masterpiece and playing it!*********\n\n"
play out.wav