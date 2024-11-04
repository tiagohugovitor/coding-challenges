# 2137-severino.py
# Problem: The Library of Mr. Severino
# Link: https://judge.beecrowd.com/en/problems/view/2137
# Solved on: 2024-11-03

def severino():
    while True:
        try:
            books = int(input())
            codes = []
            
            for _ in range(books):
                bookCode = input()
                codes.append(bookCode)
            
            codes.sort()

            for code in codes:
                print(code)


        except EOFError:
            break

severino()