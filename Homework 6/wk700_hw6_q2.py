class Empty(Exception):
    pass
class DoublyLinkedList:
    class Node:
        def __init__(self, data=None, next=None, prev=None):
            self.data = data
            self.next = next
            self.prev = prev

        def disconnect(self):
            self.data = None
            self.next = None
            self.prev = None


    def __init__(self):
        self.header = DoublyLinkedList.Node()
        self.trailer = DoublyLinkedList.Node()
        self.header.next = self.trailer
        self.trailer.prev = self.header
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return (len(self) == 0)

    def first_node(self):
        if (self.is_empty()):
            raise Empty("List is empty")
        return self.header.next

    def last_node(self):
        if (self.is_empty()):
            raise Empty("List is empty")
        return self.trailer.prev

    def add_first(self, elem):
        return self.add_after(self.header, elem)

    def add_last(self, elem):
        return self.add_after(self.trailer.prev, elem)

    def add_after(self, node, elem):
        prev = node
        succ = node.next
        new_node = DoublyLinkedList.Node()
        new_node.data = elem
        new_node.prev = prev
        new_node.next = succ
        prev.next = new_node
        succ.prev = new_node
        self.size += 1
        return new_node

    def add_before(self, node, elem):
        return self.add_after(node.prev, elem)

    def delete(self, node):
        prev = node.prev
        succ = node.next
        prev.next = succ
        succ.prev = prev
        self.size -= 1
        data = node.data
        node.disconnect()
        return data

    def __iter__(self):
        if(self.is_empty()):
            return
        cursor = self.first_node()
        while(cursor is not self.trailer):
            yield cursor.data
            cursor = cursor.next

    def __str__(self):
        return '[' + '<-->'.join([str(elem) for elem in self]) + ']'

    def __repr__(self):
        return str(self)
class Integer:
    def __init__(self, num_str):
        self.num_str = num_str
        self.linkedlst = DoublyLinkedList()
        for elem in num_str:
            self.linkedlst.add_before(self.linkedlst.trailer, elem)
    def __str__(self):
        return self.num_str
    def __add__(self, other):
        slist = self.linkedlst
        olist = other.linkedlst
        sstr = self.num_str
        ostr = other.num_str
        fin = ''
        if slist.is_empty() or olist.is_empty():
            raise Empty('Invalid Expression')
        node1 = slist.trailer.prev
        node2 = olist.trailer.prev
        carry = 0
        while node1 != slist.header and node2 != olist.header:
            num1 = node1.data
            num2 = node2.data
            newnum = int(num1) + int(num2) + int(carry)
            if newnum > 9:
                carry = str(newnum)[0]
                newnum = str(newnum)[1]
            fin = str(newnum) + fin
            slist.delete(slist.trailer.prev)
            olist.delete(olist.trailer.prev)
            node1 = slist.trailer.prev
            node2 = olist.trailer.prev
        if node1 != slist.header:
            while node1 != slist.header:
                number = int(carry) + int(slist.trailer.prev.data)
                if number > 9:
                    carry = str(number)[0]
                    number = str(number)[1]
                else:
                    carry = 0
                fin = str(number) + fin
                slist.delete(slist.trailer.prev)
                node1 = slist.trailer.prev
        if node2 != olist.header:
            while node2 != olist.header:
                number = int(carry) + int(olist.trailer.prev.data)
                if number > 9:
                    carry = str(number)[0]
                    number = str(number)[1]
                else:
                    carry = 0
                fin = str(number) + fin
                olist.delete(olist.trailer.prev)
                node2 = olist.trailer.prev
        if carry!=0:
            fin = str(carry) + fin
        return fin
    def __repr__(self):
        return str(self)
