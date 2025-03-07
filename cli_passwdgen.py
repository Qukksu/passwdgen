import secrets
import string

class PasswordGenerator:
    def __init__(self):
        self.characters = string.ascii_letters + string.digits + string.punctuation

    def generate_password(self, length: int) -> str:
        """Generate a cryptographically secure password of the given length."""
        return ''.join(secrets.choice(self.characters) for _ in range(length))

    def run(self):
        print("Password Generator (type 'exit' to quit)")

        while True:
            user_input = input("Enter the password length: ").strip()

            if user_input.lower() == 'exit':
                print("Exiting...")
                break

            try:
                length = int(user_input)

                if length <= 0:
                    print("Error: Length must be a positive number!")
                    continue

                print(f"Your password: {self.generate_password(length)}")

            except ValueError:
                print("Error: Please enter an integer or 'exit' to quit!")

if __name__ == "__main__":
    generator = PasswordGenerator()
    generator.run()
