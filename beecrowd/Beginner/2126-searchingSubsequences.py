# 2126-searchingSubsequences.py
# Problem: Searching Subsequences
# Link: https://judge.beecrowd.com/en/problems/view/2126
# Solved on: 2024-08-29

def searchingSubsequences():
    cases = 0
    while True:
        cases += 1
        try :
            number1 = input()
            number2 = input()
            amount = 0

            for char in range(len(number2)):
                if number2[char] == number1[0]:
                    isSubstring = True
                    for j in range(0, len(number1)):
                        if char + j > len(number2) - 1 or number1[j] != number2[char + j]:
                            isSubstring = False
                            break
                    if isSubstring:
                        index = char
                        amount += 1

            print(f'Caso #{cases}:')

            if amount == 0:
                print('Nao existe subsequencia')
            else:
                print(f'Qtd.Subsequencias: {amount}')
                print(f'Pos: {index + 1}')
            print()
        except EOFError:
            break

searchingSubsequences()
