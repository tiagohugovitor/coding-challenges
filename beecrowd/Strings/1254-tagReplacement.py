# 1254-tagReplacement.py
# Problem: Tag Replacement
# Link: https://judge.beecrowd.com/en/problems/view/1254
# Solved on: 2024-11-12

#PRESENTATION ERROR

def tagReplacement():
    tests = 0
    while True:
        try:
            if tests != 0:
                print()
            originalWordTag = input()
            replaceNumberTag = input()
            document = input()
            openedTag = False
            index = 0
            while index < len(document):
                char = document[index]
                index += 1
                if char == '<':
                    openedTag = True
                    continue

                if not openedTag:
                    continue
                
                originalTag = document[index - 1:].split('>')[0].lower()
                replaceTag = originalTag.replace(originalWordTag.lower(), replaceNumberTag)
                if replaceTag != originalTag:
                    document = document[:index-1] + replaceTag + document[index -1 + len(originalTag):]
                openedTag = False
                index += len(replaceTag)

            print(f'{document}', end='')
            tests += 1

        except EOFError:
            break
tagReplacement()