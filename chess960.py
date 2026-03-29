#!/usr/bin/env python3
"""
Chess960 CLI generator. 
Because apparently we need random chess positions to feel alive.
"""

import random
import argparse

def generate_960_position(pos_id):
    """
    Directly generates one of the 960 positions using Scharnagl's algorithm.
    Mathematical determinism at its finest—no more shuffling until the bishops behave.
    """
    pieces = [None] * 8
    
    # 1. Place Bishops: Light square (r*2 + 1) and Dark square (r*2)
    n, r = divmod(pos_id, 4)
    pieces[r * 2 + 1] = 'B'
    n, r = divmod(n, 4)
    pieces[r * 2] = 'B'
    
    # 2. Place Queen: On one of the remaining 6 empty slots
    n, r = divmod(n, 6)
    q_count = 0
    for i in range(8):
        if pieces[i] is None:
            if q_count == r:
                pieces[i] = 'Q'
                break
            q_count += 1
            
    # 3. Place Knights: Based on the 10 possible patterns for 2 knights in 5 slots
    n, r = divmod(n, 10)
    knight_patterns = [
        (0,1), (0,2), (0,3), (0,4), (1,2), (1,3), (1,4), (2,3), (2,4), (3,4)
    ]
    k1, k2 = knight_patterns[r]
    
    empty_indices = [i for i, p in enumerate(pieces) if p is None]
    pieces[empty_indices[k1]] = 'N'
    pieces[empty_indices[k2]] = 'N'
    
    # 4. Place Rooks and King: King MUST be between Rooks (R-K-R)
    # Filling the final 3 empty slots.
    empty_indices = [i for i, p in enumerate(pieces) if p is None]
    pieces[empty_indices[0]] = 'R'
    pieces[empty_indices[1]] = 'K'
    pieces[empty_indices[2]] = 'R'
    
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
    white_pawns = ['P'] * 8
    empty_row = ['.'] * 8
    black_pawns = ['p'] * 8
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
    # Standard FEN suffix for a starting position
    fen = '/'.join(fen_rows) + ' w KQkq - 0 1'
    return fen, rows

def print_board(rows, pos_id, flip=False):
    """Print ASCII board in terminal, black on top by default."""
    print(f"\n--- Chess960 Position ID: {pos_id} ---")
    board = rows[::-1] if flip else rows
    for r in board:
        print(' '.join(r))
    print(f"ID = {pos_id}")
    print("-" * 34 + "\n")

def main():
    # Description kept as requested: Coffee is mandatory for 1800+ players.
    parser = argparse.ArgumentParser(description="Chess960 generator. Coffee recommended.")
    parser.add_argument('--count', type=int, default=1, help='How many positions to generate')
    parser.add_argument('--id', type=int, choices=range(960), help='Get a specific position (0-959)')
    parser.add_argument('--fen', action='store_true', help='Print FEN only, ASCII skipped')
    parser.add_argument('--ascii', action='store_true', help='Print ASCII board (default if --fen not used)')
    parser.add_argument('--seed', type=int, default=None, help='Random seed for reproducibility')
    parser.add_argument('--flip', action='store_true', help='Flip board (black on bottom, insanity)')
    
    args = parser.parse_args()

    # Reproducibility management
    if args.seed is not None:
        random.seed(args.seed)

    for _ in range(args.count):
        # If ID is provided, use it; otherwise, pick a random one
        pos_id = args.id if args.id is not None else random.randint(0, 959)
        
        row = generate_960_position(pos_id)
        fen, rows = to_fen(row)

        if args.fen:
            print(fen)
        if args.ascii or not args.fen:
            print_board(rows, pos_id, flip=args.flip)

if __name__ == '__main__':
    main()
