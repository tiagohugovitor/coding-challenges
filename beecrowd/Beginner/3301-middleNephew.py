# 3301-middleNephew.py
# Problem: Middle Nephew
# Link: https://judge.beecrowd.com/en/problems/view/3301
# Solved on: 2024-09-03

def insertSort(array):
    for i in range(1, len(array)):
        temp = array[i]
        j = i
        while j > 0 and temp < array[j-1]:
            array[j] = array[j-1]
            j -= 1
        array[j] = temp

    
def middleNephew():
    while True:
        try:
            huguinho, zezinho, luisinho = map(int, input().split())
            array = [huguinho, zezinho, luisinho]
            insertSort(array)
            if array[1] == huguinho:
                print('huguinho')
            elif array[1] == zezinho:
                print('zezinho')
            else:
                print('luisinho')
        
        except EOFError:
            break
    

middleNephew()