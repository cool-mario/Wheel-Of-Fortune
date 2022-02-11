###################################################
# Filename: wheel of fortune.py
# Author:   Aidan C
# Date:     Feb, 2022
#
# Do not use repl.it - use your own laptop/computer
# or use the Mu Editor

###################################################
# Imports
from tkinter import *
import random
###################################################


# Global Variables

screen_width      = 800        # The window height and width in pixels
screen_height     = 600
chosenWordDisplay = ""        # A Label
amounts = [500, 750, 1000, 1250, 1500, 1750, 5000]
total = 0

# List of letters to remove after each guess
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W','X', 'Y', 'Z']
# Categories and chosenWords
categories = {'color': ['red', 'green' ,'blue','yellow','turqouise','purple','indigo','white','black'], 'phrase':["it's raining cats and dogs", "speak of the devil", "the best of both worlds", "see eye to eye","when pigs fly", "costs an arm and a leg","once in a blue moon", "a piece of cake", "let the cat out of the bag", "feeling under the weather", "kill two birds with one stone"]}

vowels = ["A", "E", "I", "O", "U"]

# Pick a random category
randChosenCategory = random.randint(0, (len(categories) - 1)) # color or phrase

# Print randChosenCategory name
print("Category:", list(categories.keys())[randChosenCategory])

# Get a random chosenWord or phrase from the category
chosenWord = (
    categories[list(categories.keys())[randChosenCategory]][
        random.randint(0, (len(list(categories[list(categories.keys())[randChosenCategory]])) - 1))
    ]
).upper()



###################################################


# Functions

# Function to print Word
def printWord(chosenWord):
    thing = ""
    for char in chosenWord:
        thing += char + " "
    wordDisplay['text'] = thing


# We use this to capture the key's pressed
def key_pressed(event):
    global wordDisplay

    print("Key Pressed: " + event.char)

    x = ord(event.char)
    print("Key Value:   " + str(x))

    str1 = "You pressed " + event.char
    wordDisplay['text'] = str1

def theGame():
    # Keep guessing until word is guessed correctly
    while True:
        while True:
            # Pick an random amount from amounts
            amount = amounts[random.randint(0, (len(amounts) - 1))]
            print("$" + str(amount), "per correct letter")
            print("$500 per vowel")
            guess = input().upper()
            # If the user wants to guess phrase or word
            if guess == "GUESS":
                while True:
                    correct = 0
                    guess = input().upper()
                    for letter in range(len(guess)):
                        if guess[letter] == word[letter]:
                            correct += 1
                        else:
                            break
                    if correct == len(guess):
                        for letter in range(len(guess)):
                            if guess[letter] == word[letter]:
                                if not Word[letter].isalpha():
                                    Word[letter] = guess[letter]
                                    if (
                                        guess[letter] not in vowels
                                        and guess[letter].isalpha()
                                    ):
                                        total += amount
                    else:
                        print("Sorry, that's not the answer! Keep guessing!")
                        printWord(Word)
                        break
                    if "_" not in Word:
                        printWord(Word)
                        print("You have: $" + str(total))
                        break
                    else:
                        for char in range(len(Word)):
                            if word[char] == guess:
                                Word[char] = guess
                    print("$" + str(total))
                    printWord(Word)
                    if "_" not in Word:
                        break
                break
            # If user guesses letter they've already guessed
            elif guess not in alphabet:
                print("You've already picked that letter!")
                print("You have: $" + str(total))
            # If guess is a vowel, subtract $500 from total per vowel
            elif guess in vowels:
                if total >= 500:
                    alphabet.remove(guess)
                    for char in range(len(Word)):
                        if word[char] == guess:
                            total -= 500
                            Word[char] = guess
                # If user cannot buy vowel
                else:
                    print("Not enough money")
                print("You have: $" + str(total))
                printWord(Word)
                if "_" not in Word:
                    break
            # If everythin else is False, remove letter from alphabet and replace char in Word with letter in word
            else:
                alphabet.remove(guess)
                for char in range(len(Word)):
                    if word[char] == guess:
                        Word[char] = guess
                        total += amount
                print("You have: $" + str(total))
                printWord(Word)
                if "_" not in Word:
                    break
        # If word or phrase is fully guessed, end game
        if "_" not in Word:
            print("You won!")
            break

###################################################

# The first function called to set up the the screen
def init():
    print("Starting ...")
    global screen_width, screen_height, wordDisplay, testButton, entry, submitButton

    x = threading.Thread(target=theGame, daemon=True)  # what deamon?
    x.start()

    # This is for screen frame
    root = Tk()
    root.geometry(str(screen_width) + "x" + str(screen_height))
    root.title("Wheel of Fortune!!!")
    root.configure(background='black')

    # This is a label
    wordDisplay = Label(root, text="This is a test label", height=3, width=20)
    wordDisplay.configure(background='blue')
    wordDisplay.configure(font=("Arial", 50))
    wordDisplay.configure(foreground='white')
    wordDisplay.place(relx=0.3, rely=0.05, anchor=NW)

    infoDisplay = Label(root, text="Info", height=3, width=20)
    wordDisplay.configure(background='blue')
    wordDisplay.configure(font=("Arial", 50))
    wordDisplay.configure(foreground='white')
    wordDisplay.place(relx=0.3, rely=0.35, anchor=NW)

    # Capture keystrokes here
    root.bind("<Key>", key_pressed)

    dashes = []  # dashes get revealed
    for char in chosenWord:
        if char.isalpha():    # checks if the character is a letter
            dashes.append("_")
        else:
            dashes.append(char)  # if not a letter print it out like a ' or "

    printWord(dashes)



    # This runs forever, waiting for mouse clicks
    root.mainloop()


###################################################
# Start here

init()
