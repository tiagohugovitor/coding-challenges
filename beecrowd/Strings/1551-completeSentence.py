# 1551-completeSentence.py
# Problem: Complete Sentence
# Link: https://judge.beecrowd.com/en/problems/view/1551
# Solved on: 2024-11-03

def completeSentence():
    tests = int(input())

    for _ in range(tests):
        sentence = input()
        dictionary = set()

        for char in sentence:
            if char.isalpha():
                dictionary.add(char)

        if len(dictionary) >= 26:
            print('frase completa')
            continue

        if len(dictionary) >= 13:
            print('frase quase completa')
            continue

        print('frase mal elaborada')

completeSentence()