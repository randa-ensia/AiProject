from queue import PriorityQueue
from queue import LifoQueue
import node as n

def SearchStrategies(problem, isInformed, isGreedy, cost_limit = float('inf'), DSA = LifoQueue(),strategy = "UCS"): #strategy_used tell if it is informed or not
    """
    this function is an implementation of the two searching algorithms A* and best first search
    """
    
    explored = set() 
    frontier = DSA
    explored_nodes = 0 #variable used to count number of explored nodes
    #because PriorityQueue is not iteratable
    min = float('inf')

    frontier.put(n.Node(problem.initial_state))# initializing the frontier with the initial state of the problem

    while frontier.qsize():#while frontier isn't empty
        print("number of explored nodes:\t",explored_nodes)
        ele = frontier.get() #ele is the node to be explored/expanded
        explored_nodes = explored_nodes + 1


        if problem.goal_test(ele.state): 
            print("Cost of the solution node:\t",ele.cost)
            print("Depth of the solution node:\t",ele.depth)
            print("Number of steps (explored nodes) leading to the solution node:\t",explored_nodes)
            return ele
        
        elif ele.evaluation_function > cost_limit:
            if ele.evaluation_function < min:
                min = ele.evaluation_function
        else:
            children = problem.expand_node(ele)
            if children: 
                for child in children:
            
                    if isGreedy:
                        child.evaluation_function = problem.heuristic(child)#chanding the cost for best best search into the heuristic only
                    elif isInformed and not isGreedy:
                        child.evaluation_function = problem.heuristic(child) + child.cost#adding the heuristic to the cost for A*  

                    elif not isGreedy and not isInformed:
                        child.evaluation_function = child.cost

                    if child not in explored and child not in frontier.queue :#for graph search
                        frontier.put(child)

                    if strategy == "UCS" or strategy == "A*":
                        if any(n.state == child.state and n.cost > child.cost for n in frontier.queue):
                            # Update the priority of the existing node with the same state as the child
                            for existing_node in frontier.queue:
                                if existing_node.state == child.state and existing_node.cost > child.cost:
                                    frontier.queue.remove(existing_node)
                                    frontier.put(child)
                                    break

        explored.add(ele)
        

    return min

def limitesSearchStrategy(problem,isInformed,isGreedy,cost_limit):
    solution = None
    cost_limit = 200
    while solution == None:
        response = SearchStrategies(problem,isInformed,isGreedy,cost_limit,LifoQueue())
        
        if isinstance(response,int):
            print(response)
            cost_limit = response
        else:
            solution = response
    return response