class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next
	# getters
	def get_value(self):
		return self.value
	def get_next(self):
		return self.next
	# setters
	def set_value(self, value):
		self.value = value
	def set_next(self, next):
		self.next = next

class LinkedList:
	# initialize LinkedList with one node
	def __init__(self, value=None):
		self.head = Node(value)
		self.tail = self.head
		print("initialized LinkedList with starting head node {0}".format(self.head))
	# get the head (root) node
	def get_head(self):
		return self.head
	# get the tail (ending) node
	def get_tail(self):
		return self.tail
	# set the head (root) node
	def set_head(self, node):
		self.head = node
	# set the tail (ending) node
	def set_tail(self, node):
		self.tail = node
	# add a node to the LinkedList
	def add_node(self, value, location='head'):
		node_to_add = Node(value)
		if location == 'head':
			node_to_add.set_next(self.head)
			self.head = node_to_add
			print("linked node {0} to {1}".format(node_to_add, self.head.get_next()))
			return
		if location == 'tail':
			current_node = self.head
			while(current_node.get_next() is not None):
				current_node = current_node.get_next()
			current_node.set_next(node_to_add)
			self.tail = node_to_add
			print("linked node {0} to {1}".format(current_node, self.tail))
			return
		print('invalid location parameter - {0}; it should either be "head" or "tail"'.format(location))
	# remove a node to the LinkedList
	def remove_node(self, location='head'):
		if location == 'head':
			current_node = self.head
			self.head = current_node.get_next()
			current_node.set_next(None)
			print("removed head node; setting head node to {0}".format(self.head))
			return
		if location == 'tail':
			current_node = self.head
			while current_node is not None:
				if current_node.get_next().get_next() == None:
					break
				current_node = current_node.get_next()
			self.tail = current_node
			current_node.set_next(None)
			print("removed tail node; setting tail node to {0}".format(self.tail))
			return
		print('invalid location parameter - {0}; it should either be "head" or "tail"'.format(location))
	# get the nth node starting from the head node
	def get_nth_node(self, n):
		current = self.get_head()
		counter = 0
		while(current is not None):
			if (counter == n):
				print("found node {0} at location {1}".format(current, n))
				return current
			current = current.get_next()
			counter += 1
		print("could not find node at location {0} in LinkedList".format(n))
		return
	# get the node containing a specified value
	def get_node(self, value):
		current = self.get_head()
		while(current is not None):
			if (current.value == value):
				print("found node {0} with value {1}".format(current, value))
				return current
			current = current.get_next()
		print("could not find node with value {0} in the LinkedList".format(value))
		return
	# print all the nodes and their respective values
	def print_nodes(self):
		current = self.get_head()
		while(current is not None):
			print("node {0} | value {1}".format(current, current.value))
			current = current.get_next()
		return
	# reverse the list (mutating)
	def reverse(self):
		current_node = self.get_head()
		self.set_tail(current_node)
		next_node = current_node.get_next()
		previous_node = None
		while next_node is not None:
			next_node = current_node.get_next()
			current_node.set_next(previous_node)
			print("setting node {0} to reference {1}".format(current_node, previous_node))
			previous_node = current_node
			current_node = next_node
		self.set_head(previous_node)
		print("reversed LinkedList - head is {0} | tail is {1}".format(self.head, self.tail))
	# ----------------------------------------------
	# implement Queue (FIFO) using LinkedList
	# ----------------------------------------------
	# queue nodes
	def queue(self, value=None, location='head'):
		node_to_add = Node(value)
		if location == 'head':
			node_to_add.set_next(self.head)
			self.head = node_to_add
			print("queue-ing node {0} from head Queue; setting head node to {1}".format(node_to_add, self.head))
			return
		if location == 'tail':
			self.tail.next = node_to_add
			self.tail = self.tail.next
			print("queue-ing node {0} from tail Queue; setting tail node to {1}".format(node_to_add, self.tail))
			return
		print('invalid location parameter - {0}; it should either be "head" or "tail"'.format(location))
	# dequeue nodes
	def dequeue(self, location='head'):
		if location == 'head':
			current_node = self.head
			while(current_node is not None):
				if current_node.get_next().get_next() == None:
					break
				current_node = current_node.get_next()
			self.tail = current_node
			self.tail.set_next(None)
			print("dequeue-ing node from head Queue; setting tail node to {0}".format(self.tail))
			return
		if location == 'tail':
			current_node = self.head
			next_node = current_node.get_next()
			self.head = next_node
			current_node.set_next(None)
			print("dequeue-ing node from tail Queue; setting head node to {0}".format(self.head))
			return
		print('invalid location parameter - {0}; it should either be "head" or "tail"'.format(location))
	# ----------------------------------------------
	# implement Stack (FILO) using LinkedList
	# ----------------------------------------------
	# stack nodes
	def stack(self, value=None, location='head'):
		node_to_add = Node(value)
		if location == 'head':
			node_to_add.set_next(self.head)
			self.head = node_to_add
			print("queue-ing node {0} from head Stack; setting head node to {1}".format(node_to_add, self.head))
			return
		if location == 'tail':
			self.tail.next = node_to_add
			self.tail = self.tail.next
			print("queue-ing node {0} from tail Stack; setting tail node to {1}".format(node_to_add, self.tail))
			return
		print('invalid location parameter - {0}; it should either be "head" or "tail"'.format(location))
	# destack nodes
	def destack(self, location='head'):
		if location == 'head':
			current_node = self.head
			self.head = current_node.get_next()
			current_node.set_next(None)
			print("destack-ing node from head Stack; setting head node to {0}".format(self.head))
			return
		if location == 'tail':
			current_node = self.head
			while (current_node.get_next() is not None):
				if current_node.get_next().get_next() == None:
					break
				current_node = current_node.get_next()
			self.tail = current_node
			self.tail.set_next(None)
			print("destack-ing node from tail Stack; setting tail node to {0}".format(self.tail))
			return
		print('invalid location parameter - {0}; it should either be "head" or "tail"'.format(location))

