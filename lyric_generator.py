import random
import argparse
from tswift import Artist

start = ">"
end = "<"

def get_lyrics(artist_name):
    lyrics = []
    artist = Artist(artist_name)
    print("Found artist")
    for song in artist.songs:
        # print(song.lyrics)
        lyrics.append(song.lyrics.replace("\n", " "))

    print("Appended all")
    # print(lyrics)

    return lyrics


def add_word(transitions, previous, word):
    if previous not in transitions:
        transitions[previous] = []

    transitions[previous].append(word)


def train_markov_chain(lyrics):
    transitions = {}

    # print(lyrics)
    for lyric in lyrics:
        # lyric = lyric.replace("\n", " \n ")
        words = lyric.split(" ")
        print(words)
        previous = start

        for word in words:
            if word != '':
                add_word(transitions, previous, word)
                previous = word

        add_word(transitions, previous, end)

    return transitions


def generate_new_lyrics(chain):
    # a list for storing the generated words
    words = []
    current = start

    while current != end:
        current = random.choice(chain[current])
        words.append(current)

    return " ".join(words[:-1])


# parse argument
parser = argparse.ArgumentParser(description='Generate lyrics.')
parser.add_argument('name', nargs='*', help='name of artist to search for')
args = parser.parse_args()
artist_name = ' '.join(args.name)

lyrics = get_lyrics(artist_name)
# print(lyrics)
chain = train_markov_chain(lyrics)
# print(chain)
print(generate_new_lyrics(chain))