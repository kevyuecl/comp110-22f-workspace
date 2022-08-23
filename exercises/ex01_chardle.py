"""EX01 - Chardle - A cute step toward Wordle."""
__author__ = "730559522"
word_five_letter: str = input("Enter a 5-character word: ")

if(len(word_five_letter) != 5):
    print("Error: Word must contain 5 characters")
    exit()
word_character: str = input("Enter a single character: ")
if(len(word_character) != 1):
    print("Error: Character must be a single character.")
    exit()
num_character_matches_in_word: int= 0
print("Searching for " + word_character + " in " + word_five_letter)

if(word_character == word_five_letter[0]):
    print(word_character + " found at index 0")
    num_character_matches_in_word = num_character_matches_in_word + 1
    
if(word_character == word_five_letter[1]): 
    print(word_character + " found at index 1")
    num_character_matches_in_word = num_character_matches_in_word + 1
    
if(word_character == word_five_letter[2]): 
    print(word_character + " found at index 2")
    num_character_matches_in_word = num_character_matches_in_word + 1
    
if(word_character == word_five_letter[3]): 
    print(word_character + " found at index 3")
    num_character_matches_in_word = num_character_matches_in_word + 1
    
if(word_character == word_five_letter[4]): 
    print(word_character + " found at index 4")
    num_character_matches_in_word = num_character_matches_in_word + 1
   
if(num_character_matches_in_word == 0):
    print("No instances of " + word_character + " found in " + word_five_letter)

else:
    if(num_character_matches_in_word == 1):
        print(str(num_character_matches_in_word) + " instance of " + word_character + " found in " + word_five_letter)
    else:
        print(str(num_character_matches_in_word) + " instances of " + word_character + " found in " + word_five_letter)
