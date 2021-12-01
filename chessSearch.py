# Import stuff
# THIS FILE IS NOT COMPLETE
import chess.pgn


def print_hi(name):
    print(f'Hi, {name}')


# Main
if __name__ == '__main__':
    print_hi('PyCharm')
    pgn = open('pgn/Magnus-Carlsen_vs_Wesley-So_2021.05.30.pgn')
    game = chess.pgn.read_game(pgn)
    board = game.board()

    for move in game.mainline_moves():
        print(board.san(move))
        board.push(move)
