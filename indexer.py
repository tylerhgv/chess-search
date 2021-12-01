# Import stuff
import chess.pgn
import time
import ujson
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
import nltk
import string
import re


def index_docs(f):
    """
    Build the data files for docs and construct inverted index files
    :param f: Name of raw data file (.pgn)
    :type f: str
    """

    # Begin counter
    t_start = time.perf_counter()

    # Read file and prep variable
    pgn = open(f'pgn/{f}.pgn')
    docs = {}
    terms = {}
    plies = {}

    # Iterate over each game
    i = 0
    while True:
        i += 1
        game = chess.pgn.read_game(pgn)
        # Break condition
        if game is None:
            break

        # Extract game info into dict
        print(f'[INFO] Processing game #{i}...', end='')
        headers = game.headers
        moves = str(game.mainline_moves()).split(' 4.', 1)[0]
        white = str(f'{headers["White"]} ({headers["WhiteElo"]})')
        black = str(f'{headers["Black"]} ({headers["BlackElo"]})')
        game_info = {
            'event': headers['Event'],
            'link': headers['Site'],
            'white': white,
            'black': black,
            'result': headers['Result'],
            'date': headers['UTCDate'],
            'openingName': headers['Opening'],
            'openingMoves': moves,
        }
        docs[i] = game_info

        # Build inverted index for opening names
        terms_temp = index_terms(headers['Opening'])
        for t in terms_temp:
            if t not in terms:
                terms[t] = []
            terms[t].append(i)

        # Build inverted index for opening plies
        plies_temp = index_plies(moves)
        j = 0
        while j < len(plies_temp):
            ply_index = j + 1
            ply = plies_temp[j]
            if ply not in plies:
                plies[ply] = {}
            if ply_index not in plies[ply]:
                plies[ply][ply_index] = []
            plies[ply][ply_index].append(i)
            j += 1

        # End an iteration
        print(f'DONE')

    # Write to files
    with open('data/docs_pretty.json', 'w+') as outfile:
        ujson.dump(docs, outfile, indent=4)
    with open('data/docs.json', 'w+') as outfile:
        ujson.dump(docs, outfile)
    with open('data/terms.json', 'w+') as outfile:
        ujson.dump(terms, outfile)
    with open('data/plies.json', 'w+') as outfile:
        ujson.dump(plies, outfile)

    # End function
    t_elapsed = round(time.perf_counter() - t_start, 2)
    print(f'[INFO] All games successfully processed. Elapsed time: {t_elapsed}s')


def index_terms(s):
    """
    Clean & tokenize a string, then build a list of terms
    :param s: Input string
    :type s: str
    :return: List of terms
    :rtype: list
    """

    # Clean punctuation
    for word in s:
        if word in string.punctuation:
            s = s.replace(word, " ")

    # Normalize case
    s = s.lower()

    # Tokenize
    tokens = word_tokenize(s)

    # Stem
    stemmer = PorterStemmer()
    tokens_stemmed = [stemmer.stem(t) for t in tokens]

    # Remove duplicates
    result = list(set(tokens_stemmed))

    # Remove contraction leftovers (brute force for now)
    stubs = ['s', 't']
    for x in stubs:
        if x in result:
            result.remove(x)

    # Return list of terms
    return result


def index_plies(s):
    """
    Build a list of plies from a string containing moves
    :param s: Input string
    :type s: str
    :return: List of plies
    :rtype: list
    """

    # Remove move numbers
    moves = re.sub(r'\d\.', '', s)

    # Normalize case
    moves = moves.lower()

    # Tokenize
    result = word_tokenize(moves)

    # Return list of plies
    return result


if __name__ == '__main__':
    print(f'[INFO] Starting...')
    filename = 'lichess_db_standard_rated_2013-01'
    nltk.download('punkt')
    index_docs(filename)
