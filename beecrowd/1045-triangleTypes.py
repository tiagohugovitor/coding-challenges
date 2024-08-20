# 1045-triangleTypes.py
# Problem: Triangle Types
# Link: https://judge.beecrowd.com/en/problems/view/1045
# Solved on: 2024-08-19

def triangleTypes():

    a, b, c = map(float, input().split())

    def insertionSortReversed(a,b,c):
        ordered = [a,b,c]
        for i in range(1, 3):
            current = ordered[i]
            j = i-1
            while j >=0 and ordered[j] < current:
                ordered[j + 1] = ordered[j]
                j -= 1
            ordered[j+1] = current
        return ordered

    triangle = insertionSortReversed(a,b,c)
    if triangle[0] >= triangle[1] + triangle[2]:
        print('NAO FORMA TRIANGULO')
        return
    if triangle[0]**2 == (triangle[1]**2 + triangle[2]**2):
        print('TRIANGULO RETANGULO')
    if triangle[0]**2 > (triangle[1]**2 + triangle[2]**2):
        print('TRIANGULO OBTUSANGULO')
    if triangle[0]**2 < (triangle[1]**2 + triangle[2]**2):
        print('TRIANGULO ACUTANGULO')
    if a == b and b == c:
        print('TRIANGULO EQUILATERO')
    elif a == b or b == c or a == c:
        print('TRIANGULO ISOSCELES')

triangleTypes()