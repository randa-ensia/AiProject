class Node:
    def __init__(self, state, parent=None, action=None, cost=0, heuristic_cost=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.cost = cost
        self.heuristic_cost = heuristic_cost
        if parent is None:
            self.depth = 0
        else:
            self.depth = parent.depth + 1

    def total_cost(self):
        return self.cost + self.heuristic_cost

    def __hash__(self):
        hashable = tuple(self.state)
        #print(type(hashable))
        return hash(hashable) #because dict are not hashable make it a tuple to hash it
    def __str__(self):
        return str(self.state)

    def __eq__(self, other):
        return self.state == other.state

    def __lt__(self, other):
        return self.total_cost() < other.total_cost()