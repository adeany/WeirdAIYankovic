# Weird AI Yankovic

Weird AI Yankovic is an intelligent music generator that will be able to compose new music for users to enjoy. The original compositions created from our generator will include both the melody and the lyrics to be a song.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine.

### Prerequisites

This project uses [Python 3](https://www.python.org/downloads/) and the [tswift package](https://github.com/brenns10/tswift).

## Usage

### Lyric Generator

```
python lyric_generator.py --artist Queen
```
will generate random lyrics based on real Queen lyrics. For performance reason a file named Queen.markov will be created in the same directory.

The default artist, if there is no --artist parameter is Chvrches.

### Text To Speech

Steps to Run 
1. Go into marytts directory
2. ./gradlew run
3. Modify input.txt
4. python txt2wav.py
5. the wav file is output_wav.wav

Todo: the run.sh script somewhat does this but the user needs to ^C the program after 5 sec for it to finish.

### Autotune

```
> python3 changePitch.py 
> play output.wav
```
will generate an autotuned music file and play it through the terminal. 
