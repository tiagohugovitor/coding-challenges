# 1047-gameTimeWithMinutes.py
# Problem: Game Time with Minutes
# Link: https://judge.beecrowd.com/en/problems/view/1047
# Solved on: 2024-08-19

def gameTime():

    startHour, startMinute, endHour, endMinute = map(int, input().split())
    hours = endHour - startHour if endHour > startHour else 24 - startHour + endHour
    minutes = endMinute - startMinute if endMinute > startMinute else (60 - startMinute + endMinute) % 60
    if endMinute < startMinute:
        hours -= 1
    if hours == 24 and minutes > 0:
        hours = 0
    print(f'O JOGO DUROU {hours} HORA(S) E {minutes} MINUTO(S)')

gameTime()