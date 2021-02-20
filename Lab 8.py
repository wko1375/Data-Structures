class EmptyException(Exception):
    pass
class LinkedStack:
    class Node:
        def __init__(self, data= None, next = None, prev = None):
            self.data = data
            self.next = next
            self.prev = prev
    def __init__(self):
        self.header  = LinkedStack.Node()
        self.trailer = LinkedStack.Node()
        self.header.next = self.trailer
        self.trailer.prev = self.header
        self.size = 0
    def push(self, e):
        return self.add_after(self.trailer.prev, elem)
    def pop(self):
        if self.is_empty():
            raise EmptyException('LinkedStack is empty')
        return delete(self, self.trailer.prev)
    def top(self):
        if self.is_empty():
            raise EmptyException('LinkedStack is empty')
        return self.trailer.prev.data
    def is_empty(self):
        return (len(self) == 0)
    def __len__(self):
        return self.size
    def add_after(self, node, elem):
        prev = Node
        succ = node.next
        new_node = DoublyLinkedList.Node()
        new_node.data = elem
        new_node.next = succ
        new_node.prev = prev
        prev.next = node_node
        succ.prev = new_node
        self.size += 1
        return new_node
    def delete(self, node):
        prev = node.prev
        succ = node.next
        prev.next = succ
        succ.prev = prev
        self.size -= 1
        data = node.data
        node.disconnect()
        return data

class LeakyStack:
    class Node:
        def __init__(self, data= None, next = None, prev = None):
            self.data = data
            self.next = next
            self.prev = prev
    def __init__(self, msize):
        self.msize = msize
        self.header = LeakyStack.Node()
        self.trailer = LeakyStack.Node()
        self.header.next = self.trailer
        self.trailer.prev = self.header
        self.size = 0
    def is_empty(self):
        return (len(self) == 0)
    def push(self,e):
        if self.is_empty():
            raise EmptyException('LeakyStack is empty')
        if self.size == self.msize:
            n = self.header.next
            self.header.next = self.header.next.next
            self.header.next.next.prev = self.header
