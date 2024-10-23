class Graph:
    def depth_first_search(self, start_vertex):
        # Create an empty visited list
        visited = []
        # Call depth_first_search_r with the empty list and the start vertex
        self.depth_first_search_r(visited, start_vertex)
        # Return the visited array after depth_first_search_r has mutated it
        return visited

    def depth_first_search_r(self, visited, current_vertex):
        # Visit the current vertex by adding it to the visited list
        visited.append(current_vertex)

        # Get a sorted list of the neighbors of the current vertex using the sorted() function
        sorted_neighbors = sorted(self.graph[current_vertex])

        for neighbor in sorted_neighbors:
            # If the neighboring vertex hasn't been visited yet, visit it 
            # by recursively calling depth_first_search_r with the neighboring vertex
            if neighbor not in visited:
                self.depth_first_search_r(visited, neighbor)

        

    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u in self.graph.keys():
            self.graph[u].add(v)
        else:
            self.graph[u] = set([v])
        if v in self.graph.keys():
            self.graph[v].add(u)
        else:
            self.graph[v] = set([u])

    def __repr__(self):
        result = ""
        for key in self.graph.keys():
            result += f"Vertex: '{key}'\n"
            for v in sorted(self.graph[key]):
                result += f"has an edge leading to --> {v} \n"
        return result
