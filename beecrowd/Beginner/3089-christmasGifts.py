# 3089-christmasGifts.py
# Problem: ChristmasGift
# Link: https://judge.beecrowd.com/en/problems/view/3089
# Solved on: 2024-10-30

def christmasGifts():
   while True:
        grandchildrens = int(input())
        if grandchildrens == 0:
            break
        gifts = list(map(int, input().split()))
        maxCost = gifts[0] + gifts[len(gifts) - 1]
        minCost = maxCost
        rightPointer = len(gifts) - 2
        leftPointer = 1

        while leftPointer < rightPointer:
            giftCost = gifts[leftPointer] + gifts[rightPointer]
            if giftCost > maxCost:
                maxCost = giftCost
            if giftCost < minCost:
                minCost = giftCost
            leftPointer += 1
            rightPointer -= 1

        print(f'{maxCost} {minCost}')

christmasGifts()
