import string
import random

def generate_strong_password(length):
    # Store all characters in lists
    lowercase_letters = list(string.ascii_lowercase)
    uppercase_letters = list(string.ascii_uppercase)
    digits = list(string.digits)
    punctuation = list(string.punctuation)

    # Shuffle all lists
    random.shuffle(lowercase_letters)
    random.shuffle(uppercase_letters)
    random.shuffle(digits)
    random.shuffle(punctuation)

    # Calculate 30% & 20% of the number of characters
    part1 = round(length * (30 / 100))
    part2 = round(length * (20 / 100))

    # Generation of the password (60% letters and 40% digits & punctuations)
    result = []

    for x in range(part1):
        result.append(lowercase_letters[x])
        result.append(uppercase_letters[x])

    for x in range(part2):
        result.append(digits[x])
        result.append(punctuation[x])

    # Shuffle result
    random.shuffle(result)

    # Join result
    password = "".join(result)
    return password

# Ask user about the number of characters
while True:
    try:
        characters_number = int(input("How many characters do you want in your password? "))

        if characters_number < 8:
            print("Your number should be at least 8.")
        else:
            break

    except ValueError:
        print("Please, enter numbers only.")

# Generate and print the password
password = generate_strong_password(characters_number)
print("Strong Password:", password)
