# 0029-divideTwoIntegers.py
# Problem: Divide Two Integers
# Link: https://leetcode.com/problems/divide-two-integers/description/
# Solved on: 2024-07-28
    
# Time complexity: O(n)
# Space complexity: O(1)
# Description: This function divides two integers without using multiplication, division, or modulo operators.
# The result's sign is determined based on the signs of the dividend and divisor. The absolute value of the
# dividend is reduced by the absolute value of the divisor until the dividend is smaller than the divisor.
# The result is adjusted to ensure it falls within the range of a 32-bit signed integer.
    
def divideTwoIntegers(dividend, divisor):
    result = 0
    sign = 1
    if ((dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0)):
        sign = -1
    dividendAbs = abs(dividend)
    divisorAbs = abs(divisor)

    while dividendAbs >= divisorAbs:
        dividendAbs -= divisorAbs
        result += 1

    output = result if sign == 1 else 0 - result
    return min(2147483647, max(output, -2147483648))


# Time complexity: O(log n)
# Space complexity: O(1)
# Description: This optimized function divides two integers without using multiplication, division, or modulo operators.
# It utilizes bitwise operations to efficiently find the quotient by doubling the divisor and reducing the dividend
# correspondingly. The result's sign is determined based on the signs of the dividend and divisor. The final result is
# adjusted to ensure it falls within the range of a 32-bit signed integer.

def divideTwoIntegersOptimized(dividend, divisor):
    result = 0
    sign = 1
    if ((dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0)):
        sign = -1
    dividendAbs = abs(dividend)
    divisorAbs = abs(divisor)

    while dividendAbs >= divisorAbs:
        mult = divisorAbs
        count = 1
        while dividendAbs >= mult:
            dividendAbs -= mult
            result += count
            mult += mult
            count += count

    output = result if sign == 1 else 0 - result
    return min(2147483647, max(output, -2147483648))

print(divideTwoIntegersOptimized(10000,3))