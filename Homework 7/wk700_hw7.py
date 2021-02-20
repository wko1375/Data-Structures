import math
class ArrayQueue:
    INITIAL_CAPACITY = 10

    def __init__(self):
        self.data = [None] * ArrayQueue.INITIAL_CAPACITY
        self.num_of_elems = 0
        self.front_ind = 0

    def __len__(self):
        return self.num_of_elems

    def is_empty(self):
        return (self.num_of_elems == 0)

    def enqueue(self, elem):
        if (self.num_of_elems == len(self.data)):
            self.resize(2 * len(self.data))
        back_ind = (self.front_ind + self.num_of_elems) % len(self.data)
        self.data[back_ind] = elem
        self.num_of_elems += 1

    def dequeue(self):
        if (self.is_empty()):
            raise Empty("Queue is empty")
        value = self.data[self.front_ind]
        self.data[self.front_ind] = None
        self.front_ind = (self.front_ind + 1) % len(self.data)
        self.num_of_elems -= 1
        if(self.num_of_elems < len(self.data) // 4):
            self.resize(len(self.data) // 2)
        return value

    def first(self):
        if self.is_empty():
            raise Empty("Queue is empty")
        return self.data[self.front_ind]

    def resize(self, new_cap):
        old_data = self.data
        self.data = [None] * new_cap
        old_ind = self.front_ind
        for new_ind in range(self.num_of_elems):
            self.data[new_ind] = old_data[old_ind]
            old_ind = (old_ind + 1) % len(old_data)
        self.front_ind = 0
class Dequeue:
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
class EmptyTree(Exception):
    pass
class LinkedBinaryTree:
    class Node:
        def __init__(self, data, left=None, right=None):
            self.data = data
            self.left = left
            if (self.left is not None):
                self.left.parent = self
            self.right = right
            if (self.right is not None):
                self.right.parent = self
            self.parent = None
    def __init__(self, root=None):
        self.root = root
        self.size = self.subtree_count(self.root)
    def __len__(self):
        return self.size
    def is_empty(self):
        return (len(self) == 0)
    def subtree_count(self, subtree_root):
        if(subtree_root is None):
            return 0
        else:
            left_count = self.subtree_count(subtree_root.left)
            right_count = self.subtree_count(subtree_root.right)
            return left_count + right_count + 1
    def sum_tree(self):
        return self.subtree_sum(self.root)
    def subtree_sum(self, subtree_root):
        if(subtree_root is None):
            return 0
        else:
            left_sum = self.subtree_sum(subtree_root.left)
            right_sum = self.subtree_sum(subtree_root.right)
            return left_sum + right_sum + subtree_root.data
    def height(self):
        if (self.is_empty()):
            raise EmptyCollection("Height is not defined for an empty tree")
        return self.subtree_height(self.root)
    #assuming subtree_root is not empty
    def subtree_height(self, subtree_root):
        if((subtree_root.left is None) and (subtree_root.right is None)):
            return 0
        elif(subtree_root.left is None):
            return 1 + self.subtree_height(subtree_root.right)
        elif(subtree_root.right is None):
            return 1 + self.subtree_height(subtree_root.left)
        else:
            left_height = self.subtree_height(subtree_root.left)
            right_height = self.subtree_height(subtree_root.right)
            return 1 + max(left_height, right_height)
    def preorder(self):
        yield from self.subtree_preorder(self.root)
    def subtree_preorder(self, subtree_root):
        if(subtree_root is None):
            return
        else:
            yield subtree_root
            yield from self.subtree_preorder(subtree_root.left)
            yield from self.subtree_preorder(subtree_root.right)
    def postorder(self):
        yield from self.subtree_postorder(self.root)
    def subtree_postorder(self, subtree_root):
        if(subtree_root is None):
            return
        else:
            yield from self.subtree_postorder(subtree_root.left)
            yield from self.subtree_postorder(subtree_root.right)
            yield subtree_root
    def inorder(self):
        yield from self.subtree_inorder(self.root)
    def subtree_inorder(self, subtree_root):
        if(subtree_root is None):
            return
        else:
            yield from self.subtree_inorder(subtree_root.left)
            yield subtree_root
            yield from self.subtree_inorder(subtree_root.right)
    def __iter__(self):
        for node in self.inorder():
            yield node.data
    def breadth_first(self):
        if(self.is_empty()):
            return
        nodes_q = ArrayQueue()
        nodes_q.enqueue(self.root)
        while(nodes_q.is_empty() == False):
            curr_node = nodes_q.dequeue()
            yield curr_node
            if (curr_node.left is not None):
                nodes_q.enqueue(curr_node.left)
            if (curr_node.right is not None):
                nodes_q.enqueue(curr_node.right)
    def add_right(root, node):
        root.right = node
    def add_left(root, node):
        root.left = node
    def leaves_list(self):
        if self.root == None:
            return []
        else:
            return subtree_leaves_list(self.root)
    def iterative_inorder(self):
        parent = self.root
        n = None
        while None != parent:
            if None == parent.left:
                yield parent.data
                parent = parent.right
            else:
                n = parent.left
                while None != n.right and parent != n.right:
                    n = n.right
                if None == n.right:
                    n.right = parent
                    parent = parent.left
                else:
                    yield parent.data
                    n.right = None
                    parent = parent.right
def subtree_leaves_list(root):
    lst = []
    if root.left == None and root.right == None:
        lst.append(root.data)
        return lst
    elif root.left != None and root.right != None:
        lst.extend(subtree_leaves_list(root.left))
        lst.extend(subtree_leaves_list(root.right))
        return lst
    elif root.left != None:
        lst.extend(subtree_leaves_list(root.left))
        return lst
    else:
        lst.extend(subtree_leaves_list(root.right))
        return lst
def min_and_max(bin_tree):
    if bin_tree.root == None:
        raise EmptyTree('Binary Tree is Empty')
    else:
        return subtree_min_and_max(bin_tree, bin_tree.root)
def subtree_min_and_max(bin_tree, subtree_root):
    if subtree_root.left is None and subtree_root.right is None:
        tup = (subtree_root.data, subtree_root.data)
        return tup
    elif subtree_root.right is None:
        left = subtree_min_and_max(bin_tree, subtree_root.left)
        tup = (left[0], left[1])
        if subtree_root.data > tup[1]:
            tup = (tup[0], subtree_root.data)
        if subtree_root.data < tup[0]:
            tup = (subtree_root.data, tup[1])
        return tup
    elif subtree_root.left is None:
        right = subtree_min_and_max(bin_tree, subtree_root.right)
        tup = (right[0], right[1])
        if subtree_root.data > tup[1]:
            tup = (tup[0], subtree_root.data)
        if subtree_root.data < tup[0]:
            tup = (subtree_root.data, tup[1])
        return tup
    else:
        left = subtree_min_and_max(bin_tree, subtree_root.left)
        right = subtree_min_and_max(bin_tree, subtree_root.right)
        if left[0] < right[0]:
            mini = left[0]
        else:
            mini = right[0]
        if left[1] > right[1]:
            maxi = left[1]
        else:
            maxi = right[1]
        tup = (mini, maxi)
        if subtree_root.data < tup[0]:
            mini = subtree_root.data
        if subtree_root.data > tup[1]:
            maxi = subtree_root.data
        tup = (mini, maxi)
        return tup
def is_height_balanced(bin_tree):
    return 1 + (subtree_height(bin_tree.root.left) - subtree_height(bin_tree.root.right)) <= 1
def subtree_height(root):
    if root.left == None and root.right == None:
        return 0
    elif root.left != None and root.right != None:
        return 1 + max(subtree_height(root.left), subtree_height(root.right))
    elif root.left == None:
        return 1 + subtree_height(root.right)
    elif root.right == None:
        return 1 + subtree_height(root.left)
def is_operation(str_input):
    if str_input == '+':
        return True
    if str_input == '-':
        return True
    if str_input == '*':
        return True
    if str_input == '/':
        return True
    else:
        return False
def create_expression_tree(prefix_exp_str):
    if prefix_exp_str.is_empty():
        x = LinkedBinaryTree()
        return x
    else:
        exp_lst = [elem for elem in prefix_exp_str if elem != ' ']
        return create_expression_tree_helper(exp_lst, 0)
def create_expression_tree_helper(prefix_exp, start_pos):
    if prefix_exp[start_pos].isdigit():
        ''' add to the right of the last node'''
    else:
        tree.root = LinkedBinaryTree.Node(prefix_exp[start_pos
        ])
    if prefix_exp[start_pos] == '-':
        ''' split the rest of the list into two
            if there's an operation - do the recursive call again on that
        '''
    if prefix_exp[start_pos] == '+':
        '''

'''
def main():
    left3 = LinkedBinaryTree.Node(109)
    right3 = LinkedBinaryTree.Node(7)
    left2 = LinkedBinaryTree.Node(4)
    right2 = LinkedBinaryTree.Node(5)
    left4 = LinkedBinaryTree.Node(7)
    right4 = LinkedBinaryTree.Node(8)
    left1 = LinkedBinaryTree.Node(2, left2, right2)
    right1 = LinkedBinaryTree.Node(3, left3, right3)
    firstnode = LinkedBinaryTree.Node(1, left1, right1)
    tree = LinkedBinaryTree(firstnode)
    print(tree.iterative_inorder)
    for elem in tree.iterative_inorder():
        print(elem, end = ' ')
    print()
main()'''
