# Topic 12: Graph Data Structure

# Task 1: Implementing a Graph Using Adjacency List & Adjacency Matrix

class Graph:
    def __init__(self, directed=False):
        self.directed = directed
        self.adj_list = {}
        self.vertices = []
        self.adj_matrix = []

    def add_vertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []
            self.vertices.append(vertex)
            # Update adjacency matrix
            size = len(self.vertices)
            for row in self.adj_matrix:
                row.append(0)
            self.adj_matrix.append([0] * size)

    def add_edge(self, start, end):
        if start not in self.adj_list or end not in self.adj_list:
            print("Error: One or both vertices not found.")
            return

        # Add edge to adjacency list
        self.adj_list[start].append(end)
        if not self.directed:
            self.adj_list[end].append(start)

        # Add edge to adjacency matrix
        start_idx = self.vertices.index(start)
        end_idx = self.vertices.index(end)
        self.adj_matrix[start_idx][end_idx] = 1
        if not self.directed:
            self.adj_matrix[end_idx][start_idx] = 1

    def display_adj_list(self):
        print("Adjacency List:")
        print(self.adj_list)

    def display_adj_matrix(self):
        print("Adjacency Matrix:")
        print("  ", " ".join(self.vertices))
        for i, row in enumerate(self.adj_matrix):
            print(self.vertices[i], row)


# Example Usage
g = Graph(directed=True)
g.add_vertex("A")
g.add_vertex("B")
g.add_edge("A", "B")
g.display_adj_list()
g.display_adj_matrix()

# Task 2: Implementing Breadth-First Search (BFS) & Depth-First Search (DFS)..

from collections import deque

class Graph:
    def __init__(self, directed=False):
        self.directed = directed
        self.adj_list = {}
        self.vertices = []
        self.adj_matrix = []

    def add_vertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []
            self.vertices.append(vertex)
            size = len(self.vertices)
            for row in self.adj_matrix:
                row.append(0)
            self.adj_matrix.append([0] * size)

    def add_edge(self, start, end):
        if start not in self.adj_list or end not in self.adj_list:
            print("Error: One or both vertices not found.")
            return
        self.adj_list[start].append(end)
        if not self.directed:
            self.adj_list[end].append(start)
        start_idx = self.vertices.index(start)
        end_idx = self.vertices.index(end)
        self.adj_matrix[start_idx][end_idx] = 1
        if not self.directed:
            self.adj_matrix[end_idx][start_idx] = 1

    def display_adj_list(self):
        print("Adjacency List:")
        print(self.adj_list)

    def display_adj_matrix(self):
        print("Adjacency Matrix:")
        print("  ", " ".join(self.vertices))
        for i, row in enumerate(self.adj_matrix):
            print(self.vertices[i], row)

    # BFS Implementation
    def bfs(self, start):
        if start not in self.adj_list:
            print("Error: Start vertex not found.")
            return []
        visited = set()
        queue = deque([start])
        result = []
        while queue:
            vertex = queue.popleft()
            if vertex not in visited:
                visited.add(vertex)
                result.append(vertex)
                queue.extend([neighbor for neighbor in self.adj_list[vertex] if neighbor not in visited])
        return result

    # DFS Implementation (Recursive)
    def dfs_recursive(self, start, visited=None):
        if visited is None:
            visited = set()
        if start not in self.adj_list:
            print("Error: Start vertex not found.")
            return []
        visited.add(start)
        result = [start]
        for neighbor in self.adj_list[start]:
            if neighbor not in visited:
                result.extend(self.dfs_recursive(neighbor, visited))
        return result

    # DFS Implementation (Using Stack)
    def dfs_stack(self, start):
        if start not in self.adj_list:
            print("Error: Start vertex not found.")
            return []
        visited = set()
        stack = [start]
        result = []
        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                visited.add(vertex)
                result.append(vertex)
                stack.extend([neighbor for neighbor in reversed(self.adj_list[vertex]) if neighbor not in visited])
        return result


# Example Usage
g = Graph(directed=False)
g.add_vertex("A")
g.add_vertex("B")
g.add_vertex("C")
g.add_vertex("D")
g.add_edge("A", "B")
g.add_edge("A", "C")
g.add_edge("B", "D")
g.add_edge("C", "D")

print("BFS:", g.bfs("A"))  # Output: ['A', 'B', 'C', 'D']
print("DFS (Recursive):", g.dfs_recursive("A"))  # Output: ['A', 'B', 'D', 'C'] or another valid DFS order
print("DFS (Stack):", g.dfs_stack("A"))  # Output: ['A', 'C', 'D', 'B'] or another valid DFS order


# Task 3: Implementing Dijkstra’s Algorithm for Shortest Path

import heapq

class Graph:
    def __init__(self, directed=False):
        self.directed = directed
        self.adj_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []

    def add_edge(self, start, end, weight):
        if start not in self.adj_list or end not in self.adj_list:
            print("Error: One or both vertices not found.")
            return
        self.adj_list[start].append((end, weight))
        if not self.directed:
            self.adj_list[end].append((start, weight))

    def dijkstra(self, start):
        if start not in self.adj_list:
            print("Error: Start vertex not found.")
            return {}

        # Initialize distances and priority queue
        distances = {vertex: float('inf') for vertex in self.adj_list}
        distances[start] = 0
        priority_queue = [(0, start)]  # (distance, vertex)

        while priority_queue:
            current_distance, current_vertex = heapq.heappop(priority_queue)

            # Skip if the current distance is not optimal
            if current_distance > distances[current_vertex]:
                continue

            # Explore neighbors
            for neighbor, weight in self.adj_list[current_vertex]:
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))

        return distances


# Example Usage
g = Graph(directed=True)
g.add_vertex("A")
g.add_vertex("B")
g.add_vertex("C")
g.add_vertex("D")
g.add_edge("A", "B", 4)
g.add_edge("A", "C", 1)
g.add_edge("C", "B", 2)
g.add_edge("B", "D", 1)

print("Shortest Paths:", g.dijkstra("A"))  # Output: {'A': 0, 'B': 3, 'C': 1, 'D': 4}