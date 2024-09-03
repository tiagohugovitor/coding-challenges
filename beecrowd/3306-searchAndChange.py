# 3306-searchAndChange.py
# Problem: Search and Change
# Link: https://judge.beecrowd.com/en/problems/view/3306
# Solved on: 2024-09-03

# Still not working 

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def findGCDInArray(array, start, end):
    result = array[start]
    for i in range(start + 1, end):
        result = gcd(result, array[i])
    return result

def searchAndChange():
    while True:
        try:
            n, q = map(int, input().split())
            elements = list(map(int, input().split()))
            for _ in range(q):
                query = list(map(int, input().split()))
                start = query[1] - 1
                end = query[2] - 1
                if query[0] == 1:
                    add = query[3]
                    for i in range(start, end):
                        elements[i] += add
                else:
                    result = findGCDInArray(elements, start, end + 1)
                    print(result)

        except EOFError:
            break
    

searchAndChange()