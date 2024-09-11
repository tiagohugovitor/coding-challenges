# 2534-generalExam.py
# Problem: General Exam
# Link: https://judge.beecrowd.com/en/problems/view/2534
# Solved on: 2024-09-04

import random

def particionate(array, start, end):
    pivot = random.randint(start, end)
    temp = array[start]
    array[start] = array[pivot]
    array[pivot] = temp
    right = start + 1
    left = start + 1
    while right <= end:
        if array[right] > array[start]:
            temp = array[left]
            array[left] = array[right]
            array[right] = temp
            left += 1
        right += 1
    temp = array[left - 1]
    array[left-1] = array[start]
    array[start] = temp

    return left - 1

def quickSort(array, start, end):
    if start < end:
        pivot = particionate(array, start, end)
        quickSort(array, start, pivot - 1)
        quickSort(array, pivot + 1, end)

def generalExam():
    while True:
        try:
            citzens, queries = map(int, input().split())
            grades = [0] * citzens
            for i in range(citzens):
                grades[i] = int(input())

            quickSort(grades, 0, citzens - 1)

            for _ in range(queries):
                position = int(input())
                print(grades[position - 1])
            
        except EOFError:
            break

generalExam()
