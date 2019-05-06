import time 
from numpy.random import seed 
from numpy.random import randint 
import matplotlib.pyplot as plt 

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

def words_to_array(dict_path, n):
	num = 0;
	# Read the dict from thie given file
	f = open(dict_path, "r")
	line = f.readline().strip()
	#     line = line.split(" ")[0]
	words = []
	while line != "" and num >= n:
		words.append(line)
		line = f.readline()
		line = line.split(" ")[0]
		num += 1
	f.close()
	return words
    
def words_to_hash(words, n):
    # Write to the hashtable
	hash = hashTable(n)
	for w in words:
		hash.insert(w)
	return hash

def init(dict_path, n):
	words = []
	words = words_to_array(dict_path,n)
	hash = words_to_hash(words, n)

	return hash


def main():
	hash = init(dict_path = "dict.txt", n = 50)
	print("complete")

	res = input("Please enter a word (enter empty words to exit by default):")
	while res != "":
		res = res.strip()
		# Check whether res exists in TST
		find_w = hash.search(res)
		if find_w:                                  # Exist
			print(res + " ——no spelling errors")
		else:
			print(res + " ——misspelled")
		res = input("Please enter a word (enter empty words to exit by default):")
	print("Exit")

def run_time_search():
	elements = list() 
	times = list() 
	for i in range(100, 1000, 100): 
		words = words_to_array("dict.txt",i)
		
		hash = words_to_hash(words, i)
		start = time.clock()
		for w in words:
			find_w = hash.search(w)
		end = time.clock()

		elements.append(i)
		times.append(end-start)

	plt.xlabel('Number of words') 
	plt.ylabel('Time Complexity') 
	plt.plot(elements, times, label ='Searching Time') 
	plt.grid() 
	plt.legend() 
	plt.show() 

def run_time_insert():
	elements = list() 
	times = list() 
	for i in range(100, 1000, 100): 
		words = words_to_array("dict.txt",i)
		start = time.clock()
		hash = words_to_hash(words, i)
		end = time.clock()

		elements.append(i)
		times.append(end-start)

	plt.xlabel('Number of words') 
	plt.ylabel('Time Complexity') 
	plt.plot(elements, times, label ='Inserting Time') 
	plt.grid() 
	plt.legend() 
	plt.show() 

if __name__ == "__main__":
	run_time_insert()
	run_time_search()
