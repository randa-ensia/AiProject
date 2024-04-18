"""
this file will contains the agriculture class that implements our formalization of the problem

NOTE:
besmala used the transition model with conditions in lower cases , don't forget to change this
in the actions file
"""

from transitionModel import conditionsProductivity, prices
from pathCost import pathCostHelper
from pathCost import pathCostFactors
from goalTest import goalTestHelper

import copy
import node as N

class agriculture:
       def __init__(self,initial_state,actions,transition_model,path_cost,goal_test):
              self.initial_state = initial_state
              self.actions = actions
              self.transition_model = transition_model
              self.path_cost = path_cost
              self.goal_test = goal_test
      
               
       def is_goal_test(self,state):
              return self.goal_test(state)
            

       def expand_node(self, node):#NOT TESTED
              state = node.state
              valid_actions = self.get_valid_actions(state)
              child_nodes = []
              for action in valid_actions:
                     child_state = self.transition_model(state, action)
                     child_node = N.Node(child_state, parent=node, action=action, cost=node.cost + self.path_cost(node.state,action))
                     child_nodes.append(child_node)
              return child_nodes
       #didn't check it logic
       def heuristic(self, state):

              total_cost = 0
              #Define a dectionary to keep track fo the products total production across different wilayas first initialised to 0
              total_production = {product: 0 for product in pathCostFactors.max_idealproductivity} 
              for _, data in state['wilayas'].items():
                     for product, details in data['Products'].items():
                            total_production[product]+=details['production']
              #for each product find the cost and add it to total
              for product,details in total_production.items():
                     total_cost+=self.product_cost(product, total_production[product], self.initial_state['consumption'][product]) #I assumed that the consumption in a dictionary
    
              return total_cost

       ###helper functions####
       def get_valid_actions(self,state):#TESTED
              """
              this is a helper function to be used inside of the expand node to get all the possible actions then
              applying them
              """
              valid_actions = []
              for action in self.actions:
                     (wilaya,product,condition,land) = action
                     wilaya_data = state['wilayas'][wilaya]
                     available_land = wilaya_data['Land_data']['unused land']
                     total_surface = available_land + wilaya_data['Land_data']['cultivated land'] + wilaya_data['Land_data']['terre_au_repo']
                     if available_land >= land * total_surface and state['wilayas'][wilaya]['Products'][product]['production']> 0 and land!=0 and condition != state['wilayas'][wilaya]['Products'][product]['condition']:
                            valid_actions.append(action)
              #print(valid_actions)
              return valid_actions
       
       def product_cost(self,product,production,consumption):#I didn't check its logic
              return (consumption-production)/pathCostFactors.max_idealproductivity[product]*pathCostFactors.cost_per_hec[product]*pathCostFactors.fixed_factors['ideal']




#the path cost function
def step_cost(state,action):#TESTED
       """
       This function calculates the cost of going from one step to an other
       it takes the state and the actions we want to calculate its cost as a parameter
       it will be used in the expand node function to determine the path costs of each node
       """
       return pathCostHelper.calculate_condition_change_cost(action,state) + pathCostHelper.calculate_land_change_cost(action,state)


#the transition model
def transition_model_function (state, action): #TESTED
    """
    This function takes a state and an action as parameters and returns the state that will result from applying
    that action
    It will be used to expand the nodes in the search algorithms
    """

    resulting_state = copy.deepcopy(state) #the new state that we are going to apply the action to and return 
    (wilaya,product,condition,land) = action 
    #print(action)

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

    #changing the cost
    resulting_state['wilayas'][wilaya]['Products'][product]['cost'] = resulting_state['wilayas'][wilaya]['Products'][product]['lands_surface'] * pathCostFactors.cost_per_hec[product]

    #calculating the new price of the crop according to the changement of the production
    resulting_state['prices'][product]['current'] = prices.prices_production[product](resulting_state['wilayas'][wilaya]['Products'][product]['production'])

    return resulting_state

#goal test function
def goal_test(state):
       is_self_suff = True;
       consumption = state['consumption']
    # Check for self-sufficienc
       total_production = goalTestHelper.calcTotalProduction(state)
       for crop in state['consumption']:
              #print(crop,total_production[crop]-consumption[crop])
              #print('crop',crop) debugiing purposes
              if   total_production[crop]-consumption[crop] < -5000:
                     #print("There is not self-sufficiency for", crop)
                     is_self_suff = False
                     #return False  # Not self-sufficient for this crop
              #else:
                     #print("There is a self-sufficiency for", crop)
                     #return True
            
    
    # Check for lowest price
       #for crop, details in state['prices'].items():
              #average_price = details['average']
              #current_price = details['current']

        # Check if current price is within ±2% of the average price
              #if not (0.85 * average_price <= current_price <= 1.15 * average_price):
                     #print("The price of", crop, "is not within ±2% of the average price")
                     #return False  # Current price is not within the range
              #else:
                     #print("The price of", crop, "is within ±2% of the average price ")
                     #print("so  lowest price of ", crop, "is ",current_price ,'DA')


       return is_self_suff
#
    