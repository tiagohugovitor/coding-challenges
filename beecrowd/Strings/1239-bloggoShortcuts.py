# 1239-bloggoShortcuts.py
# Problem: Bloggo Shortcuts
# Link: https://judge.beecrowd.com/en/problems/view/1239
# Solved on: 2024-11-04

def bloggoShortcuts():
    while True:
        try:
            text = input()
            openedItalic = False
            openedBold = False
            translated = ''
            for char in text:
                if char == '_':
                    translated += '</i>' if openedItalic else '<i>'
                    openedItalic = not openedItalic
                    continue
                if char == '*':
                    translated += '</b>' if openedBold else '<b>'
                    openedBold = not openedBold
                    continue
                translated += char
                
            print(translated)

        except EOFError:
            break

bloggoShortcuts()