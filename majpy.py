import os
import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog  # ← add this line
import random

MAJOR_MAP = {
    '0': 'S Z',
    '1': 'T D',
    '2': 'N',
    '3': 'M',
    '4': 'R',
    '5': 'L',
    '6': 'J SH CH soft G',
    '7': 'K hard C hard G',
    '8': 'F V',
    '9': 'P B'
}

def load_words_from_file(filename=None):
    """Load two-digit -> word mapping from a text file.

    File format (one mapping per line):
      00 sauce
      01 seed
    Lines starting with # or empty lines are ignored. First token is the
    two-digit number (keeps leading zeros). The rest of the line is the word.
    Returns a dict mapping '00'..'99' -> list of words.
    """
    if filename is None:
        # file next to this script
        filename = os.path.join(os.path.dirname(__file__), 'majwords.txt')

    words = {}
    try:
        with open(filename, encoding='utf-8') as f:
            for raw in f:
                line = raw.strip()
                if not line or line.startswith('#'):
                    continue
                parts = line.split(None, 1)
                if not parts:
                    continue
                key = parts[0].zfill(2)
                if not key.isdigit():
                    continue
                value = parts[1].strip() if len(parts) > 1 else ''
                if not value:
                    continue
                words.setdefault(key, []).append(value)
    except FileNotFoundError:
        # Fall back to a small built-in set if the file isn't present
        words = {
            '32': ['moon', 'man', 'main'],
            '45': ['rail', 'roll'],
            '17': ['duck', 'deck'],
            '86': ['fish', 'fudge'],
            '09': ['soap', 'zebra']
        }
    return words


# Load WORDS from majwords.txt (or fallback)
WORDS = load_words_from_file()

def number_to_pattern(num):
    """Return the phonetic code pattern for the given number."""
    return ' - '.join(f"{d}: {MAJOR_MAP.get(d, '?')}" for d in num if d.isdigit())

def check_word_for_number(word, num):
    """Roughly check if word corresponds to number pattern (simplified)."""
    consonant_map = {
        's': '0', 'z': '0',
        't': '1', 'd': '1',
        'n': '2',
        'm': '3',
        'r': '4',
        'l': '5',
        'j': '6', 'g': '6', 'c': '6', 'h': '6',
        'k': '7',
        'f': '8', 'v': '8',
        'p': '9', 'b': '9'
    }
    code = ''.join(consonant_map.get(c.lower(), '') for c in word if c.lower() in consonant_map)
    return code.startswith(num)

class MajorSystemApp:
    def __init__(self, root):
        self.root = root
        root.title("Major System Memory Trainer")

        self.mode = tk.StringVar(value='learn')

        tk.Label(root, text="Major System Trainer", font=("Helvetica", 16, "bold")).pack(pady=10)
        
        # Mode selector
        tk.Radiobutton(root, text="Learn", variable=self.mode, value='learn').pack()
        tk.Radiobutton(root, text="Flashcards", variable=self.mode, value='flash').pack()

        self.num_entry = tk.Entry(root, font=("Helvetica", 14))
        self.num_entry.pack(pady=10)
        self.num_entry.insert(0, "Enter number")

        tk.Button(root, text="Show Mapping", command=self.show_mapping).pack(pady=5)
        tk.Button(root, text="Practice Word", command=self.practice_word).pack(pady=5)

        self.output = tk.Label(root, text="", font=("Helvetica", 12), wraplength=300)
        self.output.pack(pady=10)

    def show_mapping(self):
        num = self.num_entry.get()
        mapping = number_to_pattern(num)
        self.output.config(text=f"{num} → {mapping}")

    def practice_word(self):
        if self.mode.get() == 'learn':
            word = simpledialog.askstring("Word Check", "Enter a word to test:")
            num = self.num_entry.get()
            if not num.isdigit():
                messagebox.showerror("Error", "Enter a valid number first!")
                return
            result = check_word_for_number(word, num)
            messagebox.showinfo("Result", f"Word '{word}' {'matches' if result else 'does not match'} number {num}.")
        else:
            # Flashcard mode
            # Present a random number and expect a matching word from the user.
            # Choose only keys that have at least one word.
            valid_items = [(k, v) for k, v in WORDS.items() if v]
            if not valid_items:
                messagebox.showerror("No words", "No flashcard words found.")
                return
            num, words = random.choice(valid_items)
            guess = simpledialog.askstring("Flashcard", f"What word can you recall for {num}?")
            if not guess:
                return
            if guess.strip().lower() in [w.lower() for w in words]:
                messagebox.showinfo("Correct!", f"Yes! '{guess}' is one of {words}.")
            else:
                messagebox.showinfo("Try again", f"Possible answers: {', '.join(words)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = MajorSystemApp(root)
    root.mainloop()
