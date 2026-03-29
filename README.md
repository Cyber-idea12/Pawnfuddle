# Pawnfuddle

**Pawnfuddle – High-Precision Chess960 (Fischer Random) Generator**

Pawnfuddle is a lightweight CLI tool that generates valid Chess960 starting positions using the official **Scharnagl's Algorithm**. It maps every possible position to a unique ID (0-959), ensuring mathematical determinism and compatibility with international tournament standards.

---

## Features

- **Scharnagl’s Algorithm**: Direct mapping of IDs (0-959) to positions. No more "shuffling and praying" for valid bishops.
- **Deterministic Generation**: Generate specific positions via `--id` for tournaments or study.
- **Engine Ready**: Full FEN string output compatible with Stockfish and modern chess GUIs.
- **Terminal Optimized**: Clean ASCII board visualization with "Flip" support for black-side perspective.
- **Zero Dependencies**: Pure Python 3. Works on Linux, BSD, and macOS out of the box.

---

## Installation

1. **Clone the repository**:
```bash
git clone [https://github.com/Cyber-idea12/Pawnfuddle.git](https://github.com/Cyber-idea12/Pawnfuddle.git)
cd Pawnfuddle
```

2. **Run directly**:
```bash
python3 pawnfuddle.py [flags]
```

---

## Usage

### Generate a random Chess960 position
```bash
python3 pawnfuddle.py
```

### Generate a specific position by ID (0-959)
*Example: ID 518 is the classical chess starting position.*
```bash
python3 pawnfuddle.py --id 518
```

### Generate multiple positions
```bash
python3 pawnfuddle.py --count 5
```

### Output FEN strings only
```bash
python3 pawnfuddle.py --fen
```

### Use a seed for reproducibility
```bash
python3 pawnfuddle.py --seed 1800 --count 3
```

---

## CLI Flags Summary

| Flag       | Type | Description                                           |
|------------|------|-------------------------------------------------------|
| `--id ID`  | int  | Fetch a specific position (0-959).                    |
| `--count N`| int  | Number of positions to generate (default=1).          |
| `--fen`    | bool | Print FEN only, skip ASCII board.                     |
| `--ascii`  | bool | Force ASCII board print (default if --fen not used).  |
| `--seed S` | int  | Random seed for reproducible random IDs.              |
| `--flip`   | bool | Flip board (Perspective from the Black side).         |

---

## Example Output

### ASCII Board with ID
```text
--- Chess960 Position ID: 214 ---
b n n q r k r b
p p p p p p p p
. . . . . . . .
. . . . . . . .
. . . . . . . .
. . . . . . . .
P P P P P P P P
B N N Q R K R B
ID = 214
```

### FEN String
```text
bnnqrkrb/pppppppp/8/8/8/8/PPPPPPPP/BNNQRKRB w KQkq - 0 1
```

---

## Technical Note
Pawnfuddle ensures the two core rules of Chess960 are always met:
1. **Bishops** must be on opposite-colored squares.
2. The **King** must be placed on a square between the two **Rooks** to allow for legal castling.

## License

This project is licensed under the [MIT License](LICENSE).

