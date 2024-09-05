# 2540-leadersImpeachment.py
# Problem: Leader's Impeachment
# Link: https://judge.beecrowd.com/en/problems/view/2540
# Solved on: 2024-09-04

def leadersImpeachment():
    while True:
        try:
            players = int(input())
            votes = list(map(int, input().split()))
            impeachment = 0
            for vote in votes:
                impeachment += vote
            
            quorum = 2 * players / 3
            if impeachment >= quorum:
                print('impeachment')
            else:
                print('acusacao arquivada')

        except EOFError:
            break

leadersImpeachment()
