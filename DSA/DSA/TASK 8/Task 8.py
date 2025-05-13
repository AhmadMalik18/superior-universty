# Topic 8: Graphs & Graph Algorithms

#Task 1: Implementing a Graph Using Adjacency List & Adjacency Matrix

import heapq

class Heap:
    def __init__(self, heap_type="min"):
        self.heap = []
        self.heap_type = heap_type.lower()

    def _compare(self, a, b):
        if self.heap_type == "min":
            return a < b
        else:
            return a > b

    def insert(self, value):
        self.heap.append(value)
        self._sift_up(len(self.heap) - 1)

    def extract_root(self):
        if not self.heap:
            return None
        root = self.heap[0]
        last = self.heap.pop()
        if self.heap:
            self.heap[0] = last
            self._sift_down(0)
        return root

    def peek(self):
        return self.heap[0] if self.heap else None

    def heapify(self, array):
        self.heap = array[:]
        for i in reversed(range(len(self.heap) // 2)):
            self._sift_down(i)

    def _sift_up(self, index):
        parent = (index - 1) // 2
        while index > 0 and self._compare(self.heap[index], self.heap[parent]):
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            index = parent
            parent = (index - 1) // 2

    def _sift_down(self, index):
        n = len(self.heap)
        while (2 * index + 1) < n:
            child = 2 * index + 1
            right = child + 1
            if right < n and self._compare(self.heap[right], self.heap[child]):
                child = right
            if self._compare(self.heap[child], self.heap[index]):
                self.heap[child], self.heap[index] = self.heap[index], self.heap[child]
                index = child
            else:
                break

class PriorityQueue:
    def __init__(self):
        self.heap = []

    def enqueue(self, value, priority):
        heapq.heappush(self.heap, (priority, value))

    def dequeue(self):
        if self.heap:
            return heapq.heappop(self.heap)[1]
        return None

    def peek(self):
        if self.heap:
            return self.heap[0][1]
        return None

def find_k_smallest(arr, k):
    return heapq.nsmallest(k, arr)

def find_k_largest(arr, k):
    return heapq.nlargest(k, arr)

class Graph:
    def __init__(self, vertices, directed=False):
        self.V = vertices
        self.directed = directed
        self.adj_list = {i: [] for i in range(vertices)}
        self.adj_matrix = [[0 for _ in range(vertices)] for _ in range(vertices)]

    def add_edge(self, v1, v2):
        self.adj_list[v1].append(v2)
        self.adj_matrix[v1][v2] = 1
        if not self.directed:
            self.adj_list[v2].append(v1)
            self.adj_matrix[v2][v1] = 1

    def remove_edge(self, v1, v2):
        if v2 in self.adj_list[v1]:
            self.adj_list[v1].remove(v2)
        self.adj_matrix[v1][v2] = 0
        if not self.directed:
            if v1 in self.adj_list[v2]:
                self.adj_list[v2].remove(v1)
            self.adj_matrix[v2][v1] = 0

    def display(self):
        print("Adjacency List:")
        for key in self.adj_list:
            print(f"{key}: {self.adj_list[key]}")
        print("\nAdjacency Matrix:")
        for row in self.adj_matrix:
            print(row)

# Test Cases

def test_heaps():
    print("Testing Min-Heap")
    min_heap = Heap("min")
    for value in [10, 5, 20, 2]:
        min_heap.insert(value)
    print(min_heap.extract_root())  

    print("Testing Max-Heap")
    max_heap = Heap("max")
    for value in [10, 5, 20, 2]:
        max_heap.insert(value)
    print(max_heap.extract_root())  

    print("Testing Heapify")
    arr = [7, 2, 9, 1, 5]
    min_heap.heapify(arr)
    print(min_heap.extract_root())  

def test_priority_queue():
    print("\nTesting Priority Queue")
    pq = PriorityQueue()
    pq.enqueue("Task A", 3)
    pq.enqueue("Task B", 1)
    pq.enqueue("Task C", 2)
    print(pq.dequeue())  
    print(pq.peek())     

    print("\nTesting Priority Queue - Emergency Room")
    er = PriorityQueue()
    er.enqueue("Patient A - Mild", 5)
    er.enqueue("Patient B - Critical", 1)
    er.enqueue("Patient C - Serious", 2)
    print(er.dequeue())  
    print(er.dequeue())  

def test_k_elements():
    print("\nTesting K Smallest and Largest Elements")
    arr = [10, 4, 3, 20, 15, 7]
    print("K Smallest (3):", find_k_smallest(arr, 3))  
    print("K Largest (2):", find_k_largest(arr, 2))    

def test_graph():
    print("\nTesting Graph Representation")
    g = Graph(5)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 4)
    g.display()

if __name__ == "__main__":
    test_heaps()
    test_priority_queue()
    test_k_elements()
    test_graph()


# Task 2: Implementing Breadth-First Search (BFS) and Depth-First Search(DFS).

import heapq
from collections import deque

class Heap:
    def __init__(self, heap_type="min"):
        self.heap = []
        self.heap_type = heap_type.lower()

    def _compare(self, a, b):
        if self.heap_type == "min":
            return a < b
        else:
            return a > b

    def insert(self, value):
        self.heap.append(value)
        self._sift_up(len(self.heap) - 1)

    def extract_root(self):
        if not self.heap:
            return None
        root = self.heap[0]
        last = self.heap.pop()
        if self.heap:
            self.heap[0] = last
            self._sift_down(0)
        return root

    def peek(self):
        return self.heap[0] if self.heap else None

    def heapify(self, array):
        self.heap = array[:]
        for i in reversed(range(len(self.heap) // 2)):
            self._sift_down(i)

    def _sift_up(self, index):
        parent = (index - 1) // 2
        while index > 0 and self._compare(self.heap[index], self.heap[parent]):
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            index = parent
            parent = (index - 1) // 2

    def _sift_down(self, index):
        n = len(self.heap)
        while (2 * index + 1) < n:
            child = 2 * index + 1
            right = child + 1
            if right < n and self._compare(self.heap[right], self.heap[child]):
                child = right
            if self._compare(self.heap[child], self.heap[index]):
                self.heap[child], self.heap[index] = self.heap[index], self.heap[child]
                index = child
            else:
                break

class PriorityQueue:
    def __init__(self):
        self.heap = []

    def enqueue(self, value, priority):
        heapq.heappush(self.heap, (priority, value))

    def dequeue(self):
        if self.heap:
            return heapq.heappop(self.heap)[1]
        return None

    def peek(self):
        if self.heap:
            return self.heap[0][1]
        return None

def find_k_smallest(arr, k):
    return heapq.nsmallest(k, arr)

def find_k_largest(arr, k):
    return heapq.nlargest(k, arr)

class Graph:
    def __init__(self, vertices, directed=False):
        self.vertices = vertices
        self.directed = directed
        self.adj_list = {i: [] for i in range(vertices)}
        self.adj_matrix = [[0 for _ in range(vertices)] for _ in range(vertices)]

    def add_edge(self, v1, v2):
        self.adj_list[v1].append(v2)
        self.adj_matrix[v1][v2] = 1
        if not self.directed:
            self.adj_list[v2].append(v1)
            self.adj_matrix[v2][v1] = 1

    def remove_edge(self, v1, v2):
        if v2 in self.adj_list[v1]:
            self.adj_list[v1].remove(v2)
        self.adj_matrix[v1][v2] = 0
        if not self.directed:
            if v1 in self.adj_list[v2]:
                self.adj_list[v2].remove(v1)
            self.adj_matrix[v2][v1] = 0

    def display(self):
        print("Adjacency List:")
        for key in self.adj_list:
            print(f"{key}: {self.adj_list[key]}")
        print("\nAdjacency Matrix:")
        for row in self.adj_matrix:
            print(row)

    def bfs(self, start):
        visited = []
        queue = deque([start])
        visited_set = set()
        visited_set.add(start)

        while queue:
            vertex = queue.popleft()
            visited.append(vertex)
            for neighbor in self.adj_list[vertex]:
                if neighbor not in visited_set:
                    queue.append(neighbor)
                    visited_set.add(neighbor)
        return visited

    def dfs(self, start):
        visited = []
        def dfs_helper(v):
            visited.append(v)
            for neighbor in self.adj_list[v]:
                if neighbor not in visited:
                    dfs_helper(neighbor)
        dfs_helper(start)
        return visited

# Test Cases

def test_heaps():
    print("Testing Min-Heap")
    min_heap = Heap("min")
    for value in [10, 5, 20, 2]:
        min_heap.insert(value)
    print(min_heap.extract_root())  # Output: 2

    print("Testing Max-Heap")
    max_heap = Heap("max")
    for value in [10, 5, 20, 2]:
        max_heap.insert(value)
    print(max_heap.extract_root())  # Output: 20

    print("Testing Heapify")
    arr = [7, 2, 9, 1, 5]
    min_heap.heapify(arr)
    print(min_heap.extract_root())  # Output: 1

def test_priority_queue():
    print("\nTesting Priority Queue")
    pq = PriorityQueue()
    pq.enqueue("Task A", 3)
    pq.enqueue("Task B", 1)
    pq.enqueue("Task C", 2)
    print(pq.dequeue())  # Output: Task B
    print(pq.peek())     # Output: Task C

    print("\nTesting Priority Queue - Emergency Room")
    er = PriorityQueue()
    er.enqueue("Patient A - Mild", 5)
    er.enqueue("Patient B - Critical", 1)
    er.enqueue("Patient C - Serious", 2)
    print(er.dequeue())  # Output: Patient B - Critical
    print(er.dequeue())  # Output: Patient C - Serious

def test_k_elements():
    print("\nTesting K Smallest and Largest Elements")
    arr = [10, 4, 3, 20, 15, 7]
    print("K Smallest (3):", find_k_smallest(arr, 3))  # Output: [3, 4, 7]
    print("K Largest (2):", find_k_largest(arr, 2))    # Output: [20, 15]

def test_graph():
    print("\nTesting Graph")
    g = Graph(5)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 4)
    g.display()

    print("\nTesting Graph BFS and DFS")
    g2 = Graph(6)
    g2.add_edge(0, 1)
    g2.add_edge(0, 2)
    g2.add_edge(1, 3)
    g2.add_edge(1, 4)
    g2.add_edge(2, 5)
    print("BFS Traversal:", g2.bfs(0))  # Output: [0, 1, 2, 3, 4, 5]
    print("DFS Traversal:", g2.dfs(0))  # Output: [0, 1, 3, 4, 2, 5] or similar

if __name__ == "__main__":
    test_heaps()
    test_priority_queue()
    test_k_elements()
    test_graph()

# Task 3:Implementing Dijkstra’s Algorithm for Shortest Path

import heapq
from collections import deque

class Heap:
    def __init__(self, heap_type="min"):
        self.heap = []
        self.heap_type = heap_type.lower()

    def _compare(self, a, b):
        if self.heap_type == "min":
            return a < b
        else:
            return a > b

    def insert(self, value):
        self.heap.append(value)
        self._sift_up(len(self.heap) - 1)

    def extract_root(self):
        if not self.heap:
            return None
        root = self.heap[0]
        last = self.heap.pop()
        if self.heap:
            self.heap[0] = last
            self._sift_down(0)
        return root

    def peek(self):
        return self.heap[0] if self.heap else None

    def heapify(self, array):
        self.heap = array[:]
        for i in reversed(range(len(self.heap) // 2)):
            self._sift_down(i)

    def _sift_up(self, index):
        parent = (index - 1) // 2
        while index > 0 and self._compare(self.heap[index], self.heap[parent]):
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            index = parent
            parent = (index - 1) // 2

    def _sift_down(self, index):
        n = len(self.heap)
        while (2 * index + 1) < n:
            child = 2 * index + 1
            right = child + 1
            if right < n and self._compare(self.heap[right], self.heap[child]):
                child = right
            if self._compare(self.heap[child], self.heap[index]):
                self.heap[child], self.heap[index] = self.heap[index], self.heap[child]
                index = child
            else:
                break

class PriorityQueue:
    def __init__(self):
        self.heap = []

    def enqueue(self, value, priority):
        heapq.heappush(self.heap, (priority, value))

    def dequeue(self):
        if self.heap:
            return heapq.heappop(self.heap)[1]
        return None

    def peek(self):
        if self.heap:
            return self.heap[0][1]
        return None

def find_k_smallest(arr, k):
    return heapq.nsmallest(k, arr)

def find_k_largest(arr, k):
    return heapq.nlargest(k, arr)

class Graph:
    def __init__(self, vertices, directed=False):
        self.v = vertices
        self.directed = directed
        self.adj_list = {i: [] for i in range(vertices)}
        self.adj_matrix = [[0 for _ in range(vertices)] for _ in range(vertices)]

    def add_edge(self, v1, v2):
        self.adj_list[v1].append(v2)
        self.adj_matrix[v1][v2] = 1
        if not self.directed:
            self.adj_list[v2].append(v1)
            self.adj_matrix[v2][v1] = 1

    def remove_edge(self, v1, v2):
        if v2 in self.adj_list[v1]:
            self.adj_list[v1].remove(v2)
        self.adj_matrix[v1][v2] = 0
        if not self.directed:
            if v1 in self.adj_list[v2]:
                self.adj_list[v2].remove(v1)
            self.adj_matrix[v2][v1] = 0

    def display(self):
        print("Adjacency List:")
        for key in self.adj_list:
            print(f"{key}: {self.adj_list[key]}")
        print("\nAdjacency Matrix:")
        for row in self.adj_matrix:
            print(row)

    def bfs(self, start):
        visited = []
        queue = deque([start])
        while queue:
            vertex = queue.popleft()
            if vertex not in visited:
                visited.append(vertex)
                for neighbor in self.adj_list[vertex]:
                    if neighbor not in visited:
                        queue.append(neighbor)
        return visited

    def dfs(self, start):
        visited = []
        self._dfs_helper(start, visited)
        return visited

    def _dfs_helper(self, vertex, visited):
        visited.append(vertex)
        for neighbor in self.adj_list[vertex]:
            if neighbor not in visited:
                self._dfs_helper(neighbor, visited)

def dijkstra(graph, start):
    heap = []
    heapq.heappush(heap, (0, start))
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0

    while heap:
        current_distance, current_vertex = heapq.heappop(heap)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(heap, (distance, neighbor))

    return distances

# Test Cases
def test_heaps():
    print("Testing Min-Heap")
    min_heap = Heap("min")
    for value in [10, 5, 20, 2]:
        min_heap.insert(value)
    print(min_heap.extract_root())  # Output: 2

    print("Testing Max-Heap")
    max_heap = Heap("max")
    for value in [10, 5, 20, 2]:
        max_heap.insert(value)
    print(max_heap.extract_root())  # Output: 20

    print("Testing Heapify")
    arr = [7, 2, 9, 1, 5]
    min_heap.heapify(arr)
    print(min_heap.extract_root())  # Output: 1

def test_priority_queue():
    print("\nTesting Priority Queue")
    pq = PriorityQueue()
    pq.enqueue("Task A", 3)
    pq.enqueue("Task B", 1)
    pq.enqueue("Task C", 2)
    print(pq.dequeue())  # Output: Task B
    print(pq.peek())     # Output: Task C

    print("\nTesting Priority Queue - Emergency Room")
    er = PriorityQueue()
    er.enqueue("Patient A - Mild", 5)
    er.enqueue("Patient B - Critical", 1)
    er.enqueue("Patient C - Serious", 2)
    print(er.dequeue())  # Output: Patient B - Critical
    print(er.dequeue())  # Output: Patient C - Serious

def test_k_elements():
    print("\nTesting K Smallest and Largest Elements")
    arr = [10, 4, 3, 20, 15, 7]
    print("K Smallest (3):", find_k_smallest(arr, 3))  # Output: [3, 4, 7]
    print("K Largest (2):", find_k_largest(arr, 2))    # Output: [20, 15]

def test_graph():
    print("\nTesting Graph")
    g = Graph(5)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 4)
    g.display()
    print("BFS starting from 0:", g.bfs(0))
    print("DFS starting from 0:", g.dfs(0))

def test_dijkstra():
    print("\nTesting Dijkstra's Algorithm")
    graph = {
        'A': {'B': 4, 'C': 1},
        'B': {'A': 4, 'C': 2, 'D': 5},
        'C': {'A': 1, 'B': 2, 'D': 8},
        'D': {'B': 5, 'C': 8}
    }
    print(dijkstra(graph, 'A'))  # Expected: {'A': 0, 'B': 3, 'C': 1, 'D': 9}

if __name__ == "__main__":
    test_heaps()
    test_priority_queue()
    test_k_elements()
    test_graph()
    test_dijkstra()
