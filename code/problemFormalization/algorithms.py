from queue import PriorityQueue
import node as n

def SearchStrategies(problem, strategy_used): #strategy_used tell if it is informed or not
    """
    this function is an implementation of the two searching algorithms A* and UCS
    to use it for A* pass 'A' as a parameter to strategy_used
    to use UCS pass 'U'
    """
    if strategy_used != 'A' and strategy_used != 'U':
        raise ValueError('invalid parameter in the strategy used')
    
    explored = set() 
    frontier = PriorityQueue()
    #because PriorityQueue is not iteratable

    frontier.put(n.Node(problem.initial_state))# initializing the frontier with the initial state of the problem

    while frontier.qsize():#while frontier isn't empty
        ele = frontier.get() #ele is the node to be explored/expanded


        if problem.goal_test(ele.state): 
            return ele
        
        else:
            explored.add(ele)
            children = problem.expand_node(ele)


            if children: 
                for child in children:
            
                    if strategy_used == 'A':
                        child.cost += problem.heuristic (child.state)#adding the heuristic h to the path cost to get the evaluation function

                    if child not in explored and child not in frontier.queue:#for graph search
                        frontier.put(child)

                        
                    elif any(n.state == child.state and n.cost > child.cost for n in frontier.queue):
                        # Update the priority of the existing node with the same state as the child
                        for existing_node in frontier.queue:
                            if existing_node.state == child.state and existing_node.cost > child.cost:
                                frontier.queue.remove(existing_node)
                                frontier.put(child)
                                break


    return None