class EmptyCollection(Exception):
    pass
class ArrayStack:
    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return len(self) == 0

    def push(self, val):
        self.data.append(val)

    def top(self):
        if (self.is_empty()):
            raise Empty("Stack is empty")
        return self.data[-1]

    def pop(self):
        if (self.is_empty()):
            raise Empty("Stack is empty")
        return self.data.pop()
class double_ended_queue:
	'''
	Elements can be inserted/removed at front and back of queue. Standard operations still run in O(1) amortized runtime.
	'''
	def __init__(self):
		self.front = 0
		self.rear = 0
		self.data = []
	def add_first(self, val):
		if self.front > self.rear:				#if front looped around before rear
			if self.rear == self.front-1:		#check if space available before
				self.resize()
				self.front = len(self.data)-1	#make first equal to last index
				self.data[self.front] = val
			else:								#space available to add at front-1
				self.front -= 1
				self.data[self.front] = val
		elif self.rear > self.front:			#front has no looped around yet
			if self.front == 0:					#check if spaces before 0 are available
				self.resize()
				self.front = len(self.data)-1	#make front point to last index
				self.data[self.front] = val
			else:								#space available, not at beginning
				self.front -= 1
				self.data[self.front] = val
		else:
			self.data.append(val)
			if (len(self) == 2):
				self.front = 1
				self.rear = 0

	def add_last(self, val):
		if self.front > self.rear:			#front loop around before rear
			if self.rear == self.front-1:	#no space available to add at rear
				self.resize()
				self.rear += 1
				self.data[self.rear] = val
			else:							#space available, insert at end
				self.rear += 1
				self.data[self.rear] = val
		elif self.rear > self.front:
			if self.rear == len(self.data)-1:	#at the last index
				self.resize()
				self.rear += 1
				self.data[self.rear] = val
			else:							#not at last index, space available at end
				self.rear += 1
				self.data[self.rear] = val
		else:
			self.data.append(val)
			if (len(self) == 2):
				self.rear = 1
				self.front = 0

	def delete_first(self):
		if self.is_Empty():
			raise IndexException('empty double_ended_queue')
		number = self.data[self.front]
		self.data[self.front] = None
		self.front += 1
		if self.is_Empty():					#reset back to everything when empty
			self.front = 0
			self.rear = 0
			self.data = []
		return number

	def delete_last(self):
		if self.is_Empty():
			raise IndexException('empty double_ended_queue')
		number = self.data[self.rear]
		self.data[self.rear] = None
		self.rear -= 1
		if self.is_Empty():					#reset back to everything when empty
			self.front = 0
			self.rear = 0
			self.data = []
		return number

	def resize(self):								#sort numbers in front to last order. double space.
		old_data = self.data[:]
		self.data = [None] * (len(self) * 2)
		if self.front > self.rear:					#front numbers are at end
			first_half = old_data[self.front:]
			second_half = old_data[:self.rear+1]
			index = 0
			for elem in first_half:
				self.data[index] = elem
				index += 1
			for elem in second_half:
				self.data[index] = elem
				index += 1
			self.front = 0							#front is zero and rear is pointing to last index
			self.rear = len(old_data)-1
		elif self.rear > self.front:				#in inserted order, that needs more space.
			index = 0
			for elem in old_data:
				self.data[index] = elem
				index += 1
			self.front = 0
			self.rear = len(old_data)-1

	def __len__(self):
		count = 0
		for elem in self.data:
			if elem is not None:
				count += 1
		return count

	def __str__(self):
		return str(self.data)

	def is_Empty(self):
		return len(self) == 0
class MidStack:
    def __init__(self):
        self.s = ArrayStack()
        self.q = double_ended_queue()
    def is_empty(self):
        return len(self.s) == 0
    def len(self):
        return len(self.s)
    def push(self, e):
        self.s.push(e)
    def top(self):
        if (self.s.is_empty()):
            raise EmptyCollection('MidStack is empty')
        return self.s.top()
    def pop(self):
        if(self.s.is_empty()):
            raise EmptyCollection("Stack is empty")
        return self.s.pop()
    def mid_push(self, e):
        if len(self.s)%2 == 0:
            for x in range(int(len(self.s)/2 )):
                self.q.add_last(self.s.pop())
        elif len(self.s) % 2 != 0:
            for x in range( (int((len(self.s)+1)/2)) -1 ):
                self.q.add_last(self.s.pop())
        self.s.push(e)
        for x in range(len(self.q)):
            self.s.push(self.q.delete_last())
