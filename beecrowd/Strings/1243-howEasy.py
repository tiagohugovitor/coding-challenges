# 1243-howEasy.py
# Problem: How Easy
# Link: https://judge.beecrowd.com/en/problems/view/1243
# Solved on: 2024-11-05

import re

def howEasy():
    def isWord(word):
        return bool(re.match(r'^[A-Za-z]+[.]?$', word))

    while True:
        try:
            statementSymbols = input().split()
            wordsAmount = 0
            totalLength = 0

            for symbol in statementSymbols:
                if isWord(symbol):
                    totalLength += len(symbol)
                    wordsAmount += 1
                    if symbol[len(symbol) - 1] == '.':
                        totalLength -= 1
                    
            if wordsAmount == 0:
                average = 0
            else:
                average = totalLength // wordsAmount

            if average <= 3:
                print('250')
            elif average <= 5:
                print('500')
            else:
                print('1000')

        except EOFError:
            break


howEasy()