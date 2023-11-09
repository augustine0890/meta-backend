import random
from collections import deque


class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = TreeNode(value)
        # Check if the BST is empty
        if not self.root:
            self.root = new_node
            return self

        current_node = self.root
        while value != current_node.data:
            # Check if the data to insert is smaller than the current node's data
            if value < current_node.data:
                if not current_node.left:
                    current_node.left = new_node
                    break
                current_node = current_node.left
            # Check if the data to insert is greater than the current node's data
            else:
                if not current_node.right:
                    current_node.right = new_node
                    break
                current_node = current_node.right
        return self

    def find_min(self):
        # Set current_node as the root
        current_node = self.root
        # Iterate over the nodes of the appropriate subtree
        while current_node.left:
            # Update current_node
            current_node = current_node.left
        return current_node.data

    def breadth_first_traversal(self):
        if not self.root:
            raise Exception("Tree is empty")
        # queue = deque()
        queue = []
        queue.append(self.root)
        visited = []
        while queue:
            # visited_node = queue.popleft()
            visited_node = queue[0]
            queue = queue[1:]
            visited.append(visited_node.data)
            if visited_node.left:
                queue.append(visited_node.left)
            if visited_node.right:
                queue.append(visited_node.right)
        return visited

    def in_order(self, current_node=None):
        if current_node is None:
            current_node = self.root

        res = []
        # Check if current_node exists
        if current_node:
            # Call recursively with the appropriate half of the tree
            self.in_order(current_node.left_child)
            res.append(current_node.data)
            # Call recursively with the appropriate half of the tree
            self.in_order(current_node.right_child)
        return res

    def print_tree(self, node=None, level=0):
        if not node:
            node = self.root
        if node.right:
            self.print_tree(node.right, level + 1)
        print(node.data, end=" ")
        if node.left:
            self.print_tree(node.left, level + 1)


def create_rand_binary_tree(n, k):
    values = [k * (v + 1) for v in range(n)]
    bst = BinarySearchTree()
    random.shuffle(values)
    for value in values:
        bst.insert(value)
    return bst


bst = create_rand_binary_tree(10, 2)
bst.print_tree()
print("\n", bst.find_min())
print(bst.breadth_first_traversal())
