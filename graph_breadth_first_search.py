class Graph:
    def breadth_first_search(self, v):
        visited = []
        to_visit = []
        # print(self.graph)
        # {'New York': {'Tokyo', 'Cairo', 'London'}, 
        # 'London': {'New York', 'Dubai'}, 
        # 'Cairo': {'New York'}, 
        # 'Tokyo': {'New York'}, 
        # 'Dubai': {'London'}}

        # Queue up the start vertex by adding it to the to_visit list.
        to_visit.append(v)               
        
        while len(to_visit) != 0:
            # Remove the first vertex off the to_visit list with pop and visit it by appending it to visited.
            visit = to_visit.pop(0)
            visited.append(visit)

            # neighbors are the countries directly connected (by an edge)
            # so in New york's case: tokyo, cairo and london

            # Get a sorted() list of the neighbors of the vertex we just visited
            sorted_neighbors = sorted(self.graph[visit])

            # For each sorted neighbor:
            for neighbor in sorted_neighbors:
                # If the neighbor hasn't been visited and it isn't already queued up to be visited:
                if neighbor not in visited and neighbor not in to_visit:
                    # Queue up the neighbor by adding it to the to_visit loop.
                    to_visit.append(neighbor)
                    
        return visited


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
