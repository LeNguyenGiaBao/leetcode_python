class Node:
	def __init__(self, value):
		self.value = value
		self.left = None 
		self.right = None 

class BinaryTree:
	def __init__(self, value=None):
		self.root = value 

	def insert(self, value):
		if self.root is None:
			self.root = Node(value)
		else:
			self._insert_recursive(self.root, value)

	def _insert_recursive(self, node, value):
		if node.value < value:
			if node.right is None:
				node.right = Node(value)
			else:
				self._insert_recursive(node.right, value)
		else:
			if node.left is None:
				node.left = Node(value)
			else:
				self._insert_recursive(node.left, value)

	def inorder_traversal(self, node):
		if node:
			self.inorder_traversal(node.left)
			print(node.value, end=" ")
			self.inorder_traversal(node.right)


# Example Usage
tree = BinaryTree()
tree.insert(10)
tree.insert(5)
tree.insert(15)
tree.insert(3)
tree.insert(7)

print("Inorder Traversal:")
tree.inorder_traversal(tree.root)  # Output: 3 5 7 10 15
