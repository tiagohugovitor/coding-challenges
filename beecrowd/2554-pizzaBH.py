# 2554-pizzaBH.py
# Problem: Pizza Before BH
# Link: https://judge.beecrowd.com/en/problems/view/2554
# Solved on: 2024-09-05

def pizzaBH():
    while True:
        try:
            people, dates = map(int, input().split())
            
            options = [0] * dates

            for day in range(dates):
                options[day] = list(input().split())

            for option in options:
                possible = True
                for person in range(people):
                    if int(option[person + 1]) == 0:
                        possible = False

                if possible:
                    print(option[0])
                    break
            
            if not possible:
                print('Pizza antes de FdI')

        except EOFError:
            break

pizzaBH()
