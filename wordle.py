#!/usr/bin/python3

import random

alpha = [
"Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "\n", "A", "S", "D", "F", "G", "H", "J", "K", "L", "\n", " ", "Z", "X", "C", "V", "B", "N", "M", "\n"
]

W  = '\033[0m'  # white (normal)
B  = '\033[30m' # black
G  = '\033[32m' # green
O  = '\033[33m' # orange

class Wordle:
    def __init__(self):
        f = open("words.ini", "r")
        temp = f.readlines()
        words = [line[:-1] for line in temp]
        self.word = random.choice(words)
        self.alphaColor = [W] * len(alpha)

        f = open("dict.ini", "r")
        temp = f.readlines()
        self.dict = [line[:-1] for line in temp]

    def getGuess(self):
        self.guess = input("Enter 5 letter word: ").upper()

        while (not self.guess.isalpha() or len(self.guess) != 5 or self.guess not in self.dict):
            print("Invalid entry!\n")
            self.guess = input("Enter 5 letter word: ").upper()
        
    def checkGuess(self):
        if (self.guess == self.word):
            print("You Got It!!\n")
            return True

        self.guessColor = [W] * 5

        freq = {i : self.word.count(i) for i in set(self.word)}

        for i in range(5):
            c = self.guess[i]
            if(c == self.word[i]):
                self.guessColor[i] = G
                freq[c] -= 1
                self.alphaColor[alpha.index(c)] = G
            if(c != self.word[i] and c in self.word and freq[c] > 0):
                self.guessColor[i] = O
                freq[c] -= 1
                if(self.alphaColor[alpha.index(c)] != G):
                    self.alphaColor[alpha.index(c)] = O
            if(c not in self.word):
                self.alphaColor[alpha.index(c)] = B

        self.printBoard(zip(self.guessColor, list(self.guess)))
        self.printBoard(zip(self.alphaColor, alpha))

    def printBoard(self, s):
        for c in s:
            print(c[0] + c[1] + " " + W, end='')

        print("\n")

    def printFail(self):
        print("You Failed!! - Word is: " + self.word)

def main():
    w = Wordle()

    for i in range(6):
        w.getGuess()
        r = w.checkGuess()

        if(not r and i != 5):
            print("Guess Again! - " + str(i+1))
        elif(not r and i == 5):
            w.printFail()
        elif(r):
            return

if __name__ == "__main__":
    main()
