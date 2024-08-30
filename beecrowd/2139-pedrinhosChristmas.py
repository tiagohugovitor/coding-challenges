# 2139-pedrinhosChristmas.py
# Problem: Pedrinho's Christmas
# Link: https://judge.beecrowd.com/en/problems/view/2139
# Solved on: 2024-08-29

def pedrinhosChristmas():
    months = {
        1: 31,
        2: 29,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
    }

    while True:
        try :
            month, day = map(int, input().split())
            if month == 12:
                if day > 25:
                    print('Ja passou!')
                elif day == 25:
                    print('E natal!')
                elif day == 24:
                    print('E vespera de natal!')
                else:
                    print(f'Faltam {25 - day} dias para o natal!')
            else:
                days = 25 - day
                for i in range(month, 12):
                    days += months[i]
                print(f'Faltam {days} dias para o natal!')

        except EOFError:
            break

pedrinhosChristmas()
