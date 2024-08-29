# 2003-sundayMorning.py
# Problem: Sunday Morning
# Link: https://judge.beecrowd.com/en/problems/view/2003
# Solved on: 2024-08-28

def sundayMorning():
    while True:
        try:
            hours, minutes = map(int, input().split(':'))
            total = hours * 60 + minutes + 60
            expectedHour = 480
            delay = total - expectedHour if total > expectedHour else 0
            print(f'Atraso maximo: {delay}') 
        except EOFError:
            break

sundayMorning()
