# 1047-gameTimeWithMinutes.py
# Problem: Game Time with Minutes
# Link: https://judge.beecrowd.com/en/problems/view/1047
# Solved on: 2024-08-19

def gameTime():

    startHour, startMinute, endHour, endMinute = map(int, input().split())
    minutes = endMinute - startMinute
    
    if minutes < 0:
        minutes += 60
        endHour -= 1

    hours = endHour - startHour
    if hours < 0:
        hours += 24

    if hours == 0 and minutes == 0:
        hours = 24
    print(f'O JOGO DUROU {hours} HORA(S) E {minutes} MINUTO(S)')

gameTime()