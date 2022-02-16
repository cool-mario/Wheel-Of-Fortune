# Write your code here :-)
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
import random, threading, math
###################################################


# Global Variables

screen_width      = 800        # The window height and width in pixels
screen_height     = 600
amounts = [500, 750, 1000, 1250, 1500, 1750, 5000]
total = 0   # total $$$$

wordDisplay = ""  # displays the dashes
infoDisplay = ""  # the label that shows the information like how much each letter costs
moreInfoDisplay = ""  # MORE INFO!!!!!
moneyDisplay = ""  # shows how much money you have, or the score

letterGuessEntry = ""  # entry box to guess letters
submitButton = ""     # button to submit your guess
buttonPressed = False

guess = ""   # this will be what the user guessed

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

print(chosenWord)


###################################################


# Functions

# Function to print Word
def printWord(chosenWord):
    thing = ""
    for char in chosenWord:
        thing += char + " "
    wordDisplay['text'] = thing
    #wordDisplay.configure(width=int(math.sqrt(len(thing)))*2)
    fontSize = (int(1002/(math.fabs(len(thing)))))
    print(fontSize)
    if fontSize > 50:
        fontSize = 50
    if fontSize < 30:
        fontSize = 30
    wordDisplay.configure(width=len(thing), font=("Courier new bold", fontSize))


# We use this to capture the key's pressed
def key_pressed(event):
    global wordDisplay, infoDisplay, root

    print("Key Pressed: " + event.char)
    try:
        x = ord(event.char)
        print("Key Value:   " + str(x))
    except:
        print("strange character pressed")

    str1 = "You pressed " + event.char
    #wordDisplay['text'] = str1

def displayInfo(textInfo):
    global infoDisplay, root
    infoDisplay['text'] = textInfo
    
def displayMoreInfo(textInfo):
    global moreInfoDisplay
    if "won" in textInfo:
        moreInfoDisplay.configure(font=("Arial", 50))
    moreInfoDisplay['text'] = textInfo
    
    
def displayMoney(textInfo):
    global moneyDisplay
    moneyDisplay['text'] = textInfo

def submitButtonClick():
    global buttonPressed
    buttonPressed = True
    print("guess submitted")
    
    
    

def theGame():
    global total, guess, alphabet, buttonPressed, moneyDisplay, moreInfoDisplay
    # Keep guessing until word is guessed correctlyh434gtr43fr4t5styht34ahystr4a5s
    while True:
        while True:
            # Pick an random amount from amounts
            amount = amounts[random.randint(0, (len(amounts) - 1))]
            displayInfo("$" + str(amount) + " per correct letter\n$500 per vowel")
            letterGuessEntry.delete(0,END)
            guess = ""
            print(guess)
            while len(guess) == 0 or (not buttonPressed):
                guess = letterGuessEntry.get().upper()
                #print(len(guess))
                #print(buttonPressed)
            
            
            buttonPressed = False
            # If the user wants to guess phrase or word
            if guess == "GUESS":
                while True:
                    correct = 0
                    guess = input().upper()
                    for letter in range(len(guess)):
                        if guess[letter] == chosenWord[letter]:
                            correct += 1
                        else:
                            break
                    if correct == len(guess):
                        for letter in range(len(guess)):
                            if guess[letter] == chosenWord[letter]:
                                if not dashes[letter].isalpha():
                                    dashes[letter] = guess[letter]
                                    if (
                                        guess[letter] not in vowels
                                        and guess[letter].isalpha()
                                    ):
                                        total += amount
                    else:
                        print("Sorry, that's not the answer! Keep guessing!")
                        printWord(dashes)
                        break
                    if "_" not in dashes:
                        printWord(dashes)
                        displayMoney("You have: $" + str(total))
                        break
                    else:
                        for char in range(len(dashes)):
                            if chosenWord[char] == guess:
                                dashes[char] = guess
                    print("$" + str(total))
                    printWord(dashes)
                    if "_" not in dashes:
                        break
                break
            # If user guesses letter they've already guessed
            elif guess not in alphabet:
                displayMoreInfo("You've already \npicked that letter!")
                print("You have: $" + str(total))
            # If guess is a vowel, subtract $500 from total per vowel
            elif guess in vowels:
                if total >= 500:
                    alphabet.remove(guess)
                    for char in range(len(dashes)):
                        if chosenWord[char] == guess:
                            total -= 500
                            dashes[char] = guess
                # If user cannot buy vowel
                else:
                    displayMoreInfo("Not enough money")
                displayMoney("You have: $" + str(total))
                printWord(dashes)
                if "_" not in dashes:
                    break
            # If everythin else is False, remove letter from alphabet and replace char in Word with letter in word
            else:
                alphabet.remove(guess)
                for char in range(len(dashes)):
                    if chosenWord[char] == guess:
                        dashes[char] = guess
                        total += amount
                displayMoney("You have: $" + str(total))
                printWord(dashes)
                if "_" not in dashes:
                    break
        # If word or phrase is fully guessed, end game
        if "_" not in dashes:
            displayMoreInfo("You won!")
            break

