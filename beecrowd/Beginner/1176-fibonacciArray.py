# 1176-fibonacciArray.py
# Problem: Fibonacci Array
# Link: https://judge.beecrowd.com/en/problems/view/1176
# Solved on: 2024-08-22

def fibonacciArray():
    tests = int(input())
    fibonacci = [0, 1]

    def getFibonnaci(array, n):
        size = len(array) - 1
        for i in range(size, n):
            array.append(array[i] + array[i-1])
    
    for _ in range(tests):
        number = int(input())
        if number > len(fibonacci) - 1:
            getFibonnaci(fibonacci, number)
        print(f'Fib({number}) = {fibonacci[number]}')

fibonacciArray()