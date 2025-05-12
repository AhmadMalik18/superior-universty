# Topic 16: Graph Algorithms

# Task 1: Implementing Depth-First Search (DFS) and Breadth-First Search (BFS)

# Depth-First Search (DFS) - Recursive
def dfs_recursive(graph, node, visited=None):
    if visited is None:
        visited = []
    visited.append(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)
    return visited

# Depth-First Search (DFS) - Iterative
def dfs_iterative(graph, start):
    visited = []
    stack = [start]
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            stack.extend(reversed(graph[node]))  # Reverse to maintain order
    return visited

# Breadth-First Search (BFS)
def bfs(graph, start):
    visited = []
    queue = [start]
    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.append(node)
            queue.extend(graph[node])
    return visited

# Example graph
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Testing the functions
print("DFS Recursive:", dfs_recursive(graph, 'A'))  # Output: ['A', 'B', 'D', 'E', 'F', 'C']
print("DFS Iterative:", dfs_iterative(graph, 'A'))  # Output: ['A', 'B', 'D', 'E', 'F', 'C']
print("BFS:", bfs(graph, 'A'))                     # Output: ['A', 'B', 'C', 'D', 'E', 'F']


# Task 2: Finding the Shortest Path Using Dijkstra’s Algorithm

import heapq

# Dijkstra's Algorithm
def dijkstra(graph, start):
    # Initialize distances with infinity and set the distance to the start node as 0
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    # Priority queue to store (distance, node)
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # Skip if the current distance is greater than the recorded distance
        if current_distance > distances[current_node]:
            continue

        # Explore neighbors
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # If a shorter path is found
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# Example weighted graph
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

# Testing the function
print("Shortest distances from 'A':", dijkstra(graph, 'A'))  # Output: {'A': 0, 'B': 1, 'C': 3, 'D': 4}


# Task 3: Detecting Cycles in a Graph (Directed & Undirected)

# Cycle Detection in an Undirected Graph using Union-Find (Disjoint Set)
class UnionFind:
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}
        self.rank = {v: 0 for v in vertices}

    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])  # Path compression
        return self.parent[node]

    def union(self, node1, node2):
        root1 = self.find(node1)
        root2 = self.find(node2)

        if root1 != root2:
            # Union by rank
            if self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            elif self.rank[root1] < self.rank[root2]:
                self.parent[root1] = root2
            else:
                self.parent[root2] = root1
                self.rank[root1] += 1

def detect_cycle_undirected(graph):
    vertices = list(graph.keys())
    uf = UnionFind(vertices)

    for node in graph:
        for neighbor in graph[node]:
            if uf.find(node) == uf.find(neighbor):
                return True  # Cycle detected
            uf.union(node, neighbor)
    return False  # No cycle detected

# Cycle Detection in a Directed Graph using DFS + Recursion Stack
def detect_cycle_directed(graph):
    def dfs(node, visited, rec_stack):
        visited.add(node)
        rec_stack.add(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                if dfs(neighbor, visited, rec_stack):
                    return True
            elif neighbor in rec_stack:
                return True

        rec_stack.remove(node)
        return False

    visited = set()
    rec_stack = set()

    for node in graph:
        if node not in visited:
            if dfs(node, visited, rec_stack):
                return True
    return False

# Example graphs
graph_undirected = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C']
}

graph_directed = {
    'A': ['B'],
    'B': ['C'],
    'C': ['A']
}

# Testing the functions
print("Cycle in undirected graph:", detect_cycle_undirected(graph_undirected))  # Output: True
print("Cycle in directed graph:", detect_cycle_directed(graph_directed))        # Output: True

