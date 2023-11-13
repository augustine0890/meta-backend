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
