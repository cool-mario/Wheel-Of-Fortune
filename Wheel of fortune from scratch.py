# Write your code here :-)
###################################################
# Filename: wheel of fortune.py
# Author:   Aidan C and Evan M
# Date:     Feb, 2022
#
# Do not use repl.it - use your own laptop/computer
# or use the Mu Editor

###################################################
# Imports
from tkinter import *
import random, threading, math

import tkinter as tk  # this is all for the wheel
from PIL import ImageTk
from PIL import Image

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

font = "Futura"  # *smirks*

# List of letters to remove after each guess
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W','X', 'Y', 'Z']
# Categories and chosenWords
"""categories = {
'Strange Sayings': ["straighten the horns and kill the bull", 'there is no cow on the ice', 'not my circus, not my monkeys', 'god gives nuts to the man with no teeth'],
'Famous Monkeys': ['donkey kong', 'harambe', 'curious george', 'king kong', 'mmm monke'],
'Countries of the Eurasian Continent': ['germany', 'finland', 'uzbekistan', 'indonesia', 'malaysia'],
'Countries that do not exist': ['northwest korea', 'france', 'saint jose', 'australia', 'west virginia', 'africa', 'elephant', 'greenland', 'the popemobile', 'bremmstrahlung'],
'Popular Video Games': ['tetris', 'minecraft', 'super mario brothers', 'raid shadow legends', 'pokemon', 'among us', 'undertale', 'five nights at freddys'],
'Board Games': ['monopoly', 'sorry', 'trouble', 'settlers of catan', 'clue', 'the game of life', 'operation', 'scrabble', 'chess']
}"""
categories = {
'Animals': ['pig', 'cow', 'horse', 'fish', 'dog', 'cat', 'monke', 'jeff', 'grant scanlan']
}

vowels = ["A", "E", "I", "O", "U"]

# Pick a random category
randChosenCategory = random.randint(0, (len(categories) - 1)) # color or phrase



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
    global displayWidth, wordDisplay

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

    displayWidth = len(thing)
    if displayWidth < 20:
        displayWidth = 15
    wordDisplay.configure(width=displayWidth, font=("Courier new bold", fontSize))

    print("word Display updated")



# We use this to capture the key's pressed
def key_pressed(event):
    global wordDisplay, infoDisplay, root

    print("Key Pressed: " + event.char)
    try:
        x = ord(event.char)
        print("Key Value:   " + str(x))
    except:
        print("strange character pressed")

    if x == 13:
        global buttonPressed
        buttonPressed = True
        print("guess submitted")

    str1 = "You pressed " + event.char
    #wordDisplay['text'] = str1

def displayInfo(textInfo):
    global infoDisplay, root
    infoDisplay['text'] = textInfo

def displayMoreInfo(textInfo, textSize=20):
    global moreInfoDisplay
    moreInfoDisplay.configure(font=(font, textSize))
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
            moreInfoDisplay.configure(text="")
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
                        displayMoreInfo("Sorry, that's not the answer! \nKeep guessing!")
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
                    displayMoreInfo("Not enough money \n;-;",30)
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
            displayMoreInfo("You won!",50)
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
    wordDisplay = Label(root, text="Loading...", height=2, width=20)
    wordDisplay.configure(background='darkblue')
    wordDisplay.configure(font=("Courier New bold", 50))
    wordDisplay.configure(foreground='white')
    wordDisplay.place(relx=0.05, rely=0.05, anchor=NW)

    # somehow thre infoDisplay is not becoming global
    infoDisplay = Label(root, text="Loading...", height=2, width=20)
    infoDisplay.configure(background='purple')
    infoDisplay.configure(font=(font, 40))
    infoDisplay.configure(foreground='white')
    infoDisplay.place(relx=0.05, rely=0.35, anchor=NW)

    moneyDisplay = Label(root, text="you have: $0", height=1, width=20)
    moneyDisplay.configure(background='orange')
    moneyDisplay.configure(font=(font, 40))
    moneyDisplay.configure(foreground='white')
    moneyDisplay.place(relx=0.05, rely=0.55, anchor=NW)

    moreInfoDisplay = Label(root, text="", height=2, width=20)
    moreInfoDisplay.configure(background='black')
    moreInfoDisplay.configure(font=(font, 20))
    moreInfoDisplay.configure(foreground='white')
    moreInfoDisplay.place(relx=0.4, rely=0.7, anchor=NW)

    # Print randChosenCategory name
    displayMoreInfo("Category:\n" + list(categories.keys())[randChosenCategory],30)

    letterGuessEntry = Entry(root)
    letterGuessEntry.configure(font=(font, 100))
    letterGuessEntry.place(relx=0.05, rely=0.7, height=100, width=100, anchor=NW)
    letterGuessEntry.configure(background= "gray15", foreground="white", highlightbackground = "gray30", highlightcolor= "red")

    submitButton = Button(root, text="Submit guess", font=font + " 20", height=2, width=10, command=submitButtonClick)
    submitButton.place(relx=0.21, rely=0.70, anchor=NW)
    submitButton.configure(bg="blue") # doesn't work???

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
    
    app = SimpleApp(root, '/Users/aidan/Desktop/Wheel-Of-Fortune-main/wheel of scanlan.png')
    
    # This runs forever, waiting for mouse clicks
    root.mainloop()


###################################################
# Start here

# This is for screen frame
root = Tk()
root.geometry(str(screen_width) + "x" + str(screen_height))
root.title("Wheel of Fortune!!!")
root.configure(background='black')

class SimpleApp(object):
    def __init__(self, master, filename, **kwargs):
        self.master = master
        self.filename = filename
        self.canvas = tk.Canvas(master, width=50, height=50)
        self.canvas.pack()

        self.update = self.draw().__next__
        master.after(100, self.update)

    def draw(self):
        image = Image.open(self.filename)
        angle = 0
        while True:
            tkimage = ImageTk.PhotoImage(image.rotate(angle))
            canvas_obj = self.canvas.create_image(
                250, 250, image=tkimage)
            self.master.after_idle(self.update)
            yield
            self.canvas.delete(canvas_obj)
            angle += 3
            angle %= 360

init()
