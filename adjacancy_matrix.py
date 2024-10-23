class Graph:
    def __init__(self, num_vertices):
        self.graph = []

        # num_vertices = 3        
        # [[false, false, false],
        # [false, false, false],
        # [false, false, false]]

        # Fill the list with n lists, where n is the number of vertices in the graph. 
        # Each of these lists should contain n False values.
        for i in range(num_vertices):
            row = []
            for j in range(num_vertices):
                row.append(False)
            self.graph.append(row)           
        

    def add_edge(self, u, v):
        # add_edge takes two vertices as inputs, 
        # and should add an edge to the graph by setting the corresponding cells to True
        self.graph[u][v] = True
        self.graph[v][u] = True

   

    def edge_exists(self, u, v):
        if u < 0 or u >= len(self.graph):
            return False
        if len(self.graph) == 0:
            return False
        row1 = self.graph[0]
        if v < 0 or v >= len(row1):
            return False
        return self.graph[u][v]
