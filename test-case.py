#! python 3
# -*- coding: utf-8 -*-
"""
Stable Marriage Problem with Gale-Shapley Algorithm
"""

import stableMarriage as sm

village = sm.Participants()

'''
male: A, B, C, D (Passive)
female: W, X, Y, Z (Active)
'''
male = [('A', {'X':1, 'Y':2, 'Z':1, 'W':4}),
        ('B', {'X':1, 'Y':2, 'Z':1, 'W':4}), 
        ('C', {'X':3, 'Y':1, 'Z':2, 'W':4}),
        ('D', {'X':4, 'Y':3, 'Z':2, 'W':1})]

female = [('W', ['A', 'C', 'B', 'D']), 
          ('X', ['D', 'C', 'A', 'B']),
          ('Y', ['A', 'D', 'C', 'B']),
          ('Z', ['A', 'D', 'C', 'B'])]

for boy in male:
    village.addPassive(boy[0], boy[1])
for girl in female:
    village.addActive(girl[0], girl[1])
    
print(village.reference)

