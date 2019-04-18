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
        '''register participant(Active/Passive) and his/her name in reference'''
        name = participant.name
        if name not in self.reference:
            self.reference[name] = participant
            
    def addActive(self, name, preference):
        '''
        create an Active object with name and its preference
        then add it into the reference
        '''
        if name not in self.reference:
            newActive = Active(name, preference)
            self.activeGroup.append(newActive)
            self.addReference(newActive)
    
    def addPassive(self, name, preference, capacity):
        '''
        create an Passive object with name, its preference and capacity
        then add it into the reference
        '''
        if name not in self.reference:
            newPassive = Passive(name, preference, capacity)
            self.passiveGroup.append(newPassive)
            self.addReference(newPassive)
            self.pairs[name] = []
            
    def updateStatus(self):
        '''
        update the status of Active and Passive
        if they're in pairs(dict), status = 1; else, status = 0
        '''
        # update status of Active
        pairredActive = []
        for picked in list(self.pairs.values()):
            pairredActive += picked
        for active in self.activeGroup:
            if active.name in pairredActive:
                active.changeStatus(1)
            else:
                active.changeStatus(0)
        
        # update status of Passive
        for passive in self.passiveGroup:
            if self.pairs[passive.name] == []:
                passive.changeStatus(0)
            else:
                passive.changeStatus(1)
    
    def updateFreeActive(self, count):
        '''
        update self.freeActive by appending Active with status = 0
        '''
        # reset freeActive list
        self.freeActive = []
        for active in self.activeGroup:
            if active.status == 0:
                self.freeActive.append(active.name)
                if count > 0: # if this isn't the first time Active enters the freeActive list,
                    active.rejectCount += 1 # it means Active is rejected by Passive in the last round
                
    def assign(self):
        '''
        Match Active with Passive
        '''
        count = 0 # count the number of matching(round) done
        self.updateFreeActive(count)
        
        while len(self.freeActive) > 0: # when there are still Active that are not pair with any Passive
            print("Matching Round: {}\n".format(count))
            
            # Active propose
            for active in self.activeGroup:
                if active.status == 0: # Active that are not pairred will propose
                    active.propose(self.reference)
            print()
            # Passive accept
            for passive in self.passiveGroup:
                passive.accept(self.pairs)
            print('\nCurrent Matching')
            print(self.pairs)
            
            count += 1 # one round of matching completed
            self.updateStatus() # update status of Active and Passive
            self.updateFreeActive(count)
            
            print('unpairred:', self.freeActive)
            print('-'*50)
            
        print("Stable Matching obtained!")
        print(self.pairs)
        

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
        self.rejectCount = 0
    
    def changeStatus(self, changeTo):
        self.status = changeTo
        
    def propose(self, reference):
        '''
        get the 'count'th preference of Active and
        add Active to the Passive's candidate
        reference: a dict to get Active using Active.name (dict)
        count: (int)
        '''
        print(self.name, 'Preference:', self.preference)
        choice = reference[self.preference[self.rejectCount]]
        choice.candidate.append(self.name)
        
class Passive(object):
    def __init__(self, name, preference, capacity):
        '''
        name: name of Passive (str)
        preference: {'name of Active': rank of Active} (dict: {keys(str), values(int)})
        candidate: ['name of Active that proposed to Passive'] (list of str)
        status: 0 (not pairred), 1 (pairred)
        capacity: number of Active able to pair with (int)
        '''
        self.name = name
        self.preference = preference
        self.candidate = []
        self.status = 0
        self.capacity = capacity
    
    def changeStatus(self, changeTo):
        self.status = changeTo
        
    def accept(self, pairs_dict):
        '''
        choose Active(s) from candidate list of number up to capacity
        pairs_dict: Participants.pairs
        '''
        if len(self.candidate) > 0:
            print(self.name, 'Preference:', self.preference)
            
            # add temporarily pairred Active to candidate list
            if self.status == 1:
                self.candidate += pairs_dict[self.name]
            print(self.name, 'Candidate:', self.candidate)
            
            pairs_dict[self.name] = [] # reset Passive's pair in pairs_dict 
            
            # a list containing only ranking (int) for easier comparison
            candidate_rank = [self.preference[active] for active in self.candidate]
#            print(self.name, candidate_rank) # uncommend when debugging
            
            # pick Active 
            for n in range(self.capacity):
                # get the index of choice in candidate
                choice = min(candidate_rank)
                choice_index = candidate_rank.index(choice)
                # add selected Active in pairs_dict
                pairs_dict[self.name].append(self.candidate.pop(choice_index))
                candidate_rank.remove(choice)
                
        # reset candidate list after choosing
        self.candidate = []
        
            
