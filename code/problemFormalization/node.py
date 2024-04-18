class Node:
    def __init__(self, state, parent=None, action=None, cost=0, total_cost = 0):
        self.state = state
        self.parent = parent
        self.action = action
        self.cost = cost
        self.total_cost = total_cost
        if parent is None:
            self.depth = 0
        else:
            self.depth = parent.depth + 1


    def __hash__(self):
        return self.state
        #print(type(hashable))
    
    def __str__(self):
        return str(self.state)

    def __eq__(self, other):
        return self.state == other.state

    def __lt__(self, other):
        return self.cost < other.cost