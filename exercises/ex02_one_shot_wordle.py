"""EX02- One Shot Wordle"""
__author__ = "730559522"
secret_word: str = "python"
desired_word_len: int = len(secret_word)
prompt_rand_num_letter_guess: str = input(f"What is your {desired_word_len} letter guess? ")
# Prompt word guess from the user
while (len(prompt_rand_num_letter_guess) != desired_word_len):
    prompt_rand_num_letter_guess: str = input(f"That was not {desired_word_len} letters! Try Again: " )
# Asks user to try again if lengths of user's guess and the secret word don't match.
if(prompt_rand_num_letter_guess == secret_word):
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")
#If user's guess end up being the secret word, print "Woo! You got it!" Otherwise, print "Not quite. Play again soon!"

WHITE_BOX: str =  "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
#Initilization of f-strings with respect to their box colors
word_guess_index: int = 0
guess_emoji: str = ""
while(word_guess_index < desired_word_len):
    if(prompt_rand_num_letter_guess[word_guess_index] == secret_word[word_guess_index]):
        guess_emoji += GREEN_BOX
    else:
        bool_guessed_character: bool = False
        alt_word_guess_index: int = 0
    #if user guess index is the same as the secret word the index, add a green box. Otherwise, declare and initialize boolean variable regarding whether a character is present or not to false and also declare and initialize an alternate word index to 0. 

        while(bool_guessed_character != True and (alt_word_guess_index < desired_word_len)):
            if(secret_word[alt_word_guess_index] == prompt_rand_num_letter_guess[word_guess_index]):
                bool_guessed_character = True
            else:
                alt_word_guess_index += 1
            #if the alternate index of the secret word is the index of the user guess, set boole

        if(bool_guessed_character == True):
            guess_emoji += YELLOW_BOX
        else:
            guess_emoji += WHITE_BOX
    word_guess_index += 1
#Add yellow box if guessed character is present somewhere else in the word. Otherwise add white box. 
print(guess_emoji)
#print the resulting emoji of box colors

    






    
