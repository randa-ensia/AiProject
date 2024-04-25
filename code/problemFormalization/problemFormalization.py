"""
this file will contains the agriculture class that implements our formalization of the problem

NOTE:
besmala used the transition model with conditions in lower cases , don't forget to change this
in the actions file
"""

from transitionModel import conditionsProductivity, prices, getProductsOfWilaya
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
              total_production = state["total_production"]
              #for each product find the cost and add it to total
              for product,_ in total_production.items():
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
                     (product,_,wilaya) = action

                     wilaya_data = state['wilayas'][wilaya]
                     available_land = wilaya_data['Land_data']['unused land']

                     if available_land > 0 and state["consumption"][product] - state["total_production"][product] > 0:
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

       cost = pathCostHelper.calculate_condition_change_cost(action,state) + pathCostHelper.calculate_land_change_cost(action,state) 

       return cost / state["total_production"][action[0]]

#the transition model
def transition_model_function (state, action): #TESTED
    """
    This function takes a state and an action as parameters and returns the state that will result from applying
    that action
    It will be used to expand the nodes in the search algorithms
    """

    resulting_state = copy.deepcopy(state) #the new state that we are going to apply the action to and return 
    (product,condition,wilaya) = action 
    #product,condition ,wilaya
    #print(action) productivoty (if I changed condition, production , surface maghroussa, unsed land)

    #total surface = unused surface + cultivated surface + terre en repo surface
    #total_surface = resulting_state['wilayas'][wilaya]['Land_data']['unused land'] + resulting_state['wilayas'][wilaya]['Land_data']['cultivated land'] + resulting_state['wilayas'][wilaya]['Land_data']['terre_au_repo']

    #unused land = unused land - total_surface * percentage

    #

    #I calculate the ratio between the need of a product and the sum of the needs of all products in the wilaya

    need_of_product = resulting_state["consumption"][product] - resulting_state["total_production"][product]
    need_all_products_wilaya = 0 


    for p in getProductsOfWilaya.algerian_crops[wilaya]:
           diffrence = resulting_state["consumption"][p] - resulting_state["total_production"][p]
           if diffrence > 0 :
              need_all_products_wilaya  = need_all_products_wilaya  + diffrence
    ratio = need_of_product / need_all_products_wilaya

    #calculate how much land will I cultivate
    cultivated_land_product = ratio*resulting_state['wilayas'][wilaya]['Land_data']['unused land']


    #the land surface
    resulting_state['wilayas'][wilaya]['Products'][product]['lands_surface'] = resulting_state['wilayas'][wilaya]['Products'][product]['lands_surface'] + cultivated_land_product

    #the unsed land
    resulting_state['wilayas'][wilaya]['Land_data']['unused land'] = resulting_state['wilayas'][wilaya]['Land_data']['unused land'] - cultivated_land_product


    #cultivated land = cultivated land + total_surface * percentage
    resulting_state['wilayas'][wilaya]['Land_data']['cultivated land'] = resulting_state['wilayas'][wilaya]['Land_data']['cultivated land'] + cultivated_land_product

    #assigning the new condition to the state
    resulting_state['wilayas'][wilaya]['Products'][product]['condition'] = condition

    #calculating the productivity using the conditions and assigning it
    resulting_state['wilayas'][wilaya]['Products'][product]['productivity'] = conditionsProductivity.map_condition_productivity[product][condition]



    #production = productivty * land surface
    old_production = resulting_state['wilayas'][wilaya]['Products'][product]['production']
    resulting_state['wilayas'][wilaya]['Products'][product]['production'] = resulting_state['wilayas'][wilaya]['Products'][product]['productivity'] * resulting_state['wilayas'][wilaya]['Products'][product]['lands_surface']

    #changing the cost
    resulting_state['wilayas'][wilaya]['Products'][product]['cost'] = resulting_state['wilayas'][wilaya]['Products'][product]['lands_surface'] * pathCostFactors.cost_per_hec[product]

    #calculating the new price of the crop according to the changement of the production
    resulting_state['prices'][product]['current'] = prices.prices_production[product](resulting_state['wilayas'][wilaya]['Products'][product]['production'])

    #calculating new production
    resulting_state['total_production'][product] = resulting_state['total_production'][product] - old_production + resulting_state['wilayas'][wilaya]['Products'][product]['production']

    return resulting_state

#goal test function
def goal_test(state):
       is_self_suff = True;
       consumption = state['consumption']
    # Check for self-sufficienc
       total_production = state['total_production']
       for crop in state['consumption']:
              #print(crop,total_production[crop]-consumption[crop])
              #print('crop',crop) debugiing purposes
              if   total_production[crop]-consumption[crop] < -50000:
                     print("There is not self-sufficiency for", crop)
                     is_self_suff = False
                     #return False  # Not self-sufficient for this crop
              else:
                     print("There is a self-sufficiency for", crop)
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
    