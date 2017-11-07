# Weird AI Yankovic

Weird AI Yankovic is an intelligent music generator that will be able to compose new music for users to enjoy. The original compositions created from this generator will include both the melody and the lyrics to be a song.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine.

### Prerequisites

This project uses
* [Python 3](https://www.python.org/downloads/)
* [tswift package](https://github.com/brenns10/tswift)
* //TODO update prerequisites

## Usage

### Lyric Generator

```
./lyric-generator/run.sh ARTIST
```
will generate random lyrics based on the artists lyrics, use text to speech to create a audio file of them and then modify it to sound nicer. 

If there is no ARTIST parameter, the default artist is 'Chvrches'.

### Melody Generator

The melody generator uses [a RNN with Tensorflow](https://github.com/sherjilozair/char-rnn-tensorflow) for character-level language models. The RNN uses [this cleaned version](https://github.com/jukedeck/nottingham-dataset) of the ABC version of the Nottingham Music Database.

To generate a random ABC notation run:

```
./melody-generator/run.sh
```

// TODO add instruction for abc to wav
