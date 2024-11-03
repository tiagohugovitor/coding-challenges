# 1234-dancingSequence.py
# Problem: Dancing Sequence
# Link: https://judge.beecrowd.com/en/problems/view/1234
# Solved on: 2024-11-03

def dancingSequence():
    while True:
        try:
            string = input()

            dancingString = ''
            upper = True

            for char in string:
                if char == ' ':
                    dancingString += ' '
                    continue
                if upper:
                    dancingString += char.upper()
                    upper = False
                    continue
                dancingString += char.lower()
                upper = True

            print(dancingString)
        
        except EOFError:
            break

dancingSequence()