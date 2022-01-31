#!/usr/bin/python3

import random

alpha = [
"Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "\n", "A", "S", "D", "F", "G", "H", "J", "K", "L", "\n", " ", "Z", "X", "C", "V", "B", "N", "M", "\n"
]

W  = '\033[0m'  # white (normal)
B  = '\033[30m' # black
G  = '\033[32m' # green
O  = '\033[33m' # orange

word = "XXXXX"

charsInWord = set() 
charsCorrect = set()
charsNotInWord = set()

def populateWords():
    f = open("dict.ini", "r")

    temp = f.readlines()

    words = [line[:-1] for line in temp]

    global word 
    word = random.choice(words)

def getGuess():
    value = input("Enter 5 letter word: ").upper()

    if(not value.isalpha() or len(value) != 5):
        print("Invalid entry!\n")
        getGuess()
    
    return value

def checkGuess(guess):

    if (guess == word):
        print("You Got It!!\n")
        return True

    for i in range(5):
        if(guess[i] == word[i]):
            charsCorrect.add(guess[i])
    
    for c in guess:
        if (word.find(c) != -1):
            charsInWord.add(c)
        else:
            charsNotInWord.add(c)

    printGuess(guess)
    print("\n")
    printAlpha(alpha)
    print("\n")

def printGuess(guess):
    for i in range(5):
        if(guess[i] == word[i]):
            print(G + guess[i] + W, end='')
        elif(guess[i] in charsInWord):
            print(O + guess[i] + W, end='')
        else:
            print(guess[i], end='')

def printAlpha(s):

    for c in alpha:
        if c in charsCorrect:
            print(G + c + " " + W, end='')
        elif c in charsInWord:
            print(O + c + " " + W, end='')
        elif c in charsNotInWord:
            print(B + c + " " + W, end='')
        else:
            print(c + " ", end='')


def main():
    populateWords()

    for i in range(6):
        r = checkGuess(getGuess())

        if(not r and i != 5):
            print("Guess Again! - " + str(i+1))
        elif(not r and i == 5):
            print("You Failed!! - Word is: " + word)
        elif(r):
            return



if __name__ == "__main__":
    main()