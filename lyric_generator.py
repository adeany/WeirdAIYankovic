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
        lyric = lyric.replace('(', '').replace(')', '').replace('#', '')
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
    # Parse arguments
    parser = argparse.ArgumentParser(description='Generate lyrics.')
    parser.add_argument('--artist', nargs='+',
                        help='name of artist to search for', default=['Chvrches'])
    parser.add_argument('--fetch', help='re-fetch markov chain',
                        action='store_true')
    args = parser.parse_args()

    artist_name = ' '.join(args.artist)
    fetch = args.fetch

    script_path = os.path.abspath(__file__)  # i.e. /path/to/dir/foobar.py
    script_dir = os.path.split(script_path)[0]  # i.e. /path/to/dir/
    rel_path = 'chain_data/' + artist_name + '.markov'
    file_name = os.path.join(script_dir, rel_path)

    # Load chain from file if we previously saved it
    if os.path.isfile(file_name) and not fetch:
        with open(file_name, 'rb') as file:
            chain = pickle.load(file)

        #print('=== Loaded', artist_name, 'chain from file ===\n')
    else:
        lyrics = get_lyrics(artist_name)
        chain = train_markov_chain(lyrics)

        # Save chain to file for later
        with open(file_name, 'wb') as file:
            pickle.dump(chain, file, protocol=pickle.HIGHEST_PROTOCOL)

    print(generate_new_lyrics(chain))


if __name__ == '__main__':
    main()
