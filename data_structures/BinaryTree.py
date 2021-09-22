class Node:
	def __init__(self, value, left=None, right=None):
		self.value = value
		self.left = left
		self.right = right
	# setters
	def set_value(self, value):
		self.value = value
	def set_left(self, left):
		self.left = left
	def set_right(self, right):
		self.right = right

class BinaryTree:
	# initialize tree with a root node
	def __init__(self, value=None):
		self.root = Node(value)
		print("initializing binary tree with root {0}".format(self.root))
	# getter [root node]
	def get_root(self):
		return self.root
	# add node to the tree
	def add_node(self, value):
		node_to_add = Node(value)
		nodes_to_search = [self.root]
		while (len(nodes_to_search) > 0):
			current_node = nodes_to_search.pop(0)
			for child in [current_node.left, current_node.right]:
				if current_node.left is None:
					current_node.set_left(node_to_add)
					print("adding node {0} as left child of {1}".format(node_to_add, current_node))
					return
				if current_node.right is None:
					current_node.set_right(node_to_add)
					print("adding node {0} as right child of {1}".format(node_to_add, current_node))
					return
				nodes_to_search.append(child)
	# get node with specified value
	def get_node(self, value):
		nodes_to_search = [self.root]
		while (len(nodes_to_search) > 0):
			current_node = nodes_to_search.pop(0)
			if current_node.value == value:
				print("found node {0} which contains value {1}".format(current_node, current_node.value))
				return current_node
			for child in [current_node.left, current_node.right]:
				if child is not None:
					nodes_to_search.append(child)
		print("cannot find node with value {0}".format(value))
		return None
	# print all the nodes in the tree
	def print_nodes(self):
		nodes_to_search = [self.root]
		while (len(nodes_to_search) > 0):
			current_node = nodes_to_search.pop(0)
			print("found node {0} with value {1}".format(current_node, current_node.value))
			for child in [current_node.left, current_node.right]:
				if child is not None:
					nodes_to_search.append(child)
	# invert the tree
	def invert(self):
		parent_nodes = [self.root]
		while(len(parent_nodes) > 0):
			parent_node = parent_nodes.pop(0)
			tmp_left = parent_node.left
			parent_node.set_left(parent_node.right)
			parent_node.set_right(tmp_left)
			print("switching {0} with {1}".format(parent_node.left, parent_node.right))
			for child in [parent_node.left, parent_node.right]:
				if child is not None:
					parent_nodes.append(child)

print("\n----- test - initializing tree")
myBinaryTree = BinaryTree("node_1")

print("\n----- test - adding nodes to tree")
myBinaryTree.add_node("node_2")
myBinaryTree.add_node("node_3")
myBinaryTree.add_node("node_4")
myBinaryTree.add_node("node_5")
myBinaryTree.add_node("node_6")
myBinaryTree.add_node("node_7")
myBinaryTree.add_node("node_8")
myBinaryTree.add_node("node_9")
myBinaryTree.add_node("node_10")
myBinaryTree.add_node("node_11")
myBinaryTree.add_node("node_12")
myBinaryTree.add_node("node_13")
myBinaryTree.add_node("node_14")
myBinaryTree.add_node("node_15")
myBinaryTree.add_node("node_16")

print("\n----- test - print all nodes in the tree")
myBinaryTree.print_nodes()

print("\n----- test - breadth-first search for a node with a specified value")
myBinaryTree.get_node("node_8")
myBinaryTree.get_node("node_6")
myBinaryTree.get_node("node_20")
myBinaryTree.get_node("node_1")
myBinaryTree.get_node("node_16")

print("\n----- test - invert a binary tree")
myBinaryTree.invert()

input()