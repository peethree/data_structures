class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):                   
        # If vertex u is already a key in the dictionary, add v to u's set.
        if u in self.graph:
            self.graph[u].add(v)
            
        # Otherwise, create a new set for u that contains v
        # my_set = {1, 2, 3, 4}
        else:
            self.graph[u] = {v}

        # same for v
        if v in self.graph:
            self.graph[v].add(u)
        else:
            self.graph[v] = {u}
            

    def edge_exists(self, u, v):
        if u in self.graph and v in self.graph:
            return (v in self.graph[u]) and (u in self.graph[v])
        return False
