"""EX03- Sturcutred Wordle."""
__author__ = "730559522"
def contains_char (secret_word: str, secret_chr: str) -> bool:
    """Searches for present characters for strings of any length"""
    assert len(secret_chr) == 1
    index: int = 0  # Initialize index to 0
    while (index < len(secret_word)):
        if (secret_word[index] == secret_chr):
            return True
        else:
            index += 1
    return False
    # While index is less than the length of the word, return true if the character is found at the index of the word and return false otherwise

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
# Initialization of f-strings with respect to their box colors 
def emojified (guess_secret: str, secret: str) -> str:
    """Returns emoji strings based on guess accuracy"""
    assert len(guess_secret) == len(secret)
    index: int = 0  # Initialize index to 0 
    emoji_result = ""
    while (index < len(secret)):
        if (guess_secret[index] == secret[index]):
            emoji_result += GREEN_BOX  # When the characters at the same index match
            index += 1
        elif contains_char (secret, guess_secret[index]):
            emoji_result += YELLOW_BOX  # When the character of secret guess appears in secret word
            index += 1
        else:
            emoji_result += WHITE_BOX  # When the character does not appear in the word
            index += 1
    return emoji_result  # Return string of color emojis
def input_guess (expected_length: int) -> str: 
    """Returns string of expected length from the user"""
    prompt_word_guess = input(f"Enter a {expected_length} character word: ")
    while (len(prompt_word_guess) != expected_length):
        prompt_word_guess = input(f"That wasn't {expected_length} chars! Try again: ")  #Prompts user for a guess
    return prompt_word_guess  # String of expected length returns

def main() -> None:
    """The entrypoint of the program and main game loop."""
    turn: int = 1  # Turn is initilized to 1
    secret_word: str = "codes"  # The secret word being guessed
    user_guess: str = ""  # Empty user guess string initialized
    win: bool = False  # If user guesses secret word right, this will become true. 
    while (turn < 7 and not win):
        print(f"=== Turn {turn}/6 ===")
        user_guess = input_guess(len(secret_word))  # User guess input assigned to guess
        print(emojified(user_guess, secret_word))  # Color emojis printed
        turn += 1 # Turn increments by 1

        if (secret_word == user_guess):
            win = True  # User win scenario
            print(f"You won in {turn-1}/6 turns!")
    if not win:
        print("X/6 - Sorry, try again tomorrow!")  # User loss scenario

if __name__== "__main__":
    main()


        



    






