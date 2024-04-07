"""
this file will contains the agriculture class that implements our formalization of the problem

NOTE:
besmala used the transition model with conditions in lower cases , don't forget to change this
in the actions file
"""

from transitionModel import conditionsProductivity, prices
from pathCost import pathCostHelper

import copy
import node as N

class agriculture:
       def __init__(self,initial_state,actions,transition_model,path_cost,goal_test):
              self.initial_state = initial_state
              self.actions = actions
              self.transition_model = transition_model
              self.path_cost = path_cost
              self.goal_test = goal_test
      
               
       def goal_test(self,state):
              consumption = state['consumption']
    # Check for self-sufficiency
              total_production = self.calcTotalProduction(state)
              for crop in state['consumption'].items():
                     if   total_production[crop]-consumption[crop] < 0:
                            print("There is not self-sufficiency for", crop)
                            return False  # Not self-sufficient for this crop
                     else:
                            print("There is a self-sufficiency for", crop)
            
    
    # Check for lowest price
              for crop, details in state['prices'].items():
                     average_price = details['average']
                     current_price = details['current']

        # Check if current price is within ±2% of the average price
                     if not (0.98 * average_price <= current_price <= 1.02 * average_price):
                            print("The price of", crop, "is not within ±2% of the average price")
                            return False  # Current price is not within the range
                     else:
                            print("The price of", crop, "is within ±2% of the average price ")
                            print("so  lowest price of ", crop, "is ",current_price ,'DA')

              return True

       def expand_node(self, node):#NOT TESTED
              state = node.state
              valid_actions = self.get_valid_actions(state)
              child_nodes = []
              for action in valid_actions:
                     child_state = self.transition_model(state, action)
                     child_node = N.Node(child_state, parent=node, action=action, cost=node.cost + self.path_cost(node.state,action))
                     child_nodes.append(child_node)
              return child_nodes
       


       ###helper functions####
       #remove the actions that leads to the same state
       def get_valid_actions(self,state):#NOT TESTED
              """
              this is a helper function to be used inside of the expand node to get all the possible actions then
              applying them
              """
              valid_actions = []

        # Iterate over each wilaya
              for wilaya in self.state['wilayas']:
                     wilaya_data = self.state['wilayas'][wilaya]
                     available_land = wilaya_data['Land_data']['unused land']
                     total_surface = wilaya_data['Land_data']['unused land']+wilaya_data['Land_data']['culivated land']+wilaya_data['Land_data']['terre au repos']
                     for action in self.actions:
                            (wilaya,product,_,land) = action
                            if available_land >= land* total_surface and state['wilayas'][wilaya][product]['production']> 0 :
                                   valid_actions.append(action)
              return valid_actions
       # Calculate total production of each product in the entire country
       def calcTotalProduction(state):
        total_production = {product: 0 for product in state['wilayas']['ADRAR']['Products']}#it is a dict of production for all the products
        for wilaya in state['wilayas'].values():
            for product, details in wilaya['Products'].items():#looping over the products of each wilaya
                total_production[product] += details['production']#calculate the total production of a product for all wilayas
                
        # print("Total production of each product:") ==> this is for testing !
        # for product, production in total_production.items():
        #     print(f"{product}: {production}")    
        return total_production


#the path cost function
def step_cost(state,action):#this function was tested
       """
       This function calculates the cost of going from one step to an other
       it takes the state and the actions we want to calculate its cost as a parameter
       it will be used in the expand node function to determine the path costs of each node
       """
       return pathCostHelper.calculate_condition_change_cost(action,state) + pathCostHelper.calculate_land_change_cost(action,state)


#the transition model
def transition_model_function (state, action): #this function was tested
    """
    This function takes a state and an action as parameters and returns the state that will result from applying
    that action
    It will be used to expand the nodes in the search algorithms
    """

    resulting_state = copy.deepcopy(state) #the new state that we are going to apply the action to and return 
    (wilaya,product,condition,land) = action 

    #total surface = unused surface + cultivated surface + terre en repo surface
    total_surface = resulting_state['wilayas'][wilaya]['Land_data']['unused land'] + resulting_state['wilayas'][wilaya]['Land_data']['cultivated land'] + resulting_state['wilayas'][wilaya]['Land_data']['terre_au_repo']

    #unused land = unused land - total_surface * percentage
    resulting_state['wilayas'][wilaya]['Land_data']['unused land'] = resulting_state['wilayas'][wilaya]['Land_data']['unused land'] - land* total_surface

    #cultivated land = cultivated land + total_surface * percentage
    resulting_state['wilayas'][wilaya]['Land_data']['cultivated land'] = resulting_state['wilayas'][wilaya]['Land_data']['cultivated land'] + land* total_surface

    #assigning the new condition to the state
    resulting_state['wilayas'][wilaya]['Products'][product]['condition'] = condition

    #calculating the productivity using the condutions and assigning it
    resulting_state['wilayas'][wilaya]['Products'][product]['productivity'] = conditionsProductivity.map_condition_productivity[product][condition]

    #the new surface used to plant the crop
    resulting_state['wilayas'][wilaya]['Products'][product]['lands_surface'] = resulting_state['wilayas'][wilaya]['Products'][product]['lands_surface'] + total_surface*land

    #production = productivty * land surface
    resulting_state['wilayas'][wilaya]['Products'][product]['production'] = resulting_state['wilayas'][wilaya]['Products'][product]['productivity'] * resulting_state['wilayas'][wilaya]['Products'][product]['lands_surface']

    #calculating the new price of the crop according to the changement of the production
    resulting_state['prices'][product] = prices.prices_production[product](resulting_state['wilayas'][wilaya]['Products'][product]['production'])

    return resulting_state
    