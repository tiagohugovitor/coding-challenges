# 1061-eventTime.py
# Problem: Event Time
# Link: https://judge.beecrowd.com/en/problems/view/1061
# Solved on: 2024-08-19

def eventTime():
    startDay = int(input().split()[1])
    startHours, startMinutes, startSeconds = map(int, input().split(' : '))
    endDay = int(input().split()[1])
    endHours, endMinutes, endSeconds = map(int, input().split(' : '))
    
    startTotalSeconds = startDay * 86400 + startHours * 3600 + startMinutes * 60 + startSeconds
    endTotalSeconds = endDay * 86400 + endHours * 3600 + endMinutes * 60 + endSeconds
    
    totalSeconds = endTotalSeconds - startTotalSeconds
    
    days = totalSeconds // 86400
    totalSeconds %= 86400
    hours = totalSeconds // 3600
    totalSeconds %= 3600
    minutes = totalSeconds // 60
    seconds = totalSeconds % 60

    print(f'{days} dia(s)')
    print(f'{hours} hora(s)')
    print(f'{minutes} minuto(s)')
    print(f'{seconds} segundo(s)')

eventTime()