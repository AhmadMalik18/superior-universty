#Task 1: DFS with Stack & Node
class Node:
    def __init__(self, value):
        self.value = value 
        self.left = None
        self.right = None

class DFS:
    def __init__(self):
        self.stack = []

    def dfs_with_stack(self, root):
        if root is None:
            return 
        result = []
        self.stack.append(root)
        while self.stack:
            current_node = self.stack.pop()
            result.append(current_node.value)
            if current_node:
                self.stack.append(current_node.right)
            if current_node:
                self.stack.append(current_node.left)
                return result
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
dfs = DFS()
result = dfs.dfs_with_stack(root)
print(f"DFS Traversal (Stack-based): {result}")

#Task 2: Inorder, Preorder, Postorder Traversal in DFS

class Node:
    def __init__(self, value):
        self.value = value 
        self.left = None
        self.right = None

class DFS:
    def __init__(self):
        self.stack = []

    def dfs_preorder(self, root):
        result = []
        if root is None:
            return result 
        self.stack.append(root)
        while self.stack:
            current_node = self.stack.pop()
            result.append(current_node.value)
            if current_node.right:
                self.stack.append(current_node.right)
                if current_node.left:
                    self.stack.append(current_node.left)
                    return result
    def inorder(self, root):
        result = []
        current_node = root
        stack = []
        while stack or current_node:
            while current_node:
                stack.append(current_node)
                current_node = current_node.left
                current_node = stack.pop()
                result.append(current_node.value)
                current_node = current_node.right
            return result
    def postorder(self, root):
        result = []
        if root is None:
            return result
        stack = []
        last_visited_node = None
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                peek_node = stack[-1]
                if peek_node.right and last_visited_node != peek_node.right:
                    root = peek_node.right
                else:
                    result.append(peek_node.value)
                    last_visited_node = stack.pop()
        return result
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

dfs = DFS()
preorder_result = dfs.dfs_preorder(root)
inorder_result = dfs.inorder(root)
postorder_result = dfs.postorder(root)

print(f"Preorder traversal: {preorder_result}")
print(f"inorder traversal: {inorder_result}")
print(f"postorder traversal: {postorder_result}")

