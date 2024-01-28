"""Creating a one short wordle."""

__author__ = "730612873"

secret_word: str = "python"
word_count: int = len(secret_word)
guess: str = input(f"What is your { word_count }-letter guess? ")
guess_index: int = 0
emoji: str = ""
exists_in_word: bool = False

while len(guess) != word_count:
    guess = input("That was not 6 letters! Try again: ")

if guess == secret_word:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

while guess_index < word_count:
    if guess[guess_index] == secret_word[guess_index]:
        emoji = str(emoji) + str(GREEN_BOX)
        guess_index = guess_index + 1
    else: 
        alternate_index: int = 0
        exists_in_word = False
        while exists_in_word != True and alternate_index < word_count:
            if guess[guess_index] == secret_word[alternate_index]:
                exists_in_word = True
            else: 
                alternate_index = alternate_index + 1

        if exists_in_word == True:
            emoji = str(emoji) + str(YELLOW_BOX)
        else: 
            emoji = str(emoji) + str(WHITE_BOX)   
        
        guess_index = guess_index + 1

print(emoji)