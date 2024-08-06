# 0182-duplicateEmails.py
# Problem: Duplicate Emails
# Link: https://leetcode.com/problems/duplicate-emails/description/
# Solved on: 2024-08-05

import pandas as pd

def duplicateEmails(person):
    return person.loc[person.duplicated('email') == True][
                ['email']].drop_duplicates(keep = 'first')