class Node:
    def __init__(self, state, parent=None, action=None, cost=0):
        self.state = state
        self.parent = parent # node
        self.action = action # action performed to get to this node
        self.cost = cost # (incremented with each newly expanded node)
        if parent is None: # root node
            self.depth = 0 # level in the graph 0 for the root node
        else:
            self.depth = parent.depth + 1 # parent level + 1
    def __hash__(self):
       return hash(tuple (map (tuple ,self.state)))
    def __eq__(self, other):
        if  self.state == other.state :
            return True
        else :
            return False