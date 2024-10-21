# 2852-messaging.py
# Problem: Messaging
# Link: https://judge.beecrowd.com/en/problems/view/2852
# Solved on: 2024-10-20

def cipherMessage(message, cipher, size):
    cipherSize = len(cipher)
    ciphered = ''

    for index, char in enumerate(message):
        sliding = cipher[(index + size)% cipherSize]
        if char == ' ':
            cipheredChar = ' '
        else:
            cipheredCharIndex = ord(char) + (ord(sliding) - ord('a'))
            if cipheredCharIndex > ord('z'):
                cipheredCharIndex = ord('a') + (cipheredCharIndex - ord('z')) - 1
            cipheredChar = chr(cipheredCharIndex)
        ciphered = ciphered + cipheredChar
    return ciphered

def messaging():
    cipher = input()
    messages = int(input())
    for _ in range(messages):
        size = 0
        message = list(input().split())
        for index, word in enumerate(message):
            if word[0] not in ['a', 'e', 'i', 'o', 'u']:
                cipheredWord = cipherMessage(word, cipher, size)
                message[index] = cipheredWord
                size += len(word)
        cipheredMessage = ' '.join(message)
        print(cipheredMessage)

messaging()
