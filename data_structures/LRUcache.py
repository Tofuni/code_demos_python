class LRUcache:
	def __init__(self, capacity):
		self.capacity = capacity
		self.cache = []

	def get(self, key):
		keys = [i[0] for i in self.cache]
		if key in keys:
			k = keys.index(key)
			print(f"item with key ({key}) found with value ({self.cache[k][1]})")
			return self.cache[k][1]
		print(f"cannot find value for item with key: ({key})")
		return -1

	def set(self, key, value):
		keys = [i[0] for i in self.cache]
		if key in keys:
			k = keys.index(key)
			del self.cache[k]
		self.cache.append([key, value])
		if len(self.cache) > self.capacity:
			self.cache.pop(0)
		return

	def __repr__(self):
		return str(self.cache)

myCache = LRUcache(5)
myCache.set(0,'ini_0')
myCache.set(1,'ini_1')
myCache.set(2,'ini_2')
myCache.set(3,'ini_3')
myCache.set(4,'ini_4')
myCache.set(5,'ini_5')
print(myCache)
myCache.get(1)
myCache.get(2)
myCache.get(5)
myCache.get(6)

myCache.set(6,'ini_6')
myCache.set(7,'ini_7')
myCache.set(8,'ini_8')
myCache.set(9,'ini_9')
print(f"\n-----\n\n{myCache}")
myCache.get(2)
myCache.get(4)
myCache.get(8)

myCache.set(5,'new_5')
myCache.set(9,'new_9')
myCache.set(8,'new_8')
print(f"\n-----\n\n{myCache}")
myCache.get(4)
myCache.get(8)
myCache.get(9)

input()