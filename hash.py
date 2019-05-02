class hashTable:
	def __init__(self,size):
		self.table = [[] for _ in range(size)]

	def insert(self, value):
		key = hash(value) % len(self.table)
		exists = False	
		bucket = self.table[key]    
		for i, v in enumerate(bucket):
			if value == v:
				exists = True 
				break
		if not exists:
			bucket.append(value)

	def search(self, value):
		key = hash(value) % len(self.table)    
		bucket = self.table[key]
		for i, v in enumerate(bucket):
			if value == v:
				return True
		return False

def init(dict_path):
	hash = hashTable(100)
	# Read the dict from thie given file
	f = open(dict_path, "r")
	line = f.readline().strip()
	#     line = line.split(" ")[0]
	words = []
	while line != "":
		words.append(line)
		line = f.readline()
		line = line.split(" ")[0]
	f.close()
    
    # Write to the TST
	for w in words:
		hash.insert(w)
	return hash

if __name__ == "__main__":
	hash = init(dict_path = "dict.txt")
	print("complete")

	res = input("Please enter a word (enter empty words to exit by default):")
	while res != "":
		res = res.strip()
		# Check whether res exists in TST
		find_w, _, _ = t.find(res)
		if find_w == True:                                  # Exist
			print(res + " ——no spelling errors")
		else:
			print(res + " ——misspelled, it is recommended to change to the following words:")
			res = input("Please enter a word (enter empty words to exit by default):")
	print("Exit")