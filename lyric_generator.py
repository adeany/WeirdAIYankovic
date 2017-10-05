import random
import argparse
import pickle
import os
from tswift import Artist

start = '>'
end = '<'


def get_lyrics(artist_name):
    lyrics = []
    artist = Artist(artist_name)
    print('=== Found artist:', artist_name, '===')
    for song in artist.songs:
        print('Fetched lyrics:', song.title)
        lyrics.append(song.lyrics)

    print('=== Fetched all lyrics ===\n')

    return lyrics


def add_word(chain, previous, word):
    if previous not in chain:
        chain[previous] = []

    chain[previous].append(word)


def train_markov_chain(lyrics):
    chain = {}

    for lyric in lyrics:
        lyric = lyric.replace('\n', ' \n ')
        words = lyric.split(' ')

        previous = start
        for word in words:
            if word != '':
                add_word(chain, previous, word)
                previous = word

        add_word(chain, previous, end)

    return chain


def generate_new_lyrics(chain):
    # a list for storing the generated words
    words = []
    current = start

    while current != end:
        current = random.choice(chain[current])
        words.append(current)

    return ' '.join(words[:-1]).replace('\n ', '\n')


def main():
    # parse arguments
    parser = argparse.ArgumentParser(description='Generate lyrics.')
    parser.add_argument('--artist', nargs='*',
                        help='name of artist to search for', default=['Chvrches'])
    parser.add_argument('--fetch', help='re-fetch markov chain',
                        action='store_true')
    args = parser.parse_args()

    artist_name = ' '.join(args.artist)
    fetch = args.fetch

    file_name = artist_name + '.markov'

    # Load chain from file if we previously saved it
    if os.path.isfile(file_name) and not fetch:
        with open(file_name, 'rb') as file:
            chain = pickle.load(file)

        print('=== Loaded', artist_name, 'chain from file ===\n')
    else:
        lyrics = get_lyrics(artist_name)
        chain = train_markov_chain(lyrics)

        # Save chain to file for later
        with open(file_name, 'wb') as file:
            pickle.dump(chain, file, protocol=pickle.HIGHEST_PROTOCOL)

    print(generate_new_lyrics(chain))

if __name__ == '__main__':
    main()
