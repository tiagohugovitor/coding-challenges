# 0175-combineTwoTables.py
# Problem: Combine Two Tables
# Link: https://leetcode.com/problems/combine-two-tables/description/
# Solved on: 2024-08-05

import pandas as pd

def combineTwoTables(person, address):
    df = pd.merge(left=person,right=address,how='left',on='personId')[['firstName', 'lastName', 'city', 'state']]
    return df