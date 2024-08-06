# 0183-findCustomers.py
# Problem: Customers Who Never Order
# Link: https://leetcode.com/problems/customers-who-never-order/description/
# Solved on: 2024-08-05

import pandas as pd

def findEmployees(customers, orders):
    df = customers.merge(orders, left_on='id', right_on='customerId', how='left')
    return df[df['customerId'].isna()][['name']].rename(columns={'name':'Customers'})