# 2694-problemWithTheCalculator.py
# Problem: OBI URI
# Link: https://judge.beecrowd.com/en/problems/view/2694
# Solved on: 2024-11-12


def problemWithTheCalculator():
    tests = int(input())

    for _ in range(tests):
        operation = input()
        total = 0
        seeNumber = False
        number = ''
        for char in operation:
            if char.isnumeric():
                seeNumber = True
                number += char
            else:
                if seeNumber:
                    total += int(number)
                    number = ''
                    seeNumber = False

        if seeNumber:
            total += int(number)
        
        print(total)


problemWithTheCalculator()