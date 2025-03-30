# ROT Cipher Cracker

A command-line Python tool that detects and decrypts ROT1 through ROT25-encrypted text. It identifies the correct cipher by checking for human-readable output using ASCII printability and a dictionary-based check for five consecutive English words (via the NLTK corpus).

---

## Features

- Scans for all ROT1–25 ciphers
- Detects English-language output using NLTK's `words` corpus
- Optional file output with `-o` flag
- Clean terminal output (no emojis or clutter)
- Can be compiled into a `.exe` with a custom icon for Windows

---

## How It Works

1. Applies ROT1 through ROT25 to the input text.
2. Filters output based on:
   - 90%+ printable ASCII characters (similar to `strings`)
   - At least five consecutive real English words
3. Outputs the correctly decrypted message.

---


# Usage

	python ROT.py encoded.txt


## Build as Executable (.exe)

To build a standalone Windows executable:

	pip install pyinstaller Pillow

	pyinstaller --onefile --icon=ROT.ico ROT.py