# Topic 3: Linked Lists

# Task 1: Implementing a Singly Linked List

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def insert_at_position(self, value, position):
        if position < 1:
            raise ValueError("Position must be 1 or greater")
        new_node = Node(value)
        if position == 1:
            new_node.next = self.head
            self.head = new_node
            return
        temp = self.head
        for _ in range(position - 2):
            if not temp:
                raise IndexError("Position out of bounds")
            temp = temp.next
        new_node.next = temp.next
        temp.next = new_node

    def delete_by_value(self, value):
        if not self.head:
            return
        if self.head.value == value:
            self.head = self.head.next
            return
        temp = self.head
        while temp.next and temp.next.value != value:
            temp = temp.next
        if temp.next:
            temp.next = temp.next.next

    def search(self, value):
        temp = self.head
        position = 1
        while temp:
            if temp.value == value:
                return position
            temp = temp.next
            position += 1
        return -1

    def display(self):
        elements = []
        temp = self.head
        while temp:
            elements.append(temp.value)
            temp = temp.next
        return elements

# Test cases
sll = SinglyLinkedList()
sll.insert_at_end(1)
sll.insert_at_end(2)
sll.insert_at_end(3)
sll.insert_at_end(4)
sll.insert_at_end(5)
sll.delete_by_value(3)
print("Linked List:", sll.display())
print("Search(4):", sll.search(4))
print("Search(6):", sll.search(6))

# Task 2: Detecting and Removing a Loop in a Linked List

class SinglyLinkedListWithLoop(SinglyLinkedList):
    def detect_loop(self):
        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                print("Loop detected")
                return slow 
        return None

    def find_start_of_loop(self):
        meeting_point = self.detect_loop()
        if not meeting_point:
            return None 

        start = self.head
        while start != meeting_point:
            start = start.next
            meeting_point = meeting_point.next

        print(f"Loop starts at node with value: {start.value}")
        return start

    def remove_loop(self):
        start_of_loop = self.find_start_of_loop()
        if not start_of_loop:
            print("No loop to remove")
            return

        temp = start_of_loop
        while temp.next != start_of_loop:
            temp = temp.next

        temp.next = None  
        print("Loop removed")

sll_with_loop = SinglyLinkedListWithLoop()
sll_with_loop.insert_at_end(1)
sll_with_loop.insert_at_end(2)
sll_with_loop.insert_at_end(3)
sll_with_loop.insert_at_end(4)
sll_with_loop.insert_at_end(5)


loop_node = sll_with_loop.head.next.next 
temp = sll_with_loop.head
while temp.next:
    temp = temp.next
temp.next = loop_node  

sll_with_loop.detect_loop()
sll_with_loop.find_start_of_loop()
sll_with_loop.remove_loop()


print("Linked List after removing loop:", sll_with_loop.display())

#  Task 3: Implementing a Doubly Linked List and Reverse Traversal..

class DoublyNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, value):
        new_node = DoublyNode(value)
        if not self.head:
            self.head = new_node
            return
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    def insert_at_end(self, value):
        new_node = DoublyNode(value)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp

    def delete_at_position(self, position):
        if position < 1:
            raise ValueError("Position must be 1 or greater")
        if not self.head:
            print("List is empty")
            return
        if position == 1:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            return
        temp = self.head
        for _ in range(position - 1):
            if not temp:
                raise IndexError("Position out of bounds")
            temp = temp.next
        if temp.next:
            temp.next.prev = temp.prev
        if temp.prev:
            temp.prev.next = temp.next

    def traverse_forward(self):
        elements = []
        temp = self.head
        while temp:
            elements.append(temp.value)
            temp = temp.next
        return elements

    def traverse_reverse(self):
        elements = []
        temp = self.head
        if not temp:
            return elements
        while temp.next:
            temp = temp.next
        while temp:
            elements.append(temp.value)
            temp = temp.prev
        return elements


dll = DoublyLinkedList()
dll.insert_at_beginning(3)
dll.insert_at_beginning(2)
dll.insert_at_beginning(1)
dll.insert_at_end(4)
dll.insert_at_end(5)

print("Forward Traversal:", dll.traverse_forward())  
print("Reverse Traversal:", dll.traverse_reverse())  

dll.delete_at_position(3)  
print("After Deletion (Forward):", dll.traverse_forward())  
print("After Deletion (Reverse):", dll.traverse_reverse())  