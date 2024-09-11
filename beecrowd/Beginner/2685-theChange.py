# 2685-theChange.py
# Problem: The Change
# Link: https://judge.beecrowd.com/en/problems/view/2685
# Solved on: 2024-09-06

def theChange():
    time = {
        90: 'Bom Dia!!',
        180: 'Boa Tarde!!',
        270: 'Boa Noite!!',
        360: 'De Madrugada!!',
    }
    while True:
        try:
            angle = int(input()) % 360
            for period in time:
                if angle < period:
                    print(time[period])
                    break  
        except EOFError:
            break

theChange()
