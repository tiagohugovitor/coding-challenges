# 1598-crawlerLogFolder.py
# Problem: Crawler Log Folder
# Link: https://leetcode.com/problems/crawler-log-folder/description/
# Solved on: 2024-07-09

# Time complexity: O(n)
# Description: This function iterates through the array once and use a count
# variable to store how deep we are in the folders

def minOperations(logs):
    operations = 0
    for log in logs:
        if log == '../':
            operations -= 1
        elif log != './':
            operations += 1
        operations = max(operations, 0)
    return operations

print(minOperations(["d1/","d2/","../","d21/","./"]))