"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730489294"

word: str = input("Enter a 5-character word:")
if len(word) != 5:
    print("Error: Word must contain 5 characters")
    exit()

guess_letter: str = input("Enter a single character:")
if len(guess_letter) != 1:
    print("Error: Character must be a single character.")
    exit()

print("Searching for " + guess_letter + " in " + word)

instances: int = 0

if guess_letter == word[0]:
    print(guess_letter + " found at index 0 ")
    instances += 1
if guess_letter == word[1]:
    print(guess_letter + " found at index 1 ")
    instances += 1
if guess_letter == word[2]:
    print(guess_letter + " found at index 2 ")
    instances += 1
if guess_letter == word[3]:
    print(guess_letter + " found at index 3 ")
    instances += 1
if guess_letter == word[4]:
    print(guess_letter + " found at index 4 ")
    instances += 1

if instances == 0:
    print("No instances of " + guess_letter + " found in " + word)
elif instances == 1:
    print("1 instance of " + guess_letter + " found in " + word)
elif instances > 1:
    print(str(instances) + " instances of " + guess_letter + " found in " + word)
