# 2168-twilightAtPortland.py
# Problem: Twilight at Portland
# Link: https://judge.beecrowd.com/en/problems/view/2168
# Solved on: 2024-08-31

def twilightAtPortland():
    size = int(input())
    blocks = [0] * (size + 1)

    for i in range(size+1):
        blocks[i] = list(map(int, input().split()))
  
    for i in range(size):
        blockResult = []
        for j in range(size):
            topLeft = blocks[i][j]
            topRight = blocks[i][j+1]
            bottomLeft = blocks[i+1][j]
            bottomRight = blocks[i+1][j+1]
            
            cameras = topLeft + topRight + bottomLeft + bottomRight

            if cameras >= 2:
                blockResult.append('S')
            else:
                blockResult.append('U')
        
        print(''.join(blockResult))

twilightAtPortland()
