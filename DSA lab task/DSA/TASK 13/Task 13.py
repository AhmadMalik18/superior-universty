# Topic 13: Greedy Algorithms

# Task 1: Implementing Activity Selection Algorithm

def activity_selection(activities):
    """
    Selects the maximum number of non-overlapping activities using a greedy approach.
    
    Parameters:
    activities (list of tuples): A list of activities where each activity is represented as (start_time, end_time).
    
    Returns:
    list of tuples: A list of selected non-overlapping activities.
    """
    # Step 1: Sort activities based on their finish times
    sorted_activities = sorted(activities, key=lambda x: x[1])
    
    # Step 2: Initialize the list of selected activities
    selected_activities = []
    
    # Step 3: Select the first activity
    last_end_time = 0  # Tracks the end time of the last selected activity
    for activity in sorted_activities:
        start_time, end_time = activity
        if start_time >= last_end_time:
            selected_activities.append(activity)
            last_end_time = end_time  # Update the end time of the last selected activity
    
    return selected_activities

# Example Input
activities = [(1, 3), (2, 5), (3, 9), (6, 8), (8, 11)]

# Example Output
print("Selected Activities:", activity_selection(activities))

# Task 2: Implementing Huffman Coding for Data Compression


import heapq
from collections import Counter, namedtuple

class HuffmanNode(namedtuple("HuffmanNode", ["char", "freq"])):
    def __lt__(self, other):
        return self.freq < other.freq

    def __init__(self, char, freq):
        self.left = None
        self.right = None

def build_huffman_tree(text):
    """
    Builds the Huffman Tree using a priority queue (min-heap).
    
    Parameters:
    text (str): The input string.
    
    Returns:
    HuffmanNode: The root of the Huffman Tree.
    """
    # Step 1: Count character frequencies
    freq = Counter(text)
    
    # Step 2: Create a priority queue (min-heap) of Huffman nodes
    heap = [HuffmanNode(char, freq) for char, freq in freq.items()]
    heapq.heapify(heap)
    
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = HuffmanNode(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)
    
    return heap[0]  # Root of the Huffman Tree

def generate_huffman_codes(node, prefix="", code_map=None):
    """
    Generates Huffman codes for characters by traversing the Huffman Tree.
    
    Parameters:
    node (HuffmanNode): The root of the Huffman Tree.
    prefix (str): The current prefix for the Huffman code.
    code_map (dict): A dictionary to store character-to-code mappings.
    
    Returns:
    dict: A dictionary of Huffman codes for each character.
    """
    if code_map is None:
        code_map = {}
    
    if node.char is not None:  # Leaf node
        code_map[node.char] = prefix
    else:
        generate_huffman_codes(node.left, prefix + "0", code_map)
        generate_huffman_codes(node.right, prefix + "1", code_map)
    
    return code_map

def huffman_encoding(text):
    """
    Encodes the given text using Huffman Coding.
    
    Parameters:
    text (str): The input string.
    
    Returns:
    dict: A dictionary of Huffman codes for each character.
    """
    if not text:
        return {}
    
    # Step 1: Build the Huffman Tree
    root = build_huffman_tree(text)
    
    # Step 2: Generate Huffman codes
    huffman_codes = generate_huffman_codes(root)
    
    return huffman_codes

# Example Input
text = "hello greedy"

# Example Output
huffman_codes = huffman_encoding(text)
print("Huffman Codes:", huffman_codes)

# Comparison of original vs compressed data size
original_size = len(text) * 8  # Each character is 8 bits
compressed_size = sum(len(huffman_codes[char]) * freq for char, freq in Counter(text).items())
print(f"Original Size: {original_size} bits")
print(f"Compressed Size: {compressed_size} bits")

# Task 3: Implementing Kruskal’s Algorithm for Minimum Spanning Tree (MST)

class DisjointSet:
    """
    Disjoint-Set (Union-Find) data structure to manage connected components.
    """
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])  # Path compression
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            # Union by rank
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1

def kruskal(edges, n):
    """
    Implements Kruskal's Algorithm to find the Minimum Spanning Tree (MST).
    
    Parameters:
    edges (list of tuples): A list of edges represented as (u, v, weight).
    n (int): The number of vertices in the graph.
    
    Returns:
    list of tuples: The edges included in the MST.
    """
    # Step 1: Sort edges by weight
    edges.sort(key=lambda x: x[2])
    
    # Step 2: Initialize Disjoint-Set
    ds = DisjointSet(n)
    
    # Step 3: Construct MST
    mst = []
    for u, v, weight in edges:
        if ds.find(u - 1) != ds.find(v - 1):  # Check if adding this edge forms a cycle
            mst.append((u, v, weight))
            ds.union(u - 1, v - 1)
    
    return mst

# Example Input
edges = [(1, 2, 4), (2, 3, 1), (1, 3, 3), (3, 4, 2)]
n = 4  # Number of vertices

# Example Output
mst = kruskal(edges, n)
print("Minimum Spanning Tree:", mst)