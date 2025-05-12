#Topic 6: Trees & Binary Search Trees (BST)

#Task 1: Implementing a Binary Search Tree (BST) with Basic Operations

class TreeNode:
    """A node in the binary search tree."""
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    """Binary Search Tree implementation."""
    def __init__(self):
        self.root = None

    def insert(self, value):
        """Insert a new value into the BST."""
        if not self.root:
            self.root = TreeNode(value)
        else:
            self._insert_recursively(self.root, value)

    def _insert_recursively(self, node, value):
        """Helper method to insert a value recursively."""
        if value < node.value:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self._insert_recursively(node.left, value)
        else:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self._insert_recursively(node.right, value)

    def search(self, value):
        """Search for a value in the BST."""
        return self._search_recursively(self.root, value)

    def _search_recursively(self, node, value):
        """Helper method to search for a value recursively."""
        if node is None or node.value == value:
            return node is not None
        if value < node.value:
            return self._search_recursively(node.left, value)
        else:
            return self._search_recursively(node.right, value)

    def delete(self, value):
        """Delete a value from the BST."""
        self.root = self._delete_recursively(self.root, value)

    def _delete_recursively(self, node, value):
        """Helper method to delete a value recursively."""
        if node is None:
            return node

        if value < node.value:
            node.left = self._delete_recursively(node.left, value)
        elif value > node.value:
            node.right = self._delete_recursively(node.right, value)
        else:
            # Node with only one child or no child
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            # Node with two children: Get the inorder successor (smallest in the right subtree)
            min_larger_node = self._min_value_node(node.right)
            node.value = min_larger_node.value
            node.right = self._delete_recursively(node.right, min_larger_node.value)

        return node

    def _min_value_node(self, node):
        """Get the node with the minimum value greater than the current node."""
        current = node
        while current.left is not None:
            current = current.left
        return current

    def inorder_traversal(self):
        """Print the elements of the BST in ascending order."""
        elements = []
        self._inorder_recursively(self.root, elements)
        print(" ".join(map(str, elements)))

    def _inorder_recursively(self, node, elements):
        """Helper method for inorder traversal."""
        if node:
            self._inorder_recursively(node.left, elements)
            elements.append(node.value)
            self._inorder_recursively(node.right, elements)

# Test the Binary Search Tree
def test_bst():
    bst = BinarySearchTree()
    numbers = [50, 30, 70, 20, 40, 60, 80]
    
    for number in numbers:
        bst.insert(number)

    print("Inorder Traversal after insertions:")
    bst.inorder_traversal()  # Expected Output: 20 30 40 50 60 70 80

    print("Search for 40:", bst.search(40))  # Expected Output: True
    print("Search for 90:", bst.search(90))  # Expected Output: False

    bst.delete(20)  # Deleting leaf node
    print("Inorder Traversal after deleting 20:")
    bst.inorder_traversal()  # Expected Output: 30 40 50 60 70 80

    bst.delete(30)  # Deleting node with one child
    print("Inorder Traversal after deleting 30:")
    bst.inorder_traversal()  # Expected Output: 40 50 60 70 80

    bst.delete(50)  # Deleting node with two children
    print("Inorder Traversal after deleting 50:")
    bst.inorder_traversal()  # Expected Output: 40 60 70 80

# Run the test cases
test_bst()


#Task 2: Finding the Lowest Common Ancestor (LCA) in a BST
class TreeNode:
    """A node in the binary search tree."""
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    """Binary Search Tree implementation."""
    def __init__(self):
        self.root = None

    def insert(self, value):
        """Insert a new value into the BST."""
        if not self.root:
            self.root = TreeNode(value)
        else:
            self._insert_recursively(self.root, value)

    def _insert_recursively(self, node, value):
        """Helper method to insert a value recursively."""
        if value < node.value:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self._insert_recursively(node.left, value)
        else:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self._insert_recursively(node.right, value)

    def find_lca(self, n1, n2):
        """Find the Lowest Common Ancestor of n1 and n2."""
        return self._find_lca_recursively(self.root, n1, n2)

    def _find_lca_recursively(self, node, n1, n2):
        """Helper method to find LCA recursively."""
        if node is None:
            return None

        # If both n1 and n2 are smaller than node, LCA lies in left subtree
        if n1 < node.value and n2 < node.value:
            return self._find_lca_recursively(node.left, n1, n2)

        # If both n1 and n2 are greater than node, LCA lies in right subtree
        if n1 > node.value and n2 > node.value:
            return self._find_lca_recursively(node.right, n1, n2)

        # If we reach here, then node is the LCA
        return node.value

# Test the LCA function
def test_lca():
    bst = BinarySearchTree()
    values = [20, 10, 30, 5, 15, 25, 35]
    
    for value in values:
        bst.insert(value)

    print("LCA(5, 15):", bst.find_lca(5, 15))  # Expected Output: 10
    print("LCA(5, 25):", bst.find_lca(5, 25))  # Expected Output: 20
    print("LCA(25, 35):", bst.find_lca(25, 35))  # Expected Output: 30
    print("LCA(10, 30):", bst.find_lca(10, 30))  # Expected Output: 20
    print("LCA(5, 10):", bst.find_lca(5, 10))  # Expected Output: 10

# Run the test cases
test_lca()

#Task 3: Checking if a Binary Tree is Balanced

class TreeNode:
    """A node in the binary tree."""
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def is_balanced(root: TreeNode) -> bool:
    """Check if the binary tree is height-balanced."""
    
    def check_balance_and_height(node: TreeNode):
        """Helper function to check balance and compute height."""
        if node is None:
            return 0, True  # Height is 0 and balanced

        left_height, left_balanced = check_balance_and_height(node.left)
        right_height, right_balanced = check_balance_and_height(node.right)

        # Current node is balanced if the left and right subtrees are balanced
        # and the height difference is at most 1
        current_balanced = left_balanced and right_balanced and abs(left_height - right_height) <= 1

        # Height of the current node is max height of left/right + 1
        current_height = max(left_height, right_height) + 1

        return current_height, current_balanced

    # Start the recursive check from the root
    _, balanced = check_balance_and_height(root)
    return balanced

# Test the is_balanced function
def test_is_balanced():
    # Balanced Tree
    root1 = TreeNode(10)
    root1.left = TreeNode(5)
    root1.right = TreeNode(15)
    root1.left.left = TreeNode(2)
    root1.left.right = TreeNode(7)
    root1.right.left = TreeNode(12)
    root1.right.right = TreeNode(20)

    print("Tree 1 is balanced:", is_balanced(root1))  # Expected Output: True

    # Unbalanced Tree
    root2 = TreeNode(10)
    root2.left = TreeNode(5)
    root2.left.left = TreeNode(2)

    print("Tree 2 is balanced:", is_balanced(root2))  # Expected Output: False

    # Another Balanced Tree
    root3 = TreeNode(1)
    root3.left = TreeNode(2)
    root3.right = TreeNode(3)
    root3.left.left = TreeNode(4)
    root3.left.right = TreeNode(5)

    print("Tree 3 is balanced:", is_balanced(root3))  # Expected Output: True

    # Another Unbalanced Tree
    root4 = TreeNode(1)
    root4.left = TreeNode(2)
    root4.left.left = TreeNode(3)
    root4.left.left.left = TreeNode(4)

    print("Tree 4 is balanced:", is_balanced(root4))  # Expected Output: False

# Run the test cases
test_is_balanced()