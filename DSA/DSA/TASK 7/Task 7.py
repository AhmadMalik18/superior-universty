# Topic 7: Heaps & Priority Queues

#Task 1: Implementing a Min-Heap and Max-Heap

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

    def peak(self):
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


def test_heaps():
    print("Testing Min-Heap") 
    min_heap = Heap("min")
    for value in [10, 5, 20, 2]:
        min_heap.insert(value)
    print(min_heap.extract_root())

    print("Texting Max-Heap")
    max_heap = Heap("max")
    for value in [10, 5, 20, 2]:
        max_heap.insert(value)
    print(max_heap.extract_root())

    print("Testing Heapify")
    arr = [7, 2, 9, 1, 5]
    min_heap.heapify(arr)
    print(min_heap.extract_root())

test_heaps()

# Task 2: Implementing a Priority Queue Using a Heap

import heapq

class Heap:
    def __init__(self, heap_type="min"):
        self.heap = []
        self.heap_type = heap_type.lower()
    
    def _compare(self, a, b):
        if self.heap_type  == "min":
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

if __name__ == "__main__":
    test_heaps()
    test_priority_queue()


# Task 3: Finding the K Smallest and K Largest Elements Using a Heap

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

if __name__ == "__main__":
    test_heaps()
    test_priority_queue()
