#! python 3
# -*- coding: utf-8 -*-
"""
Stable Marriage Problem with Gale-Shapley Algorithm
Test-Case
"""

import stableMarriage as sm


def testFunction(func):
     # initialise       
    village = sm.Participants()
    '''
    male: A, B, C, D (Passive)
    female: W, X, Y, Z (Active)
    '''
    male = [('A', {'X':4, 'Y':2, 'Z':1, 'W':3}, 1),
            ('B', {'X':1, 'Y':2, 'Z':3, 'W':4}, 1), 
            ('C', {'X':3, 'Y':1, 'Z':2, 'W':4}, 1),
            ('D', {'X':4, 'Y':3, 'Z':2, 'W':1}, 1)]
    
    female = [('W', ['A', 'C', 'B', 'D']), 
              ('X', ['D', 'C', 'A', 'B']),
              ('Y', ['A', 'D', 'C', 'B']),
              ('Z', ['D', 'A', 'C', 'B'])]
    
    for boy in male:
        village.addPassive(boy[0], boy[1], boy[2])
    for girl in female:
        village.addActive(girl[0], girl[1])
    
    if func == 'propose':
        for girl in village.activeGroup:
            girl.propose(village.reference, 0)
        for boy in village.passiveGroup:
            print(boy.candidate)
            
    elif func == 'accept':
        for girl in village.activeGroup:
            girl.propose(village.reference, 0)
        for boy in village.passiveGroup:
            boy.accept(village.pairs)
        print(village.pairs)
    
    elif func == 'changeStatus':
        for girl in village.activeGroup:
            girl.changeStatus(1)
            print(girl.name, girl.status)
        for girl in village.activeGroup:
            print(girl.name, girl.status)
            
    elif func == 'assign':
        village.assign()

def testCapacity():
    '''
    assigning 8 students to 4 different labs,
    where each lab has a capacity of 2
    '''
    uni = sm.Participants()
    labs = [('A', {'S':8, 'T':1, 'U':2, 'V':3, 'W':4, 'X':5, 'Y':6, 'Z':7}, 1),
           ('B', {'S':8, 'T':1, 'U':2, 'V':3, 'W':4, 'X':5, 'Y':6, 'Z':7}, 2), 
           ('C', {'S':8, 'T':1, 'U':2, 'V':3, 'W':4, 'X':5, 'Y':6, 'Z':7}, 3),
           ('D', {'S':8, 'T':1, 'U':2, 'V':3, 'W':4, 'X':5, 'Y':6, 'Z':7}, 2)]
    students = [('S', ['A', 'C', 'B', 'D']),
                ('T', ['C', 'A', 'B', 'D']),
                ('U', ['A', 'C', 'D', 'B']),
                ('V', ['A', 'B', 'C', 'D']),
                ('W', ['A', 'D', 'B', 'C']),
                ('X', ['D', 'C', 'A', 'B']),
                ('Y', ['A', 'D', 'C', 'B']),
                ('Z', ['D', 'A', 'C', 'B'])]
    for lab in labs:
        uni.addPassive(lab[0], lab[1], lab[2])
    for student in students:
        uni.addActive(student[0], student[1])
        
    uni.assign()


#testFunction('propose')
#testFunction('accept')
#testFunction('changeStatus')
#testFunction('assign')
#testCapacity()