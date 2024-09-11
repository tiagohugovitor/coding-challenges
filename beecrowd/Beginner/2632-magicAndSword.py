# 2632-magicAndSword.py
# Problem: Magic and Sword
# Link: https://judge.beecrowd.com/en/problems/view/2632
# Solved on: 2024-09-09

#NOT WORKING AS EXPECTED


def magicAndSword():
    spells = {
        'fire': {
            'distance': [20, 30, 50],
            'damage': 200
        },
        'water': {
            'distance': [10, 25, 40],
            'damage': 300
        },
        'earth': {
            'distance': [25, 55, 70],
            'damage': 400
        },
        'air': {
            'distance': [18, 38, 60],
            'damage': 100
        }
    }
    tests = int(input())
    for _ in range(tests):
        width, height, x, y = map(int, input().split())
        spell, level, centerX, centerY = input().split()
        level = int(level)
        centerX = int(centerX)
        centerY = int(centerY)
        r = spells[spell]['distance'][level - 1]

        corners = [
            (x, y), (x + width, y),
            (x, y + height), (x + width, y + height)
        ]
        
        damaged = False

        for (px, py) in corners:
            if (px - centerX) ** 2 + (py - centerY) ** 2 <= r ** 2:
                print(spells[spell]['damage'])
                damaged = True
                break
        
        if not damaged:
            edges = [
                (x, y, x + width, y),
                (x, y, x, y + height),
                (x + width, y, x + width, y + height),
                (x, y + height, x + width, y + height)
            ]
            
            for (x1, y1, x2, y2) in edges:
                dx = x2 - x1
                dy = y2 - y1
                if dx == 0 and dy == 0:
                    px, py = x1, y1
                else:
                    t = max(0, min(1, ((centerX - x1) * dx + (centerY - y1) * dy) / (dx * dx + dy * dy)))
                    px, py = x1 + t * dx, y1 + t * dy
                
                if (px - centerX) ** 2 + (py - centerY) ** 2 <= r ** 2:
                    print(spells[spell]['damage'])
                    damaged = True
                    break

        if not damaged:
            print('0')
    
    return False

magicAndSword()