###################################################

# The first function called to set up the the screen
def init():
    print("Starting ...")
    global root
    global screen_width, screen_height
    global infoDisplay, wordDisplay, letterGuessEntry, submitButton, moneyDisplay, moreInfoDisplay
    global dashes, total

    # This is a label
    wordDisplay = Label(root, text="Loading...", height=2, width=30)
    wordDisplay.configure(background='darkblue')
    wordDisplay.configure(font=("Courier New bold", 50))
    wordDisplay.configure(foreground='white')
    wordDisplay.place(relx=0.1, rely=0.05, anchor=NW)
    
    # somehow thre infoDisplay is not becoming global
    infoDisplay = Label(root, text="Loading...", height=2, width=25)
    infoDisplay.configure(background='purple')
    infoDisplay.configure(font=("Arial", 40))
    infoDisplay.configure(foreground='white')
    infoDisplay.place(relx=0.1, rely=0.35, anchor=NW)
    
    moneyDisplay = Label(root, text="you have: $0", height=1, width=20)
    moneyDisplay.configure(background='orange')
    moneyDisplay.configure(font=("Arial", 40))
    moneyDisplay.configure(foreground='white')
    moneyDisplay.place(relx=0.1, rely=0.55, anchor=NW)
    
    moreInfoDisplay = Label(root, text="", height=1, width=15)
    moreInfoDisplay.configure(background='crimson')
    moreInfoDisplay.configure(font=("Arial", 20))
    moreInfoDisplay.configure(foreground='white')
    moreInfoDisplay.place(relx=0.5, rely=0.7, anchor=NW)

    letterGuessEntry = Entry(root, font = "Helvetica 60")
    letterGuessEntry.place(relx=0.10, rely=0.7, height=100, width=70, anchor=NW)
    
    submitButton = Button(root, text="Submit guess", font="arial 20", height=3, width=10, command=submitButtonClick)
    submitButton.place(relx=0.25, rely=0.70, anchor=NW)

    # Capture keystrokes here
    root.bind("<Key>", key_pressed)

    dashes = []  # dashes get revealed
    for char in chosenWord:
        if char.isalpha():    # checks if the character is a letter
            dashes.append("_")
        else:
            dashes.append(char)  # if not a letter print it out like a ' or "

    printWord(dashes)
    
    x = threading.Thread(target=theGame, daemon=True)  # what deamon?
    x.start()  # start the thread to the main game
    
    # This runs forever, waiting for mouse clicks
    root.mainloop()


###################################################
# Start here

# This is for screen frame
root = Tk()
root.geometry(str(screen_width) + "x" + str(screen_height))
root.title("Wheel of Fortune!!!")
root.configure(background='black')

init()
