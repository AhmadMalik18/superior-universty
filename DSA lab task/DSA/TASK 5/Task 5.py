#Topic 5: Hashing & Hash Tables

# Task 1: Implementing a Custom Hash Table with Collision Handling
# Node class for linked list in chaining...
import random
import time


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

# Hash Table with Chaining...
class HashTableChaining:
    def __init__(self, size = 10):
        self.size = size
        self.table = [None] * self.size

    def _hash(self, key):
        return hash(key) % self.size
    
    def insert(self, key, value):
        index = self._hash(key)
        new_node = Node(key, value)
        if self.table[index] is None:
            self.table[index] = new_node
        else:
            current = self.table[index]
            while current:
                if current.key == key:
                    current.value = value
                    return
                if current.next is None:
                    break
                current = current.next
            current.next = new_node

    def get(self, key):
        index = self._hash(key)
        current = self.table[index]
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None

    def delete(self, key):
        index = self._hash(key)
        current = self.table[index]
        prev = None
        while current:
            if current.key == key:
                if prev:
                    prev.next = current.next
                else:
                    self.table[index] = current.next
                return
            prev = current
            current = current.next

    def display(self):
        for index, node in enumerate(self.table):
            if node:
                current = node
                chain = []
                while current:
                    chain.append(f"{current.key}: {current.value}")
                    current = current.next
                print(f"Index {index}: " + " -> ".join(chain))
            else:
                print(f"Index {index}: None")

# # Hash Table with Open Addressing (Linear Probing)
class HashTableOpenAddressing:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * self.size

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash(key)
        while self.table[index] is not None:
            if self.table[index][0] == key:
                self.table[index] = (key, value)  # Update existing key
                return
            index = (index + 1) % self.size
        self.table[index] = (key, value)

    def get(self, key):
        index = self._hash(key)
        while self.table[index] is not None:
            if self.table[index][0] == key:
                return self.table[index][1]
            index = (index + 1) % self.size
        return None

    def delete(self, key):
        index = self._hash(key)
        while self.table[index] is not None:
            if self.table[index][0] == key:
                self.table[index] = None
                return
            index = (index + 1) % self.size

    def display(self):
        for index, item in enumerate(self.table):
            if item is not None:
                print(f"Index {index}: {item[0]}: {item[1]}")
            else:
                print(f"Index {index}: None")

# Performance Comparison
def performance_test():
    keys = [random.randint(1, 10000) for _ in range(1000)]
    values = [random.randint(1, 10000) for _ in range(1000)]

    # Test Chaining
    chaining_table = HashTableChaining()
    start_time = time.time()
    for key, value in zip(keys, values):
        chaining_table.insert(key, value)
    for key in keys:
        chaining_table.get(key)
    end_time = time.time()
    print(f"Chaining Time: {end_time - start_time:.6f} seconds")

    # Test Open Addressing
    open_addressing_table = HashTableOpenAddressing()
    start_time = time.time()
    for key, value in zip(keys, values):
        open_addressing_table.insert(key, value)
    for key in keys:
        open_addressing_table.get(key)
    end_time = time.time()
    print(f"Open Addressing Time: {end_time - start_time:.6f} seconds")

# Run performance test
performance_test()


# Task 2: Checking if Two Strings Are Anagrams Using Hashing
def are_anagrams(str1, str2):
    # If lengths are not the same, they cannot be anagrams
    if len(str1) != len(str2):
        return False

    # Create a frequency dictionary for the first string
    char_count = {}

    # Count the frequency of each character in str1
    for char in str1:
        char_count[char] = char_count.get(char, 0) + 1

    # Decrease the count for each character in str2
    for char in str2:
        if char in char_count:
            char_count[char] -= 1
            if char_count[char] < 0:
                return False
        else:
            return False

    # If all counts are zero, they are anagrams
    return all(count == 0 for count in char_count.values())

# Test cases
def test_are_anagrams():
    test_cases = [
        ("listen", "silent"),  # True
        ("hello", "world"),    # False
        ("anagram", "nagaram"), # True
        ("rat", "car"),        # False
        ("evil", "vile"),      # True
        ("fluster", "restful"), # True
        ("", ""),               # True (empty strings)
        ("aabbcc", "abcabc"),   # True
        ("abcd", "abcde"),      # False
        ("a" * 1000, "a" * 1000) # True (large strings)
    ]

    for str1, str2 in test_cases:
        result = are_anagrams(str1, str2)
        print(f"are_anagrams({str1!r}, {str2!r}) = {result}")

# Run the test cases
test_are_anagrams()

# Task 3: Implementing a Simple Caching Mechanism Using Hash Maps
class Node:
    """A node in the doubly linked list."""
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    """LRU Cache implementation."""
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # Hash map to store key and node
        self.head = Node(0, 0)  # Dummy head
        self.tail = Node(0, 0)  # Dummy tail
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: Node):
        """Remove a node from the doubly linked list."""
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _add_to_head(self, node: Node):
        """Add a node right after the head (most recently used)."""
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int):
        """Retrieve a value from the cache and update its usage."""
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._add_to_head(node)
            return node.value
        return -1  # Key not found

    def put(self, key: int, value: str):
        """Insert a key-value pair into the cache."""
        if key in self.cache:
            # Update the value and move the node to the head
            node = self.cache[key]
            node.value = value
            self._remove(node)
            self._add_to_head(node)
        else:
            # Create a new node
            new_node = Node(key, value)
            self.cache[key] = new_node
            self._add_to_head(new_node)

            if len(self.cache) > self.capacity:
                # Remove the least recently used item
                lru_node = self.tail.prev
                self._remove(lru_node)
                del self.cache[lru_node.key]

    def display(self):
        """Print the current state of the cache."""
        current = self.head.next
        cache_state = {}
        while current != self.tail:
            cache_state[current.key] = current.value
            current = current.next
        print("Cache state:", cache_state)

# Test the LRU Cache
def test_lru_cache():
    cache = LRUCache(5)
    cache.put(1, "A")
    cache.put(2, "B")
    cache.put(3, "C")
    cache.put(4, "D")
    cache.put(5, "E")
    cache.display()  # Expected: {1: "A", 2: "B", 3: "C", 4: "D", 5: "E"}

    print(cache.get(2))  # Expected: "B"
    cache.display()  # Expected: {1: "A", 3: "C", 4: "D", 5: "E", 2: "B"}

    cache.put(6, "F")  # Should remove key 1 (least recently used)
    cache.display()  # Expected: {3: "C", 4: "D", 5: "E", 2: "B", 6: "F"}

    cache.put(7, "G")  # Should remove key 3 (least recently used)
    cache.display()  # Expected: {4: "D", 5: "E", 2: "B", 6: "F", 7: "G"}

    print(cache.get(1))  # Expected: -1 (not found)
    print(cache.get(4))  # Expected: "D"

# Run the test cases
test_lru_cache()