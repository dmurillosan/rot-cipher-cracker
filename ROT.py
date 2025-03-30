import argparse
import string
from nltk.corpus import words
import nltk

# Load word list
try:
    english_words = set(words.words())
except LookupError:
    nltk.download('words')
    english_words = set(words.words())

def rot_n(text, shift):
    """Applies ROT-N cipher to the text."""
    result = []
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            rotated = chr((ord(char) - base + shift) % 26 + base)
            result.append(rotated)
        else:
            result.append(char)
    return ''.join(result)

def is_printable(text, threshold=0.9):
    """Checks if most characters in the text are printable (like `strings`)."""
    if not text:
        return False
    printable_chars = sum(c in string.printable for c in text)
    return (printable_chars / len(text)) >= threshold

def has_5_consecutive_words(text):
    """Checks if there are at least 5 consecutive English words."""
    word_list = text.split()
    count = 0
    for word in word_list:
        cleaned = ''.join(filter(str.isalpha, word)).lower()
        if cleaned in english_words:
            count += 1
            if count >= 5:
                return True
        else:
            count = 0
    return False

def find_rot_and_output(input_file, output_file=None):
    """Tries all ROT ciphers and either prints or writes the result."""
    try:
        with open(input_file, 'r', encoding='utf-8', errors='ignore') as file:
            original = file.read()
    except FileNotFoundError:
        print(f"[Error] File not found: {input_file}")
        return

    for shift in range(1, 26):  # ROT1 to ROT25
        decoded = rot_n(original, shift)
        if is_printable(decoded) and has_5_consecutive_words(decoded):
            output = f"\nROT Cipher Found: ROT{shift}\n" + ("=" * 60) + f"\n{decoded}\n" + ("=" * 60) + "\n"
            if output_file:
                with open(output_file, 'w', encoding='utf-8') as f:
                    f.write(output)
                print(f"[Info] ROT{shift} output saved to '{output_file}'")
            else:
                print(output)
            return

    print("[Info] No readable ROT cipher output found.")

# Entry point
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="ROT cipher cracker with readability detection.")
    parser.add_argument("input_file", help="The file to scan for ROT cipher text")
    parser.add_argument("-o", "--output", help="Optional output file to save the decrypted result")
    args = parser.parse_args()

    find_rot_and_output(args.input_file, args.output)
