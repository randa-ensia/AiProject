import copy
import random 
import initialstate
from random import choice
from collections import deque
class Node:
    def __init__(self, state, parent=None, action=None, cost=0):
        self.state = state
        self.parent = parent # node
        self.action = action # action performed to get to this node
        self.cost = cost # (incremented with each newly expanded node)
        if parent is None: # root node
            self.depth = 0 # level in the graph 0 for the root node
        else:
            self.depth = parent.depth + 1 # parent level + 1
    def __hash__(self):
       return hash(tuple (map (tuple ,self.state)))
    def __eq__(self, other):
        if  self.state == other.state :
            return True
        else :
            return False
class Agriculture:
    def __init__(self, initial_state, goal_state, state_transition_model,path_cost=0,actions=""):
        self.state = initial_state
        self.goal_state = goal_state
        self.state_transition_model = state_transition_model
        self.actions=actions
        self.path_cost=path_cost 

    def transition_model_function (self,state, action):
        new_state = copy.deepcopy(state)
        wilaya , product, condition , land = action 
        wilaya_data = state['wilayas'][wilaya]
        unused_land = state ['wilayas'][wilaya]['Land_data']['unused land']
        if unused_land >= land :
            state ['wilayas'][wilaya]['Products'][product]['land_surface'] += land*unused_land
            state ['wilayas'][wilaya]['Products'][product]['productivity'] = transition_model['change conditions '][product][condition]
            state ['wilayas'][wilaya]['Products'][product]['production'] = state ['wilayas'][wilaya]['Products'][product]['land_surface']*state ['wilayas'][wilaya]['Products'][product]['productivity']


                
                    

transition_model = {
    'change conditions ':{
        'Wheat': {
            'Poor': random.uniform (0,10), 
            'Below average': random.uniform (10,20),
            'Average': random.uniform (20,35),
            'Above Average': random.uniform (35,50),
            'Ideal': random.uniform (50,90),
        },
        'Corn': {
            'Poor': random.uniform (0,20),
            'Below average': random.uniform (20,40),
            'Average': random.uniform (40,60),
            'Above Average':random.uniform (60,80),
            'Ideal': random.uniform(80,150)
        },
        'Dates': {
            'Poor': random.uniform (0,20),
            'Below average':random.uniform (20,40),
            'Average': random.uniform (40,60),
            'Above Average': random.uniform (60,80),
            'Ideal': random.uniform(80,180)
        },
        'Potatoes': {
            'Poor': random.uniform (0,100),
            'Below average':random.uniform (100,200), 
            'Average':random.uniform (200,300),
            'Above Average': random.uniform (300,400),
            'Ideal': random.uniform(400,500)
        },
        'Tomatoes': {
            'Poor': random.uniform (0,200),
            'Below average':random.uniform (200,400),
            'Average': random.uniform (400,600),
            'Above Average':random.uniform (600,800), 
            'Ideal': random.uniform(800,1000)
        },
        'Green Pepper': {
            'Poor': random.uniform (0,100),
            'Below average': random.uniform (100,200),
            'Average': random.uniform (200,300),
            'Above Average': random.uniform (300,400),
            'Ideal': random.uniform(400,500)
        },
        'Aubergines': {
            'Poor':random.uniform(0,100),
            'Below average':random.uniform(100,200), 
            'Average':random.uniform(200,300),
            'Above Average':random.uniform(300,400),
            'Ideal':random.uniform(400,600),
        },
        'Onions': {
            'Poor':random.uniform(0,100), 
            'Below average':random.uniform(100,200),
            'Average':random.uniform(200,300),
            'Above Average':random.uniform(300,400),
            'Ideal':random.uniform(400,600)
        },
        'Carrots': {
            'Poor':random.uniform(0,200), 
            'Below average':random.uniform(200,400),
            'Average':random.uniform(400,600),
            'Above Average':random.uniform(600,800), 
            'Ideal':random.uniform(800,1000)
        },
        'Lemon': {
            'Poor':random.uniform(0,100), 
            'Below average':random.uniform(100,200), 
            'Average':random.uniform(200,300),
            'Above Average':random.uniform(300,400),
            'Ideal':random.uniform(400,500),
        },
        'Apples': {
            'Poor':random.uniform(0,100), 
            'Below average':random.uniform(100,200),
            'Average':random.uniform(200,300),
            'Above Average':random.uniform(300,400),
            'Ideal':random.uniform(400,500)
        }

    },
    'change_land' : {-0.15,-0.1 ,-0.05,0,0.05,0.10,0.15} #the pecentages of changes

}
