# 2775-preparingProduction.py
# Problem: Preparing Production
# Link: https://judge.beecrowd.com/en/problems/view/2775
# Solved on: 2024-09-11

# Time Limit exceed for insertSort (n²)

def insertSort(array, weights):
    cost = 0
    for i in range(1, len(array)):
        temp, movingCost = array[i], weights[i]
        j = i - 1
        while j >= 0 and array[j] > temp:
            array[j+1], weights[j+1] = array[j], weights[j]
            cost += weights[j] + movingCost
            j -= 1
        array[j+1], weights[j+1] = temp, movingCost   
    return cost

# Merge Sort

def mergeSort(array, weights, start, end):
    if start < end:
        middle = (start + end) // 2
        leftCost = mergeSort(array, weights, start, middle)
        rightCost = mergeSort(array, weights, middle + 1, end)
        mergeCost = merge(array, weights, start, end, middle)
        return leftCost + rightCost + mergeCost
    return 0

def merge(array, weights, start, end, middle):
    leftArray = array[start:middle + 1]
    rightArray = array[middle + 1: end + 1]
    leftWeights = weights[start:middle + 1]
    rightWeights = weights[middle + 1: end + 1]

    leftPointer = 0
    rightPointer = 0
    swaps = 0
    k = start
    cost = 0

    while leftPointer < len(leftArray) and rightPointer < len(rightArray):
        if leftArray[leftPointer] <= rightArray[rightPointer]:
            array[k] = leftArray[leftPointer]
            weights[k] = leftWeights[leftPointer]
            leftPointer += 1
        else:
            array[k] = rightArray[rightPointer]
            weights[k] = rightWeights[rightPointer]
            cost += (middle + 1 - (leftPointer + start)) * (rightWeights[rightPointer] + leftWeights[leftPointer])
            swaps += (middle + 1 - (start + leftPointer))
            rightPointer += 1
        k += 1
    
    while leftPointer < len(leftArray):
        array[k] = leftArray[leftPointer]
        weights[k] = leftWeights[leftPointer]
        leftPointer += 1
        k += 1
    
    while rightPointer < len(rightArray):
        array[k] = rightArray[rightPointer]
        weights[k] = rightWeights[rightPointer]
        rightPointer += 1
        k += 1

    return cost

def preparingProduction():
    while True:
        try:
            n = int(input())
            order = list(map(int, input().split()))
            packages = list(map(int, input().split()))
            cost = mergeSort(order, packages, 0, n - 1)
            print(cost)
        except EOFError:
            break

preparingProduction()

