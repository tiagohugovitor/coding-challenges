# 0181-findEmployee.py
# Problem: Employees Earning More Than Their Managers
# Link: https://leetcode.com/problems/employees-earning-more-than-their-managers/description/
# Solved on: 2024-08-05

import pandas as pd

def findEmployees(employee):
    df = employee.merge(right = employee, how = 'left',
                    left_on = 'managerId',
                    right_on = 'id')

    return pd.DataFrame({'Employee': 
                  df[df.salary_x > df.salary_y]['name_x']})