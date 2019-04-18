#! python 3
# -*- coding: utf-8 -*-
"""
Stable Marriage Problem with Gale-Shapley Algorithm
"""

class Participants(object):
    def __init__(self):
        '''
        Active(object), Passive(object)
        activeGroup = [Active]
        passiveGroup = [Passive]
        reference ={'name': Active/Passive}
        freeActive = ['name of Active']
        pairs = {'name of Passive': ['name of Active chosen by Passive']}
        '''
        self.activeGroup = []
        self.passiveGroup = []
        self.reference = {}
        self.freeActive = []
        self.pairs = {}
        
    def addReference(self, participant):
        # register participant(Active/Passive) and his/her name in reference
        name = participant.name
        if name not in self.reference:
            self.reference[name] = participant
            
    def addActive(self, name, preference):
        # create an Active object with name and its preference
        # then add it into the reference
        if name not in self.reference:
            newActive = Active(name, preference)
            self.activeGroup.append(newActive)
            self.addReference(newActive)
    
    def addPassive(self, name, preference):
        # create an Passive object with name and its preference
        # then add it into the reference
        if name not in self.reference:
            newPassive = Passive(name, preference)
            self.activeGroup.append(newPassive)
            self.addReference(newPassive)
        

class Active(object):
    def __init__(self, name, preference):
        '''
        name: name of Active (str)
        preference: ['name of Passive'] (list of str)
        status: 0 (not pairred), 1 (pairred)
        '''
        self.name = name
        self.preference = preference
        self.status = 0
        
class Passive(object):
    def __init__(self, name, preference):
        '''
        name: name of Passive (str)
        preference: {'name of Active': rank of Active} (dict: {keys(str), values(int)})
        candidate: ['name of Active that proposed to Passive'] (list of str)
        status: 0 (not pairred), 1 (pairred)
        '''
        self.name = name
        self.preference = preference
        self.candidate = []
        self.status = 0
