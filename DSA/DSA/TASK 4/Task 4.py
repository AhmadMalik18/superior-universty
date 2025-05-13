# Topic 4: Stacks & Queues

#Task 1: Implementing a Stack Using Arrays and Linked Lists

# Stack Implement using Arrays..
class StackArray:
    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from empty stack")
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)
    
print("Testing StackArray:")
stack_array = StackArray()
stack_array.push(10)
stack_array.push(20)
stack_array.push(30)
print("Peek:", stack_array.peek())  
print("Pop:", stack_array.pop())   
print("Size:", stack_array.size())
print("Is Empty:", stack_array.is_empty())  

    
# Stack Implement Using Linked Lists..
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class StackLinkedList:
    def __init__(self):
        self.head = None
        self._size = 0

    def push(self, element):
        new_node = Node(element)
        new_node.next = self.head
        self.head = new_node
        self._size += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        value = self.head.value
        self.head = self.head.next
        self._size -= 1
        return value

    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from empty stack")
        return self.head.value

    def is_empty(self):
        return self.head is None

    def size(self):
        return self._size    
    
print("\nTesting StackLinkedList:")
stack_linked_list = StackLinkedList()
stack_linked_list.push(10)
stack_linked_list.push(20)
stack_linked_list.push(30)
print("Peek:", stack_linked_list.peek())  
print("Pop:", stack_linked_list.pop())    
print("Size:", stack_linked_list.size())  
print("Is Empty:", stack_linked_list.is_empty()) 

# Task 2: Evaluating Postfix Expressions Using Stacks
def evaluate_postfix(expression):
    stack = []
    operators = {'+', '-', '*', '/'}

    for token in expression.split():
        if token not in operators:
            stack.append(float(token))
        else:
            b = stack.pop()
            a = stack.pop()

            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                if b == 0:
                    raise ZeroDivisionError("Division by zero is not allowed")
                stack.append(a / b)

    return stack.pop()

print("Testing Postfix Evaluation:")
expression1 = "5 1 2 + 4 * + 3 -"
print(f"Expression: {expression1}")
print("Result:", evaluate_postfix(expression1))  

expression2 = "10 2 8 * + 3 -"
print(f"\nExpression: {expression2}")
print("Result:", evaluate_postfix(expression2))  

expression3 = "7 4 5 + * 2 /"
print(f"\nExpression: {expression3}")
print("Result:", evaluate_postfix(expression3))  

expression4 = "3 4 + 2 * 7 /"
print(f"\nExpression: {expression4}")
print("Result:", evaluate_postfix(expression4))  

# Task 3: Implementing a Circular Queue

# Circular Queue Implementation.
class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = -1
        self.rear = -1

    def enqueue(self, element):
        if self.is_full():
            raise OverflowError("Queue is full")
        if self.is_empty():
            self.front = 0
        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = element

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        element = self.queue[self.front]
        if self.front == self.rear:  
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.size
        return element

    def front_element(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.queue[self.front]

    def rear_element(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.queue[self.rear]

    def is_empty(self):
        return self.front == -1

    def is_full(self):
        return (self.rear + 1) % self.size == self.front
    
print("Testing Circular Queue:")
cq = CircularQueue(5)
cq.enqueue(10)
cq.enqueue(20)
cq.enqueue(30)
cq.enqueue(40)
cq.enqueue(50)
print("Dequeued:", cq.dequeue())  
cq.enqueue(60)
print("Front:", cq.front_element())
print("Rear:", cq.rear_element())    
print("Is Full:", cq.is_full())      
print("Is Empty:", cq.is_empty()) 


