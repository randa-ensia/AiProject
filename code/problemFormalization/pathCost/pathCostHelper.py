"""
this file contains two helper functions used to calculate the path cost.

according to the actions we defined there are three types of actions:
    *actions that changes the conditions used to plant the crops
    *actions that changes the surface of land used to plant the crops

so we will define two functions : a function to calculate the cost of changing the conditions and a function that
calculates the cost of chaning the surface
and our step cost will be the sum of both functions
"""
from pathCost import pathCostFactors

#function used to calculate the cost of chaning the condition
def  calculate_condition_change_cost(action , state):
    (wilaya,product,condition,_) = action
    #print(wilaya);
    #print(product);
    cost = state['wilayas'][wilaya]['Products'][product]['cost'] #the cost of plating in a given wilaya
    old_condition = state['wilayas'][wilaya]['Products'][product]['condition']#the original condition of the state

    if old_condition == condition:#if we didn't change the condition the cost will be 0
        return 0;

    wilaya_climate=pathCostFactors.wilaya_to_climate[wilaya]
    suitability=pathCostFactors.product_suitability[wilaya_climate][product]
    #print(old_condition)
    #print(old_condition)
    #print(suitability)
    #print(condition)
    adjustment_factor = pathCostFactors.adjustment_factors[suitability][old_condition][condition]
    
    return cost*adjustment_factor

#function used to calculate the cost of changing the surface of land used to plant
def calculate_land_change_cost(action,state): 
#['ADRAR', 'Potatoes', 'Ideal', 0.15]
    (wilaya,product,condition,percentage) = action
    if percentage <= 0:
        return 0;
    total_surface = state['wilayas'][wilaya]['Land_data']['unused land'] + state['wilayas'][wilaya]['Land_data']['cultivated land'] + state['wilayas'][wilaya]['Land_data']['terre_au_repo']
    addedland_sur = percentage * total_surface
    product,addedland_sur,condition,

    added_cost=addedland_sur*pathCostFactors.cost_per_hec[product]
    return added_cost*pathCostFactors.fixed_factors[condition]

