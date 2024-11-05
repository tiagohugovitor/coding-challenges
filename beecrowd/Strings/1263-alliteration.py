# 1263-alliteration.py
# Problem: Alliteration
# Link: https://judge.beecrowd.com/en/problems/view/1263
# Solved on: 2024-11-04

def alliteration():
    while True:
        try:
            words = list(input().split())
            alliterations = 0
            currentFirstLetter = ''
            count = 0
            for word in words:
                if count == 2:
                    alliterations += 1
                if currentFirstLetter != word[0].lower():
                    count = 1
                    currentFirstLetter = word[0].lower()
                else:
                    count += 1

            if count == 2:
                alliterations += 1

            print(alliterations)

        except EOFError:
            break
alliteration()