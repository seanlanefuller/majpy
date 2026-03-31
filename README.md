# Major System Memory Trainer (majpy)

A simple Python GUI application to help you learn and practice the **Major System** mnemonic technique.

The Major System is a mnemonic technique used to aid in memorizing numbers by converting them into consonant sounds, which can then be combined with vowels to form words.

## Features

- **Learn Mode**: Explore the phonetic mappings for any number.
- **Flashcard Mode**: Test your memory by recalling words for randomly selected numbers.
- **Custom Word List**: Load your own mappings from `majwords.txt`.
- **GUI Interface**: Easy-to-use interface built with `tkinter`.

## Mnemonic Mapping

The application uses the standard Major System mapping:

- **0**: S, Z
- **1**: T, D
- **2**: N
- **3**: M
- **4**: R
- **5**: L
- **6**: J, SH, CH, soft G
- **7**: K, hard C, hard G
- **8**: F, V
- **9**: P, B

## Installation

### Prerequisites

- Python 3.x
- `tkinter` (usually included with Python on Windows and macOS; may need `sudo apt install python3-tk` on Linux)

### Setup

1.  Clone the repository or download the source files.
2.  Ensure `majpy.py` and `majwords.txt` are in the same directory.

## Usage

Run the application using Python:

```bash
python majpy.py
```

### Word List Format

The `majwords.txt` file should contain one mapping per line:

```text
00 sauce
01 seed
...
```

Lines starting with `#` or empty lines are ignored.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
