import re


class Node (object):
	def __init__(self,initdata):
		self.data = initdata
		self.next = None          

	def getData (self):
		return self.data

	def getNext (self):
		return self.next           

	def setData (self, newData):
		self.data = newData        

	def setNext (self,newNext):
		self.next = newNext        

class UnorderedList ():

	def __init__(self):
		self.head = None


	def isEmpty (self):
		return self.head == None

	def add (self,item):
		# add a new Node to the beginning of an existing list
		temp = Node(item)
		temp.setNext(self.head)
		self.head = temp

	def getLast(self):

		previous = None
		current = self.head

		while current != None:
			previous = current
			current = current.getNext()

		return previous

	def length (self):
		current = self.head
		count = 0

		while current != None:
			count += 1
			current = current.getNext()

		return count

	def search (self,item):
		current = self.head
		found = False

		while current != None and not found:
			if current.getData() == item:
				found = True
			else:
				current = current.getNext()

		return found

	def remove (self,item):
		current = self.head
		previous = None
		found = False

		while not found:
			if current.getData() == item:
				found = True
			else:
				previous = current
				current = current.getNext()

		if previous == None:
			self.head = current.getNext()
		else:
			previous.setNext(current.getNext() ) 

def create_list(self,names):

	for ind, item in enumerate(list):

		lastIndex = len(names) - 1

	
	




def main():
	names = open('HotPotatoData.txt','r')
	lines = names.readlines()
	finalArr = []
	addArr = []
	startoff = True
	for line in lines:
		if re.match(r'\d+', line):
			nums = re.findall(r'\d+', line)
			finalArr.append(nums[1])
			count = 0
			count_to = nums[1]
			addArr = []
		else:
			count += 1
			addArr.append(line[:-1])
			if count == int(count_to):
				finalArr.append(addArr)
	print(finalArr)
			


main()