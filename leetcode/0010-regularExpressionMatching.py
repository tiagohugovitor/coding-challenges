# 0010-regularExpressionMatching.py
# Problem: Regular Expression Matching
# Link: https://leetcode.com/problems/regular-expression-matching/description/
# Solved on: 2024-07-21

# Time complexity: O(m * n)
# Space complexity: O(m * n)
# Description: This function checks if a given string matches a pattern. The function uses a depth-first search (DFS)
# approach with memoization to store intermediate results in a cache,ensuring that overlapping subproblems are computed
# only once.

def isMatch(string, pattern):
    cache = {}

    def dfs(i, j):
        if (i, j) in cache:
            return cache[(i,j)]

        if i >= len(string) and j>= len(pattern):
            return True
        
        if j >= len(pattern):
            return False
        
        match = i < len(string) and (string[i] == pattern[j] or pattern[j] == '.')

        if (j+1) < len(pattern) and pattern[j+1] == '*':
            cache[(i,j)] = dfs(i, j + 2) or (match and dfs(i + 1, j))
            return cache[(i,j)]

        if match:
            cache[(i,j)] = dfs(i+1, j+1)
            return cache[(i,j)]

        cache[(i,j)] = False
        return False

    return dfs(0,0)

print(isMatch())