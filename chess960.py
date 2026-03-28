#!/usr/bin/env python3
"""
Chess960 CLI generator.
Because apparently we need random chess positions to feel alive.
"""

import random
import argparse

def generate_chess960(seed=None):
    """Generate a valid Chess960 starting position."""
    if seed is not None:
        random.seed(seed)

    while True:
        pieces = ['R','R','N','N','B','B','Q','K']
        random.shuffle(pieces)

        # Bishops on opposite colors
        bishops = [i for i, p in enumerate(pieces) if p == 'B']
        if bishops[0] % 2 == bishops[1] % 2:
            continue

        # King between rooks
        king_idx = pieces.index('K')
        rook_idxs = [i for i, p in enumerate(pieces) if p == 'R']
        if not (min(rook_idxs) < king_idx < max(rook_idxs)):
            continue

        return pieces

def to_fen(row):
    """Convert top row to FEN format, white pawns on row 2."""
    def row_to_fen(r):
        fen = ''
        empty = 0
        for c in r:
            if c == '.':
                empty += 1
            else:
                if empty != 0:
                    fen += str(empty)
                    empty = 0
                fen += c
        if empty != 0:
            fen += str(empty)
        return fen

    white_row = row
    white_pawns = ['P']*8
    empty_row = ['.']*8
    black_pawns = ['p']*8
    black_row = [c.lower() for c in row]

    rows = [
        ''.join(black_row),
        ''.join(black_pawns),
        ''.join(empty_row),
        ''.join(empty_row),
        ''.join(empty_row),
        ''.join(empty_row),
        ''.join(white_pawns),
        ''.join(white_row)
    ]

    fen_rows = [row_to_fen(r) for r in rows]
    fen = '/'.join(fen_rows) + ' w KQkq - 0 1'
    return fen, rows

def print_board(rows, flip=False):
    """Print ASCII board in terminal, black on top by default."""
    board = rows[::-1] if flip else rows
    for r in board:
        print(' '.join(r))
    print('')  # extra line for sanity

def main():
    parser = argparse.ArgumentParser(description="Chess960 generator. Coffee recommended.")
    parser.add_argument('--count', type=int, default=1, help='How many positions to generate')
    parser.add_argument('--fen', action='store_true', help='Print FEN only, ASCII skipped')
    parser.add_argument('--ascii', action='store_true', help='Print ASCII board (default if --fen not used)')
    parser.add_argument('--seed', type=int, default=None, help='Random seed for reproducibility')
    parser.add_argument('--flip', action='store_true', help='Flip board (black on bottom, insanity)')
    args = parser.parse_args()

    for i in range(args.count):
        row = generate_chess960(seed=args.seed)
        fen, rows = to_fen(row)

        if args.fen:
            print(fen)
        if args.ascii or not args.fen:
            print_board(rows, flip=args.flip)

if __name__ == '__main__':
    main()