print("----- test - initialize a LinkedList")
myLinkedList = LinkedList("item_1")

print("\n----- test - add nodes at head")
myLinkedList.add_node("item_2")
myLinkedList.add_node("item_3")
myLinkedList.add_node("item_4")
myLinkedList.add_node("item_5")
myLinkedList.add_node("item_6")
myLinkedList.add_node("item_7")
myLinkedList.add_node("item_8")

print("\n----- test - print the attributes of all nodes")
myLinkedList.print_nodes()

print("\n----- test - add nodes at tail")
myLinkedList.add_node("item_t1", "tail")
myLinkedList.add_node("item_t2", "tail")
myLinkedList.add_node("item_t3", "tail")
myLinkedList.add_node("item_t4", "tail")
myLinkedList.add_node("item_t5", "tail")
myLinkedList.add_node("item_t6", "tail")

print("\n----- printing all nodes")
myLinkedList.print_nodes()

print("\n----- test - get the nth node")
myLinkedList.get_nth_node(0)
myLinkedList.get_nth_node(3)
myLinkedList.get_nth_node(9)
myLinkedList.get_nth_node(25)

print("\n----- test - search for nodes with a specified value")
myLinkedList.get_node("item_1")
myLinkedList.get_node("item_4")
myLinkedList.get_node("item_t5")
myLinkedList.get_node("item_36")

print("\n----- test - reverse the list items")
myLinkedList.reverse()

print("\n----- printing all nodes")
myLinkedList.print_nodes()

print("\n----- test - remove node from head")
myLinkedList.remove_node()
myLinkedList.print_nodes()

print("\n----- test - remove node from tail")
myLinkedList.remove_node('tail')
myLinkedList.print_nodes()

print("\n\n------------------------------------\n\
----------- Queue [FIFO] -----------\n\
------------------------------------\n")

print("\n----- test - queue from head Queue")
myLinkedList.queue('queue_from_head')
myLinkedList.print_nodes()

print("\n----- test - dequeue from head Queue")
myLinkedList.dequeue()
myLinkedList.print_nodes()

print("\n----- test - queue from tail Queue")
myLinkedList.queue('queue_from_tail', 'tail')
myLinkedList.print_nodes()

print("\n----- test - dequeue from tail Queue")
myLinkedList.dequeue('tail')
myLinkedList.print_nodes()

print("\n\n------------------------------------\n\
----------- Stack [FILO] -----------\n\
------------------------------------\n")

print("\n----- test - stack from head Stack")
myLinkedList.stack('stack_from_head')
myLinkedList.print_nodes()

print("\n----- test - destack from head Stack")
myLinkedList.destack()
myLinkedList.print_nodes()

print("\n----- test - stack from tail Stack")
myLinkedList.stack('stack_from_tail', 'tail')
myLinkedList.print_nodes()

print("\n----- test - destack from tail Stack")
myLinkedList.destack('tail')
myLinkedList.print_nodes()

input()