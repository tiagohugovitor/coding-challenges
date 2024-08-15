# 0434-countSegments.py
# Problem: Number of Segments in a String
# Link: https://leetcode.com/problems/number-of-segments-in-a-string/description/
# Solved on: 2024-08-15

# Time complexity: O(n)
# Space complexity: O(1)
# Description: This function counts the number of segments in a string `s`, where a segment is defined as a contiguous 
# sequence of non-space characters. It iterates through each character in the string, tracking whether the current character 
# is part of a segment using a boolean flag `inSegment`. When it encounters a non-space character that starts a new segment, 
# it increments the segment count.

def countSegments(s):
    segments = 0
    inSegment = False

    for char in s:
        if char != ' ' and not inSegment:
            inSegment = True
            segments += 1
        elif char == ' ':
            inSegment = False

    return segments
    

print(countSegments('Hello, my name    is John'))