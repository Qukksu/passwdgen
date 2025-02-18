"""Copyright (C) <2025> <Evrotskii Artem>
This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or (at your option)
any later version.
"""

import math
import string
from typing import Set

class PasswordEntropyChecker:
    def __init__(self):
        self.char_sets = {
            'lowercase': set(string.ascii_lowercase),
            'uppercase': set(string.ascii_uppercase),
            'digits': set(string.digits),
            'special': set(string.punctuation)
        }

    def get_charset_size(self, password: str) -> int:
        used_chars: Set[str] = set(password)
        charset_size = 0

        if any(c in self.char_sets['lowercase'] for c in used_chars):
            charset_size += len(self.char_sets['lowercase'])
        if any(c in self.char_sets['uppercase'] for c in used_chars):
            charset_size += len(self.char_sets['uppercase'])
        if any(c in self.char_sets['digits'] for c in used_chars):
            charset_size += len(self.char_sets['digits'])
        if any(c in self.char_sets['special'] for c in used_chars):
            charset_size += len(self.char_sets['special'])

        return charset_size

    def calculate_entropy(self, password: str) -> float:
        if not password:
            return 0.0

        charset_size = self.get_charset_size(password)
        password_length = len(password)

        entropy = password_length * math.log2(charset_size) if charset_size > 0 else 0
        return round(entropy, 2)

    def get_strength_level(self, entropy: float) -> str:
        if entropy < 28:
            return "Very Weak"
        elif entropy < 36:
            return "Weak"
        elif entropy < 60:
            return "Reasonable"
        elif entropy < 128:
            return "Strong"
        else:
            return "Very Strong"

def main():
    checker = PasswordEntropyChecker()

    while True:
        password = input("Enter password to check (or 'q' to quit): ")
        if password.lower() == 'q':
            break

        entropy = checker.calculate_entropy(password)
        strength = checker.get_strength_level(entropy)

        print(f"\nPassword: {password}")
        print(f"Entropy: {entropy} bits")
        print(f"Strength: {strength}")
        print("-" * 40)

if __name__ == "__main__":
    main()