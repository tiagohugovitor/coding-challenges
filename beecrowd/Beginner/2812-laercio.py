# 2812-laercio.py
# Problem: Laercio
# Link: https://judge.beecrowd.com/en/problems/view/2812
# Solved on: 2024-10-20

import random

def quickSort(array, start, end):
    if start < end:
        pivot = partitionate(array, start, end)
        quickSort(array, start, pivot - 1)
        quickSort(array, pivot + 1, end)

def partitionate(array, start, end):
    pivot = random.randint(start, end)

    temporary = array[start]
    array[start] = array[pivot]
    array[pivot] = temporary

    left, right = start + 1, start + 1

    while right <= end:
        if array[right] < array[start]:
            temporary = array[right]
            array[right] = array[left]
            array[left] = temporary
            left += 1
        right += 1
    temporary = array[start]
    array[start] = array[left - 1]
    array[left - 1] = temporary

    return left - 1


def laercio():
    tests = int(input())

    for _ in range(tests):
        _ = int(input())
        numbers = list(map(int, input().split()))
        odd = []
        
        for number in numbers:
            if number % 2 != 0:
                odd.append(number)

        quickSort(odd, 0, len(odd) - 1)

        print(odd)

        start = 0
        end = len(odd) - 1
        biggest = True

        while(start <= end):
            if start == end:
                print(odd[start], end='')
                break    
            if biggest:
                print(odd[end], end=' ')
                end -= 1
            else:
                print(odd[start], end=' ')
                start += 1
            biggest = not biggest

        print()

laercio()