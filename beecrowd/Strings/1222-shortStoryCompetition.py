# 1222-shortStoryCompetition.py
# Problem: Short Story Competition
# Link: https://judge.beecrowd.com/en/problems/view/1222
# Solved on: 2024-11-05

import math

def shortStoryCompetition():
    while True:
        try:
            _, numberOfLines, numberOfCharacters = map(int, input().split())
            story = list(input().split())
            line = 0
            lines = 1
            for word in story:
                if len(word) + line > numberOfCharacters:
                    line = len(word) + 1
                    lines += 1
                else:
                    line += len(word) + 1

            pages = math.ceil(lines / numberOfLines)
                    
            print(pages)

        except EOFError:
            break

shortStoryCompetition()