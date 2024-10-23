class Graph:
    def bfs_path(self, start, end):
        visited = []
        to_visit = [start]
        path = {start: None}
        
        while to_visit:
            current_vertex = to_visit.pop(0)
            visited.append(current_vertex)

            # if the end is reached
            if current_vertex == end:                
                path_list = []
                
                # work backwards to get the shortest path
                while current_vertex is not None:
                    path_list.append(current_vertex)
                    # set the current vertex to its parent
                    current_vertex = path[current_vertex]
                # reverse the order
                path_list.reverse()
                return path_list

            sorted_neighbors = sorted(self.graph[current_vertex])
            
            for neighbor in sorted_neighbors:
                if neighbor not in visited and neighbor not in to_visit:
                    to_visit.append(neighbor)
                    path[neighbor] = current_vertex                    
        return None

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
    

run_cases = [
    (
        [
            ("New York", "London"),
            ("New York", "Cairo"),
            ("New York", "Tokyo"),
            ("London", "Dubai"),
            ("Cairo", "Kyiv"),
            ("Cairo", "Madrid"),
            ("London", "Madrid"),
            ("Buenos Aires", "New York"),
            ("Tokyo", "Buenos Aires"),
            ("Kyiv", "San Francisco"),
        ],
        "Cairo",
        "San Francisco",
        ["Cairo", "Kyiv", "San Francisco"],
    ),
    (
        [
            ("Oslo", "Bergen"),
            ("Oslo", "Trondheim"),
            ("Bergen", "Trondheim"),
            ("Edinburgh", "London"),
            ("Edinburgh", "Bristol"),
            ("London", "Bristol"),
        ],
        "Oslo",
        "Edinburgh",
        None,
    ),
    (
        [
            ("New York", "London"),
            ("New York", "Cairo"),
            ("New York", "Tokyo"),
            ("London", "Dubai"),
            ("Cairo", "Kyiv"),
            ("Cairo", "Madrid"),
            ("London", "Madrid"),
            ("Buenos Aires", "New York"),
            ("Tokyo", "Buenos Aires"),
            ("Kyiv", "San Francisco"),
        ],
        "New York",
        "Dubai",
        ["New York", "London", "Dubai"],
    ),
]
submit_cases = run_cases + [
    (
        [
            ("Los Angeles", "Paris"),
            ("Los Angeles", "Istanbul"),
            ("Los Angeles", "Shanghai"),
            ("Paris", "Singapore"),
            ("Istanbul", "Rome"),
            ("Paris", "Rome"),
            ("Rome", "Seattle"),
            ("Sydney", "Los Angeles"),
            ("Shanghai", "Sydney"),
            ("Sydney", "Cairo"),
            ("Cairo", "Seattle"),
        ],
        "Los Angeles",
        "Seattle",
        ["Los Angeles", "Istanbul", "Rome", "Seattle"],
    ),
    (
        [
            ("Los Angeles", "Istanbul"),
            ("Los Angeles", "Shanghai"),
            ("Paris", "Singapore"),
            ("Istanbul", "Rome"),
            ("Paris", "Rome"),
            ("Rome", "Seattle"),
            ("Sydney", "Los Angeles"),
            ("Shanghai", "Sydney"),
            ("Sydney", "Cairo"),
            ("Cairo", "Seattle"),
            ("Seattle", "Tokyo"),
            ("Tokyo", "Shanghai"),
            ("Istanbul", "Cairo"),
            ("Rome", "Berlin"),
            ("Berlin", "Paris"),
            ("Singapore", "Sydney"),
            ("Cairo", "Istanbul"),
            ("Berlin", "Tokyo"),
        ],
        "Los Angeles",
        "Berlin",
        ["Los Angeles", "Istanbul", "Rome", "Berlin"],
    ),
]


def test(edges_to_add, from_vertex, to_vertex, expected_path):
    print("=================================")
    graph = Graph()
    for edge in edges_to_add:
        graph.add_edge(edge[0], edge[1])
        print(f"Added edge: {edge}")
    print("---------------------------------")
    try:
        print(f"Path from {from_vertex} to {to_vertex}")
        path = graph.bfs_path(from_vertex, to_vertex)
        print(f" - Expecting: {expected_path}")
        print(f" - Actual: {path}")

        if path == expected_path:
            print("Pass \n")
            return True
        print("Fail \n")
        return False
    except Exception as e:
        print(f"Error: {e}")
        return False


def main():
    passed = 0
    failed = 0
    for test_case in test_cases:
        correct = test(*test_case)
        if correct:
            passed += 1
        else:
            failed += 1
    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")
    print(f"{passed} passed, {failed} failed")


test_cases = submit_cases
if "__RUN__" in globals():
    test_cases = run_cases

main()
