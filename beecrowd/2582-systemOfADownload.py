# 2582-systemOfADownload.py
# Problem: System of a Download
# Link: https://judge.beecrowd.com/en/problems/view/2582
# Solved on: 2024-09-05

def systemOfADownload():
    songs = {
        0: 'PROXYCITY',
        1: 'P.Y.N.G.',
        2: 'DNSUEY!',
        3: 'SERVERS',
        4: 'HOST!',
        5: 'CRIPTONIZE',
        6: 'OFFLINE DAY',
        7: 'SALT',
        8: 'ANSWER!',
        9: 'RAR?',
        10: 'WIFI ANTENNAS',
    }

    tests = int(input())

    for _ in range(tests):
        a, b = map(int, input().split())
        
        print(songs[a+b])

systemOfADownload()
