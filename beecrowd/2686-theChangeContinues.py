# 2686-theChangeContinues.py
# Problem: The Change Continues
# Link: https://judge.beecrowd.com/en/problems/view/2686
# Solved on: 2024-09-06

def theChangeContinues():
    time = {
        90: 'Bom Dia!!',
        180: 'Boa Tarde!!',
        270: 'Boa Noite!!',
        360: 'De Madrugada!!',
    }
    while True:
        try:
            angle = float(input()) % 360
            for period in time:
                if angle < period:
                    print(time[period])
                    break
            
            seconds = angle * 86400 / 360
            minutes = int(seconds // 60)
            seconds = int(seconds % 60)
            hours = (int(minutes // 60) + 6) % 24
            minutes = minutes % 60

            print(f'{hours:>02}:{minutes:>02}:{seconds:>02}')

        except EOFError:
            break

theChangeContinues()
