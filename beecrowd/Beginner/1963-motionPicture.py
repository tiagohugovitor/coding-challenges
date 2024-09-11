# 1963-motionPicture.py
# Problem: The Motion Picture
# Link: https://judge.beecrowd.com/en/problems/view/1963
# Solved on: 2024-08-27

def motionPicture():
    oldPrice, newPrice = map(float, input().split())
    increase = (newPrice - oldPrice) * 100 / oldPrice
    print(f'{increase:.2f}%')

motionPicture()
