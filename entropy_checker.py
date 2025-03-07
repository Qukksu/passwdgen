import math
import string
from typing import Set

# Class for calculating and evaluating password entropy and strength
class PasswordEntropyChecker:
    def __init__(self):
        # Dictionary of character sets used for entropy calculation
        self.char_sets = {
            'lowercase': set(string.ascii_lowercase),  # a-z
            'uppercase': set(string.ascii_uppercase),  # A-Z
            'digits': set(string.digits),             # 0-9
            'special': set(string.punctuation)        # Special characters
        }

    def get_charset_size(self, password: str) -> int:
        # Calculate total size of character sets used in password
        used_chars: Set[str] = set(password)
        charset_size = 0

        # Add length of each character set if used in password
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
        # Calculate password entropy using formula: length * log2(charset_size)
        if not password:
            return 0.0

        charset_size = self.get_charset_size(password)
        password_length = len(password)

        entropy = password_length * math.log2(charset_size) if charset_size > 0 else 0
        return round(entropy, 2)

    def get_strength_level(self, entropy: float) -> str:
        # Determine password strength based on entropy value
        # < 28 bits: Very Weak
        # 28-35 bits: Weak
        # 36-59 bits: Reasonable
        # 60-127 bits: Strong
        # >= 128 bits: Very Strong
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

# Main function for command-line interface
def main():
    checker = PasswordEntropyChecker()

    # Interactive loop for password checking
    while True:
        password = input("Enter password to check (or 'q' to quit): ")
        if password.lower() == 'q':
            break

        # Calculate and display password metrics
        entropy = checker.calculate_entropy(password)
        strength = checker.get_strength_level(entropy)

        print(f"\nPassword: {password}")
        print(f"Entropy: {entropy} bits")
        print(f"Strength: {strength}")
        print("-" * 40)

if __name__ == "__main__":
    main()
