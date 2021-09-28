class HashMap:
	def __init__(self, size=0):
		self.map = [None]*size
		self.size = size
		print("initializing a HashMap with size ({0})".format(size))

	# hash function
	def hash(self, key, collisions=0):
		r = 0
		for c in key:
			r += ord(c)
		return r + collisions
	
	# compression function
	def compress(self, value):
		return value % self.size

	# getters
	def get_map(self):
		return self.map
	def get_size(self):
		return self.size

	# metadata getters
	def get_available_space(self):
		return len([a for a in self.map if a is None])
	def get_used_space(self):
		return len([a for a in self.map if a is not None])

	# add an item to the HashMap
	def add_item(self, key, value):
		hash_index = self.compress(self.hash(key))
		resolved = self.map[hash_index]
		collisions = 0

		if resolved is None:
			self.map[hash_index] = [key, value]
			print("now added ({0}, {1}) to HashMap under the resolved index {2}".format(key, value, hash_index))
			return
		if resolved[0] == key:
			self.map[hash_index][1] = value
			print("existing key encountered, overwriting to use ({0}, {1}) to HashMap under the resolved index {2}".format(key, value, hash_index))
			return
		collisions += 1
		while (collisions <= self.size):
			print("index collision encountered at {0}: checking next index...".format(hash_index))
			hash_index = self.compress(self.hash(key, collisions))
			resolved = self.map[hash_index]
			if resolved is None:
				self.map[hash_index] = [key, value]
				print("now added ({0}, {1}) to HashMap under the resolved index {2}".format(key, value, hash_index))
				return
			if resolved[0] == key:
				self.map[hash_index][1] = value
				print("existing key encountered in the resolved index {0}, overwriting to use ({1}, {2})".format(hash_index, key, value))
				return
			collisions += 1
		print("cannot find an available index to store ({0}, {1}) in the HashMap; adding capacity to HashMap...".format(key, value))
		self.map.insert(hash_index, [key, value])
		self.size += 1
		print("now inserted ({0}, {1}) at the index {2}; HashMap size is now {3}".format(key, value, hash_index, self.size))
		return

	# retrieve an item from the HashMap
	def get_item(self, key):
		hash_index = self.compress(self.hash(key))
		resolved = self.map[hash_index]
		collisions = 0

		if resolved is None:
			print("cannot find value for the given key ({0})".format(key))
			return None
		if resolved[0] == key:
			print("found value ({0}) for the key ({1})".format(resolved[1], key))
			return resolved[1]
		collisions += 1
		while (collisions <= self.size):
			print("key not found at index ({0}); checking next available index...".format(hash_index))
			hash_index = self.compress(self.hash(key, collisions))
			resolved = self.map[hash_index]
			if resolved is None:
				print("cannot find value for the given key ({0})".format(key))
				return None
			if resolved[0] == key:
				print("found value ({0}) for the key ({1})".format(resolved[1], key))
				return resolved[1]
			collisions += 1
		print("cannot find value for the given key ({0})".format(key))
		return
		
	# remove a (key, value) pair given a key from the HashMap
	def remove_item(self, key):
		hash_index = self.compress(self.hash(key))
		resolved = self.map[hash_index]
		collisions = 0

		if resolved is None:
			print("cannot find value for the given key ({0}); skipping item removal".format(key))
			return None
		if resolved[0] == key:
			self.map[hash_index] = None
			print("removed key, value pair ({0}, {1}) from the HashMap".format(key, resolved[1]))
			return resolved[1]
		collisions += 1
		while (collisions <= self.size):
			print("key not found at index ({0}); checking next available index...".format(hash_index))
			hash_index = self.compress(self.hash(key, collisions))
			resolved = self.map[hash_index]
			if resolved is None:
				print("cannot find value for the given key ({0}); skipping item removal".format(key))
				return None
			if resolved[0] == key:
				self.map[hash_index] = None
				print("removed key, value pair ({0}, {1}) from the HashMap".format(key, resolved[1]))
				return resolved[1]
			collisions += 1
		print("cannot find value for the given key ({0}); skipping item removal".format(key))
		return

# ---------------- HashMap tests ----------------

print("\n----- test - initialize a HashMap\n")
myHashMap = HashMap(15)

print("\n----- test - add items to the HashMap\n")
myHashMap.add_item("Reimu", "Hakurei")
myHashMap.add_item("Hieda", "no Akyuu")
myHashMap.add_item("Yuyuko", "Saigyouji")
myHashMap.add_item("Remilia", "Scarlet")
myHashMap.add_item("Kasen", "Ibaraki")
myHashMap.add_item("Kosozu", "Motoori")
myHashMap.add_item("Koishi", "Komeiji")
myHashMap.add_item("Marisa", "Kirisame")
myHashMap.add_item("Reisen", "Udongein")
myHashMap.add_item("Patchouli", "Knowledge")
myHashMap.add_item("Sanae", "Kochiya")

print("\n----- test - get items from the HashMap\n")
myHashMap.get_item("Yuyuko")
myHashMap.get_item("Reimu")
myHashMap.get_item("Sanae")
myHashMap.get_item("Reisen")
myHashMap.get_item("Kasen")
myHashMap.get_item("Koishi")
myHashMap.get_item("Cirno")

print("\n----- test - overwrite an existing key in HashMap\n")
myHashMap.add_item("Reisen", "Udongein Inaba")
myHashMap.get_item("Reisen")

print("\n----- test - get metadata and attributes of the HashMap\n")
print("HashMap map: {0}".format(myHashMap.get_map()))
print("")
print("HashMap size: {0}".format(myHashMap.get_size()))
print("")
print("HashMap available space: {0}".format(myHashMap.get_available_space()))
print("")
print("HashMap used space: {0}".format(myHashMap.get_used_space()))

print("\n----- test - remove items from the HashMap\n")
myHashMap.remove_item("Patchouli")
myHashMap.remove_item("Yuyuko")
myHashMap.remove_item("Mai")

print("\n----- test - get updated metadata and attributes of the HashMap\n")
print("HashMap map: {0}".format(myHashMap.get_map()))
print("")
print("HashMap size: {0}".format(myHashMap.get_size()))
print("")
print("HashMap available space: {0}".format(myHashMap.get_available_space()))
print("")
print("HashMap used space: {0}".format(myHashMap.get_used_space()))

input()