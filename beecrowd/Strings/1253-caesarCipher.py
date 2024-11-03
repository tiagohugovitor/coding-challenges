# 1253-caesarCipher.py
# Problem: Contract Revision
# Link: https://judge.beecrowd.com/en/problems/view/1253
# Solved on: 2024-11-01

def caesarCipher():
    tests = int(input())

    for _ in range(tests):
        message = input()
        shift = int(input())
        encrypted = ''

        for char in message:
            charEncrypted = (ord(char) - shift)
            if charEncrypted < ord('A'):
                charEncrypted = ord('Z') - (ord('A') - charEncrypted) + 1

            encrypted += chr(charEncrypted)

        print(encrypted)

caesarCipher()