import algorithms
from problemFormalization import problemFormalization as pF
from problemFormalization import initialstate as init
from problemFormalization.actions import actions as ac
from problemFormalization.transitionModel import conditionsProductivity, prices
obj = pF.agriculture(init.state,ac.ACTIONS,pF.transition_model_function,pF.step_cost,pF.goal_test);
algorithms.SearchStrategies(obj,'A')