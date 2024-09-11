# 1960-romanNumeralsForPage.py
# Problem: Roman Numerals for Page Numbers
# Link: https://judge.beecrowd.com/en/problems/view/1960
# Solved on: 2024-08-27

def romanNumeralsForPage():
    intToRoman = {
        1000: 'M',
        900: 'CM',
        500: 'D',
        400: 'CD',
        100: 'C',
        90: 'XC',
        50: 'L',
        40: 'XL',
        10: 'X',
        9: 'IX',
        5: 'V',
        4: 'IV',
        1: 'I',
    }

    number = int(input())
    result = ''

    for i in intToRoman:
        if number == 0:
            break
        while number >= i:
            result = result + intToRoman[i]
            number -= i

    print(result)

    
romanNumeralsForPage()
