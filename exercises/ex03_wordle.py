"""EX03 - Wordle - Finally!"""

__author__ = "730489294"


def contains_char(guess_string: str, single_character: str) -> bool:
    """This functions sees if one character is in a string."""
    assert len(single_character) == 1
    i: int = 0
    while i < len(guess_string):
        if guess_string[i] == single_character:
            return True
        i += 1
    return False


def emojified(guess_word: str, secret_word: str) -> str:
    """This function returns an emoji string."""
    assert len(guess_word) == len(secret_word)
    i: int = 0
    emoji: str = ""
    answer: bool = True
    green: str = "\U0001F7E9"
    yellow: str = "\U0001F7E8"
    white: str = "\U00002B1C"
    while i < len(guess_word):
        if guess_word[i] == secret_word[i]:
            emoji = emoji + green
        else: 
            answer = contains_char(secret_word, guess_word[i])
            if answer:
                emoji = emoji + yellow 
            else:
                emoji = emoji + white
        i += 1
    return emoji


def input_guess(expected_len: int) -> str:
    """This function prompts the user to give a guess of a certain len."""
    string_guess: str = input(f"Enter a {expected_len} character word: ")
    while len(string_guess) != expected_len:
        string_guess = input(f"That wasn't {expected_len} chars! Try again:")
    
    return string_guess


def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret_word: str = "codes"
    integer_len: int = len(secret_word)
    guess_word: str = ""
    emoji: str = ""
    i: int = 1
    while i <= 6:
        print(f"=== Turn {i}/6 ===")
        guess_word = input_guess(integer_len)
        emoji = emojified(guess_word, secret_word)
        print(emoji)
        if guess_word == secret_word:
            print(f"You won in {i}/6 turns!")
            i = integer_len + 1
    
        i += 1
    if guess_word != secret_word:
        print("X/6 - Sorry, try again tomorrow.")
    

if __name__ == "__main__":
    main()

    
