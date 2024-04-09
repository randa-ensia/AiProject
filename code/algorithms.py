from queue import PriorityQueue
from problemFormalization import node as n

def SearchStrategies(problem,strategy):
    explored = set()
    complexity = 0
    frontier_states = set()
    frontier = PriorityQueue()
    frontier.put(n.Node(problem.state))
    while frontier.qsize():
        ele = frontier.get()
        if problem.is_goal_test(ele):
            # Backtrack to construct the path and calculate cost
            path = []
            cost = ele.total_cost ()
            while ele.parent:
                path.append(ele.state)
                ele = ele.parent
            path.append(ele.state)  # Adding the initial state
            path.reverse()
            return path, cost ,complexity
        else:
            explored.add(ele.state)
            children = problem.expand_node(ele,strategy)
            complexity += 1 
            if children:
                for child in children:
                    if child.state not in explored and child.state not in frontier_states:
                        frontier.put(child)
                        frontier_states.add(child.state)
                    elif any(n.state == child.state and n.total_cost() > child.total_cost() for n in frontier.queue):
                        # Update the priority of the existing node with the same state as the child
                        for existing_node in frontier.queue:
                            if existing_node.state == child.state and existing_node.total_cost ()> child.total_cost() :
                                frontier.queue.remove(existing_node)
                                frontier.put(child)
                                break
    return None