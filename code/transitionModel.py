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



    def transition_model_function (self,state, action):  #shouldn't we define this outside of the class and assign it??
        """
        This function takes a state and an action as parameters and returns the state that will result from applying
        that action

        It will be used to expand the nodes in the search algorithms
        """

        #a dictionnary to map each condition with the equivalent productivity
        map_production_condition  = { 'change conditions ':{
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

    }

    }
        
        #a dictionnary for the yearly prices of vegetables acording to their production
        prices_production = {
    'Potatoes': lambda x: -7066 + 0.0038*x - 0.000000000861*x**2 + 0.0000000000000109*x**3 - 0.00000000000000000000848*x**4 + 0.0000000000000000000000429*x**5 - 0.0000000000000000000000000143*x**6 + 0.000000000000000000000000000312*x**7 - 0.000000000000000000000000000000428*x**8 + 0.000000000000000000000000000000000334*x**9 - 0.00000000000000000000000000000000000113*x**10,
    'Tomatoes': lambda x: -26463 + 0.0312*x - 0.0000000159*x**2 + 0.0000000000000458*x**3 - 0.0000000000000000000827*x**4 + 0.0000000000000000000000973*x**5 - 0.000000000000000000000000075*x**6 + 0.000000000000000000000000000369*x**7 - 0.00000000000000000000000000108*x**8 + 0.00000000000000000000000000000000000000000000159*x**9 - 0.00000000000000000000000000000000000718*x**10,
    'Carrots': lambda x: 2780000 - 8.54*x + 0.0000117*x**2 - 0.00000000000931*x**3 + 0.00000000000000000481*x**4 - 0.000000000000000000000168*x**5 + 0.000000000000000000000000404*x**6 - 0.000000000000000000000000000655*x**7 + 0.000000000000000000000000000000689*x**8 - 0.00000000000000000000000000000000424*x**9 + 0.0000000000000000000000000000000000116*x**10,
    'Lemon': lambda x: -1250000 + 28.1*x - 0.000272*x**2 + 0.00000000015*x**3 - 0.00000000000000524*x**4 + 0.0000000000000000000122*x**5 - 0.0000000000000000000000193*x**6 + 0.000000000000000000000000205*x**7 - 0.00000000000000000000000000000000000000000000000000000154*x**10,
    'Dates': lambda x: 303 - 0.000102*x + 0.000000000022*x**2 - 0.00000000000000000101*x**3,
    'Green Pepper': lambda x: -9793 + 0.0232*x - 0.0000000228*x**2 + 0.000000000000123*x**3 - 0.000000000000000000004*x**4 + 0.0000000000000000000000801*x**5 - 0.000000000000000000000000097*x**6 + 0.000000000000000000000000000651*x**7 - 0.0000000000000000000000000000186*x**8,
    'Onions': lambda x: -210 + 0.268*x - 0.000101*x**2 + 0.0000000142*x**3 - 0.000000000000275*x**4,
    'Corn': lambda x: 17.6 + 0.000263*x - 0.0000000125*x**2 + 0.000000000000182*x**3 - 0.000000000000000644*x**4,
    'Aubergines': lambda x: 18103 - 0.153*x + 0.000000553*x**2 - 0.00000000000112*x**3 + 0.00000000000000000137*x**4 - 0.00000000000000000000105*x**5 + 0.00000000000000000000000489*x**6 - 0.0000000000000000000000000127*x**7 + 0.000000000000000000000000000000000000000000000000000000000000000000000000014*x**8 + 0.00000000000000000000000000000000000000000000000000000000014*x**9

        }

        new_state = copy.deepcopy(state) #the new state that we are going to apply the action to and return (ask fatima if we need to make the copy)

        (wilaya,product,condition,land) = action 

        #total surface = unused surface + cultivated surface + terre en repo surface
        total_surface = new_state['wilayas'][wilaya]['Land_data']['unused land'] + new_state['wilayas'][wilaya]['Land_data']['cultivated land'] + new_state['wilayas'][wilaya]['Land_data']['terre_au_repo']

        #unused land = unused land - total_surface * percentage
        new_state['wilayas'][wilaya]['Land_data']['unused land'] = new_state['wilayas'][wilaya]['Land_data']['unused land'] - land* total_surface

        #cultivated land = cultivated land + total_surface * percentage
        new_state['wilayas'][wilaya]['Land_data']['cultivated land'] = new_state['wilayas'][wilaya]['Land_data']['cultivated land'] + land* total_surface
        
        new_state['wilayas'][wilaya]['Products'][product]['condition'] = condition

        new_state['wilayas'][wilaya]['Products'][product]['productivity'] = map_production_condition['change conditions '][product][condition]
        new_state['wilayas'][wilaya]['Products'][product]['lands_surface'] = new_state['wilayas'][wilaya]['Products'][product]['lands_surface'] + total_surface*land

        #production = productivty * land surface
        new_state['wilayas'][wilaya]['Products'][product]['production'] = new_state['wilayas'][wilaya]['Products'][product]['productivity'] * new_state['wilayas'][wilaya]['Products'][product]['lands_surface']

        new_state['prices'][product] = prices_production[product][new_state['wilayas'][wilaya]['Products'][product]['production']];

        return new_state
    
    
    #def get_valid_actions:

    
                    

