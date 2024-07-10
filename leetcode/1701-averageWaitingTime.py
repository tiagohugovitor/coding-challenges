# 1701-averageWaitingTime.py
# Problem: Average Waiting Time
# Link: https://leetcode.com/problems/average-waiting-time/description
# Solved on: 2024-07-09

# Time complexity: O(n)
# Description: This function iterates through all the array once and sums up
# the time taken for each order to be ready.

def averageWaitingTime(customers):
    timeSum = 0
    totalWaitingTime = 0
    for order in customers:
        if(timeSum > order[0]):
            waiting = timeSum - order[0]
        else:
            timeSum = order[0]
            waiting = 0
        totalWaitingTime += (waiting + order[1])
        timeSum += order[1]
    average = totalWaitingTime/len(customers)
    return average
    

print(averageWaitingTime([[2,3],[6,3],[7,5],[11,3],[15,2],[18,1]]))