# 2635-webBrowser.py
# Problem: Web Browser
# Link: https://judge.beecrowd.com/en/problems/view/2635
# Solved on: 2024-09-06

def isSubstring(search, word):
    if len(word) < len(search):
        return False

    for i in range(len(search)):
        if word[i] != search[i]:
            return False
    return True

def webBrowser():
    while True:
        try:
            history = int(input())
            words = [0] * history
            for search in range(history):
                words[search] = input()

            queries = int(input())
            for _ in range(queries):
                search = input()
                count = 0
                maxLength = 0
                for word in words:
                    if isSubstring(search, word):
                        count += 1
                        if len(word) > maxLength:
                            maxLength = len(word)
                if count > 0:
                    print(f'{count} {maxLength}')
                else:
                    print('-1')
        except EOFError:
            break

webBrowser()
