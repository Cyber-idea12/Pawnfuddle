# Pawnfuddle

**Pawnfuddle – Chess960 Random Position Generator (CLI)**

Pawnfuddle generates valid Chess960 (Fischer Random) starting positions, prints them in ASCII or FEN format, and allows for easy integration with engines or online play. Lightweight, terminal-based, no GUI required.

---

## Features

- Generates **valid Chess960 starting positions**.
- Outputs **ASCII board** in terminal.
- Outputs **FEN strings** for use in chess engines or online platforms.
- CLI flags for customization: number of positions, seed, board flip.
- Lightweight Python script, runs anywhere with Python 3.

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/pawnfuddle.git
cd pawnfuddle

Ensure Python 3 is installed.

Run directly:

```bash
python chess960.py [flags]

No additional dependencies are requir

---

## Usage

### Generate a single random Chess960 position (ASCII by default)

```bash
python chess960.py

### Generate multiple positions

```bash
python chess960.py --count 5

### Print FEN only

```bash
python chess960.py --fen

### Use a seed for reproducible positions

```bash
python chess960.py --seed 42 --count 3

### Flip the board upside-down

```bash
python chess960.py --flip

### Combine flags

```bash
python chess960.py --count 3 --fen --seed 123 --flip

---

## CLI Flags Summary

| Flag       | Type | Description                                  |
|-----------|------|----------------------------------------------|
| --count N | int  | Number of positions to generate (default=1) |
| --fen     | bool | Print FEN only, skip ASCII board            |
| --ascii   | bool | Force ASCII board print (default if --fen not used) |
| --seed S  | int  | Random seed for reproducible positions      |
| --flip    | bool | Flip board (black on bottom)                |

---

## Example Output

### ASCII Board
r n b q k b n r
p p p p p p p p
. . . . . . . .
. . . . . . . .
. . . . . . . .
. . . . . . . .
P P P P P P P P
R N B Q K B N R

### FEN
rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1


---

## Notes

- Terminal-based, works on any system with Python 3 installed.
- Designed for simplicity and easy integration with engines or online play.

## License

This project is licensed under the MIT License.
