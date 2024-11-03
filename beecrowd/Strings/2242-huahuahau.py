# 2242-huahauhauh.py
# Problem: Huaauhahhuahau
# Link: https://judge.beecrowd.com/en/problems/view/2242
# Solved on: 2024-11-03

def huahauhauh():
    laughter = input()

    vowelLaughter = ''.join([char for char in laughter if char in ['a', 'e', 'i', 'o', 'u']])

    reversedVowelLaughter = vowelLaughter[::-1]

    if vowelLaughter == reversedVowelLaughter:
        print('S')
    else:
        print('N')

huahauhauh()