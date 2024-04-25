from queue import PriorityQueue
from queue import LifoQueue
from queue import Queue
import node as n
import random

def SearchStrategies(problem, strategy = "UCS", cost_limit = float('inf'), DSA = LifoQueue()): #strategy_used tell if it is informed or not
    """
    this function is an implementation of the general graph first search
    """
    print("start");

    root = n.Node(problem.initial_state)

    isInformed = False
    isGreedy = False
    isLocal = False
    DSA = Queue()
    costcum = 0
    initial_total_cost = 0



    if strategy == "BFS":
        DSA = Queue()
    elif strategy == "DFS":
        DSA = LifoQueue()
    elif strategy == "UCS":
        DSA = PriorityQueue()
    elif strategy == "A*":
        DSA = PriorityQueue()
        isInformed = True
        initial_total_cost = problem.heuristic(root)
    elif strategy == "G":
        DSA = PriorityQueue()
        isInformed = True
        isGreedy =  True
        initial_total_cost = problem.heuristic(root)
    elif strategy == "IDA*":
        DSA = LifoQueue()
        isInformed = True
        initial_total_cost = problem.heuristic(root)
    elif strategy == "SAHC":
        DSA = PriorityQueue()
        isLocal = True
        initial_total_cost = problem.heuristic(root)
    elif strategy == "SHC":
        DSA = Queue()
        isLocal = True
        initial_total_cost = problem.heuristic(root)

    else:
        print("start1");
        exit()


    explored = set() 
    frontier = DSA
    explored_nodes = 0 #variable used to count number of explored nodes
    #because PriorityQueue is not iteratable
    min = float('inf')

    frontier.put(root)# initializing the frontier with the initial state of the problem
    root.total_cost = initial_total_cost
    while frontier.qsize():#while frontier isn't empty

        if strategy == "SHC":
            rand = random.randint(0, frontier.qsize() - 1)
            ele = frontier.queue[rand]

            

        else:
            ele = frontier.get() #ele is the node to be explored/expanded

        explored_nodes = explored_nodes + 1


        if problem.goal_test(ele.state): 
            print("Path Cost of the solution node:\t",ele.cost)
            print("Cost used for the search:\t",costcum)
            print("Depth of the solution node:\t",ele.depth)
            print("Number of steps (explored nodes) leading to the solution node:\t",explored_nodes)
            return ele
        
        elif ele.total_cost > cost_limit:
            if ele.total_cost < min:
                min = ele.total_cost
        else: #if I am in a new iteration, empty the frontier if it is a local search get rid of the children of previous nodes
            print("depth: ",ele.depth,"explored node: ",explored_nodes,ele.cost)
            costcum += ele.total_cost
            if isLocal:
                frontier = DSA 
            children = problem.expand_node(ele)
            if children: 
                for child in children:
                    #here we are taking child by child and changing its data accordonly to the strategy..
                    #if it is local search we won't need any of this..

                    if not isLocal: #if it is local search we don't need to know data about the total cost used for informed search
                        if isGreedy:
                            child.total_cost = problem.heuristic(child)#chanding the cost for best best search into the heuristic only
                        elif isInformed and not isGreedy:
                            child.total_cost = problem.heuristic(child) + child.cost#adding the heuristic to the cost for A*  

                        elif not isGreedy and not isInformed:
                            child.total_cost = child.cost
                    else:#if it is local add the objective value as total cost
                        child.total_cost = problem.heuristic(child)
                     

                    #here we are adding the children to the frontier...
                    #if not local, add them, but if it is local remove everything and add the children of that node only already handled above
                    if child not in explored and child not in frontier.queue :#for graph search
                        frontier.put(child)



                    #so this is for UCS and A* include the name of the strategy as a parameter
                    #and after doing that add a condition: is UCS/ is A* for now just disable it for TD..

                    elif any(n.state == child.state and n.cost > child.cost for n in frontier.queue) and strategy == "UCS" or "A*":
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