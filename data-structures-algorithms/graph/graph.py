from collections import deque


class Graph:
    def __init__(self):
        self.adjacency_list = {}

    # Time and Space: O(1)
    def add_vertex(self, vertex):
        if vertex in self.adjacency_list:
            raise Exception("Vertex already in graph")
        self.adjacency_list[vertex] = []
        return self

    # Time and Space: O(1)
    def add_edge(self, vertex1, vertex2):
        if vertex1 not in self.adjacency_list or vertex2 not in self.adjacency_list:
            raise Exception("Invalid vertices")
        self.adjacency_list[vertex1].append(vertex2)
        self.adjacency_list[vertex2].append(vertex1)
        return self

    # Time O(V) (cause iterative list to remove) and Space O(1)
    def remove_edge(self, vertex1, vertex2):
        if vertex1 not in self.adjacency_list or vertex2 not in self.adjacency_list:
            raise Exception("Invalid vertices")
        self.adjacency_list[vertex1].remove(vertex2)
        self.adjacency_list[vertex2].remove(vertex1)
        return

    # Time O(E) and Space O(1)
    def remove_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            raise Exception("Vertex not in graph")
        for neighbor in self.adjacency_list[vertex]:
            self.adjacency_list[neighbor].remove(vertex)
        self.adjacency_list.pop[vertex]
        return self

    # Time Complexity: O(V + E), Space Complexity: O(V)
    def breadth_first_traversal(self, start):
        if start not in self.adjacency_list:
            raise Exception("Vertex not in graph")
        queue = deque([start])
        visited = set()
        traversal_result = []

        while queue:
            vertex = queue.popleft()
            if vertex not in visited:
                traversal_result.append(vertex)
                visited.add(vertex)  # Add vertex to the visited set
                # Add adjacent vertices to the queue
                queue.extend(
                    [vertex for vertex in self.adjacency_list[vertex] if vertex not in visited])
        return traversal_result


graph = Graph()
graph.add_vertex("A")
graph.add_vertex("B")
graph.add_vertex("C")
graph.add_edge("A", "B")
graph.add_edge("B", "C")
print(graph.breadth_first_traversal("A"))  # Expected Output: ["A", "B", "C"]

graph = Graph()
graph.add_vertex("1").add_vertex("2").add_vertex("3")
graph.add_vertex("4").add_vertex("5")
graph.add_edge("1", "2").add_edge("2", "3")
graph.add_edge("4", "5")

print(graph.breadth_first_traversal("1"))  # Expected Output: ["1", "2", "3"]
print(graph.breadth_first_traversal("4"))  # Expected Output: ["4", "5"]

graph = Graph()
graph.add_vertex("X").add_vertex("Y").add_vertex("Z")
graph.add_edge("X", "Y").add_edge("Y", "Z").add_edge("Z", "X")

print(graph.breadth_first_traversal("X"))  # Expected Output: ["X", "Y", "Z"]
