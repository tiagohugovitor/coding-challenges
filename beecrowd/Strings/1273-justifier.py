# 1273-justifier.py
# Problem: Justifier
# Link: https://judge.beecrowd.com/en/problems/view/1273
# Solved on: 2024-11-03

def justifier():
    test = 0
    while True:
        wordsAmount = int(input())

        if wordsAmount == 0:
            break
        
        if test != 0:
            print()

        words = []
        biggestWord = 0

        for _ in range(wordsAmount):
            word = input().strip()
            words.append(word)

            if len(word) > biggestWord:
                biggestWord = len(word)

        for word in words:
            print(f'{word:>{biggestWord}}')

        test += 1
    
justifier()