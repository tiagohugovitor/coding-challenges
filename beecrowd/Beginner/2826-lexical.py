# 2826-lexical.py
# Problem: Lexical
# Link: https://judge.beecrowd.com/en/problems/view/2826
# Solved on: 2024-10-21

def lexical():
    word1 = input()
    word2 = input()

    index = 0
    first, second = word1, word2

    while index < len(word1) and index < len(word2):
        if ord(word1[index]) > ord(word2[index]):
            first = word2
            second = word1
            break
        if ord(word1[index]) < ord(word2[index]):
            first = word1
            second = word2
            break
        index += 1

    if index == len(word1):
        first = word1
        second = word2
    
    if index == len(word2):
        first = word2
        second = word1

    print(first)
    print(second)

lexical()
