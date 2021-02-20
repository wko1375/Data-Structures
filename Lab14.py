class PriorityQueue:
    class Node:
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.next = None
    def __init__(self, head = None):
        self.head = head

    def peek_min(self):

    def peek_max(self):

    def pop_min(self):

    def insert_node(self, node):
        curr = self.head
        if curr.next == None:
            curr.next = node
        else:
            while node.key > curr.key:
                if curr.next == None:
                    curr.next = node
                elif curr.next.key > node.key:
                    node.next = curr.next
                    curr.next = node
                curr = curr.next 


    def search_node(self, node):
