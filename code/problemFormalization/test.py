import problemFormalization as pF
import initialstate as init
from actions import actions
import algorithms
from queue import Queue

myQ =Queue()

object = pF.agriculture(init.state,actions.ACTIONS,pF.transition_model_function,pF.step_cost,pF.goal_test);

#print(problemFormalization.transition_model_function(initialstate.state,['ADRAR', 'Potatoes', 'ideal', 0.15]));
#print(problemFormalization.step_cost(initialstate.state,['ADRAR', 'Potatoes', 'ideal', 0.15]))
#print(len(object.get_valid_actions(init.state)));
"""
the goal test function of rania should be passes as a parameter and we should add a function that checks it for the nodes
"""

print(algorithms.SearchStrategies(object,"SAHC"));

