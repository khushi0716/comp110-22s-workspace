"""EX02 - One-Shot Wordle - Loops!"""

__author__ = "730489294"

# Initilizing the guess_word and secret_word 
secret_word: str = "python"
guess_word: str = input("What is your " + str(len(secret_word)) + " letter guess? ")

# While loop checks length of guess and prompts the user to try again if the guess doesn't have a length of 6
while len(guess_word) != len(secret_word):
    guess_word = input("That was not " + str(len(secret_word)) + " letters! Try again: ")

# Initilizing the index counter and emoji string
# The while loop has an in-else that goes through each letter in guess_word to see if it is equal to the letter at the same index of secret_word and concatinates the correct emoji
# If they are not the same letter, then the if-else checks to see if the letter is in the secret word at all and concatinates the correct emoji
# Lastly the if-else checks to see the letter of the guess_word matches any letter in the secret word and concatinates the correct emoji
i: int = 0
emoji: str = " "
while i < len(secret_word):
    if guess_word[i] == secret_word[i]:
        emoji = emoji + "\U0001F7E9"
    elif guess_word[i] not in secret_word:
        emoji = emoji + "\U00002B1C"
    else: 
        letter_in_guess: bool = False
        j: int = 0
        while letter_in_guess and (j < len(secret_word)):
            if secret_word[j] == guess_word[i]:
                letter_in_guess = True
            else:
                j += 1
        emoji = emoji + "\U0001F7E8"
    
    i += 1

# This prints out the emoji
print(emoji)

# This checks to see which emojis are present in the variable emoji and prints the correct statement
if "\U00002B1C" in emoji:
    print("Not quite. Play again soon!")
elif "\U0001F7E8" in emoji:
    print("Not quite. Play again soon!")
else:
    print("Woo! You got it!")