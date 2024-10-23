class Graph:
    def adjacent_nodes(self, node):
        # print(self.graph)
        # {0: {2}, 2: {0, 1, 4}, 4: {2, 5}, 1: {2, 3}, 3: {1}, 5: {4}}        

        adjacent = []
        # if the node value is a value under a key, return all the keys
        for key in self.graph.keys():            
            if node in self.graph[key]:
                adjacent.append(key)
        return sorted(adjacent)


    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u in self.graph:
            self.graph[u].add(v)
        else:
            self.graph[u] = {v}
        if v in self.graph:
            self.graph[v].add(u)
        else:
            self.graph[v] = {u}
