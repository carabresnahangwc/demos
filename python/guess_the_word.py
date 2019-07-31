
# GUESS THE WORD aka HANGMAN

"""
Psuedo-code
1. pick a word from a list to use
2. make a variables rounds, guesses list
3. print the letters, show the letters that are correct and
            use a dash for missing letters
4. tell user when they have guessed the word
5. take guess from user and add to our guesses list
6. check if our guess is in our word
    if guess is in our word add points
    else take points
7. if we run out of guesses, tell the user they lost

#HOW TO PRINT WITHOUT A NEW LINE
 print(letter, end="")

 #TO MAKE A STRING A LIST OF CHARACTERS
 string_as_list = list("word")

 #CHANGE A LETTER (DASH TO LETTER) IN A WORD AT INDEX
 word[index] = letter
"""

'''
Solution 1:
'''

'''
import random

listofwords = ["loops", "variables", "conditional", "iteration", "psuedocode"]

guesses = []
num_wrong = 0
mistakes = 10
word = random.choice(listofwords)
print(word)
while num_wrong < mistakes:

    left = len(word)
    for char in word:
        if char in guesses:
            print(char, end=" ")
            left -=1
        else:
            print("_", end=" ")

    if left == 0:
        print("\nYOU WON!")
        break

    print("\nGuesses: ", end=" ")
    for char in guesses:
        if char not in word:
            print(char, end=" ")

    letter = input("\nGuess a letter: ")
    guesses += letter

    if letter not in word:
        num_wrong += 1
        print("That letter is not in the word, you have ",mistakes-num_wrong, " guesses left." )
'''
'''
Solution 2: Using the Starter Code
            Only works with words with single occurence letters
'''
import random

# A list of words
potential_words = ["example", "words", "someone", "can", "guess"]
word = random.choice(potential_words)

# Use to test your code:
# print(word)

# Converts the word to lowercase
word = word.lower()
mystery = list(word)

# Make it a list of letters for someone to guess
current_word = []
for x in range(len(mystery)):# TIP: the number of letters should match the word
    current_word.append('_')

# Some useful variables
guesses = []
maxfails = 7
fails = 0

while fails < maxfails:
    print(current_word)

    if '_' not in current_word:
        print("You Guessed the word!")
        break

    print("Guesses: ", guesses)

    guess = input("Guess a letter: ")

	# check if the guess is correct: Is it in the word? If so, reveal the letters!
    if guess in mystery:
        index = mystery.index(guess)
        current_word[index] = guess
    elif guess in guesses:
        print("You have already guessed that letter!")
    else:
        fails += 1
        guesses.append(guess)
        print("You have " + str(maxfails - fails) + " tries left!")

if fails == maxfails:
    print("You have failed to guess the word :(")
