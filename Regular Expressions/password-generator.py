# place import statements at the top of your code
# sort them in alphabetic order to improve readability
import re
import secrets
import string


def generate_password(length=16, nums=1, special_chars=1, uppercase=1, lowercase=1):
    # Define the possible characters for the password
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    # Combine all characters
    all_characters = letters + digits + symbols
    while True:
        password = ''
        # Generate password
        for _ in range(length):  # _ representing a value you don't care or that won't be used in your code
            password += secrets.choice(all_characters)
        constraints = [
            (nums, r'\d'),  # r'[0-9]'
            (special_chars, fr'[{symbols}]'),  # r'[^a-zA-Z0-9_]' -> r'\W'
            (uppercase, r'[A-Z]'),
            (lowercase, r'[a-z]')
        ]
        # Check constraints
        # count = 0
        # for constraint, pattern in constraints:
        #     if constraint <= len(re.findall(pattern, password)):
        #         count += 1
        #
        # if count == 4:
        if all(
            constraint <= len(re.findall(pattern, password))
            for constraint, pattern in constraints
        ):
            break

    return password


if __name__ == '__main__':
    new_password = generate_password()
    print('Generated password:', new_password)

