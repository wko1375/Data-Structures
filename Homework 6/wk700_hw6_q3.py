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
            raise EmptyCollection("List is empty")
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
class CompactString:
    def __init__(self, orig_str):
        self.orig_str = orig_str
        self.linkedlst = DoublyLinkedList()
        if len(self.orig_str) != 0:
            self.linkedlst.add_before(self.linkedlst.trailer, (self.orig_str[0],1) )
            for i in range(1, len(self.orig_str)):
                if self.linkedlst.trailer.prev.data[0] != self.orig_str[i]:
                    self.linkedlst.add_before(self.linkedlst.trailer, (self.orig_str[i], 1) )
                else:
                    x = self.linkedlst.trailer.prev.data[0]
                    y = self.linkedlst.trailer.prev.data[1] + 1
                    self.linkedlst.delete(self.linkedlst.trailer.prev)
                    self.linkedlst.add_before(self.linkedlst.trailer, (x,y))
    def __add__(self, other):
        if self.linkedlst.is_empty() and other.linkedlst.is_empty():
            raise Empty('Invalid Expression')
        if self.linkedlst.is_empty():
            return other
        if other.linkedlst.is_empty():
            return self
        new = CompactString('')
        otherlst = DoublyLinkedList()
        for elem in self.linkedlst:
            new.linkedlst.add_last(elem)
        for elem in other.linkedlst:
            otherlst.add_last(elem)
        if otherlst.header.next.data[0] == new.linkedlst.trailer.prev.data[0]:
            letter = new.linkedlst.trailer.prev.data[0]
            number = new.linkedlst.trailer.prev.data[1]
            othernumber = otherlst.header.next.data[1]
            new.linkedlst.trailer.prev.data = (letter, number + othernumber)
            otherlst.delete(otherlst.header.next)
        while otherlst.is_empty() == False:
            new.linkedlst.add_before(new.linkedlst.trailer, otherlst.header.next.data)
            otherlst.delete(otherlst.header.next)
        for elem in new.linkedlst:
            new.orig_str += elem[0] * elem[1]
        return new
    def __str__(self):
        return str(self.linkedlst)
    def __repr__(self):
        return str(self)
    def __lt__(self, other):
        slinkedlst = DoublyLinkedList()
        olinkedlst = DoublyLinkedList()
        for elem in self.linkedlst:
            slinkedlst.add_last(elem)
        for elem in other.linkedlst:
            olinkedlst.add_last(elem)
        while slinkedlst.is_empty() == False and olinkedlst.is_empty() == False:
            if slinkedlst.first_node().data[0] < olinkedlst.first_node().data[0]:
                return True
            elif slinkedlst.first_node().data[0] > olinkedlst.first_node().data[0]:
                return False
            else:
                if slinkedlst.first_node().data[1] > olinkedlst.first_node().data[1]:
                    onumber = olinkedlst.first_node().data[1]
                    olinkedlst.delete(olinkedlst.first_node())
                    letter = slinkedlst.first_node().data[0]
                    number = slinkedlst.first_node().data[1]
                    slinkedlst.first_node().data = (letter, number - onumber)
                elif slinkedlst.first_node().data[1] < olinkedlst.first_node().data[1]:
                    snumber = slinkedlst.first_node().data[1]
                    slinkedlst.delete(slinkedlst.first_node())
                    letter = olinkedlst.first_node().data[0]
                    number = olinkedlst.first_node().data[1]
                    olinkedlst.first_node().data = (letter, number - snumber)
                else:
                    slinkedlst.delete(slinkedlst.first_node())
                    olinkedlst.delete(olinkedlst.first_node())
        if slinkedlst.is_empty() and olinkedlst.is_empty():
            return False
        elif slinkedlst.is_empty():
            return True
        else:
            return False
    def __le__(self, other):
        slinkedlst = DoublyLinkedList()
        olinkedlst = DoublyLinkedList()
        for elem in self.linkedlst:
            slinkedlst.add_last(elem)
        for elem in other.linkedlst:
            olinkedlst.add_last(elem)
        while slinkedlst.is_empty() == False and olinkedlst.is_empty() == False:
            if slinkedlst.first_node().data[0] < olinkedlst.first_node().data[0]:
                return True
            elif slinkedlst.first_node().data[0] > olinkedlst.first_node().data[0]:
                return False
            else:
                if slinkedlst.first_node().data[1] > olinkedlst.first_node().data[1]:
                    onumber = olinkedlst.first_node().data[1]
                    olinkedlst.delete(olinkedlst.first_node())
                    letter = slinkedlst.first_node().data[0]
                    number = slinkedlst.first_node().data[1]
                    slinkedlst.first_node().data = (letter, number - onumber)
                elif slinkedlst.first_node().data[1] < olinkedlst.first_node().data[1]:
                    snumber = slinkedlst.first_node().data[1]
                    slinkedlst.delete(slinkedlst.first_node())
                    letter = olinkedlst.first_node().data[0]
                    number = olinkedlst.first_node().data[1]
                    olinkedlst.first_node().data = (letter, number - snumber)
                else:
                    slinkedlst.delete(slinkedlst.first_node())
                    olinkedlst.delete(olinkedlst.first_node())
        if slinkedlst.is_empty() and olinkedlst.is_empty():
            return True
        elif slinkedlst.is_empty():
            return True
        else:
            return False
    def __gt__(self, other):
        slinkedlst = DoublyLinkedList()
        olinkedlst = DoublyLinkedList()
        for elem in self.linkedlst:
            slinkedlst.add_last(elem)
        for elem in other.linkedlst:
            olinkedlst.add_last(elem)
        while slinkedlst.is_empty() == False and olinkedlst.is_empty() == False:
            if slinkedlst.first_node().data[0] < olinkedlst.first_node().data[0]:
                return False
            elif slinkedlst.first_node().data[0] > olinkedlst.first_node().data[0]:
                return True
            else:
                if slinkedlst.first_node().data[1] > olinkedlst.first_node().data[1]:
                    onumber = olinkedlst.first_node().data[1]
                    olinkedlst.delete(olinkedlst.first_node())
                    letter = slinkedlst.first_node().data[0]
                    number = slinkedlst.first_node().data[1]
                    slinkedlst.first_node().data = (letter, number - onumber)
                elif slinkedlst.first_node().data[1] < olinkedlst.first_node().data[1]:
                    snumber = slinkedlst.first_node().data[1]
                    slinkedlst.delete(slinkedlst.first_node())
                    letter = olinkedlst.first_node().data[0]
                    number = olinkedlst.first_node().data[1]
                    olinkedlst.first_node().data = (letter, number - snumber)
                else:
                    slinkedlst.delete(slinkedlst.first_node())
                    olinkedlst.delete(olinkedlst.first_node())
        if slinkedlst.is_empty() and olinkedlst.is_empty():
            return False
        elif slinkedlst.is_empty():
            return False
        else:
            return True
    def __ge__(self, other):
        slinkedlst = DoublyLinkedList()
        olinkedlst = DoublyLinkedList()
        for elem in self.linkedlst:
            slinkedlst.add_last(elem)
        for elem in other.linkedlst:
            olinkedlst.add_last(elem)
        while slinkedlst.is_empty() == False and olinkedlst.is_empty() == False:
            if slinkedlst.first_node().data[0] < olinkedlst.first_node().data[0]:
                return False
            elif slinkedlst.first_node().data[0] > olinkedlst.first_node().data[0]:
                return True
            else:
                if slinkedlst.first_node().data[1] > olinkedlst.first_node().data[1]:
                    onumber = olinkedlst.first_node().data[1]
                    olinkedlst.delete(olinkedlst.first_node())
                    letter = slinkedlst.first_node().data[0]
                    number = slinkedlst.first_node().data[1]
                    slinkedlst.first_node().data = (letter, number - onumber)
                elif slinkedlst.first_node().data[1] < olinkedlst.first_node().data[1]:
                    snumber = slinkedlst.first_node().data[1]
                    slinkedlst.delete(slinkedlst.first_node())
                    letter = olinkedlst.first_node().data[0]
                    number = olinkedlst.first_node().data[1]
                    olinkedlst.first_node().data = (letter, number - snumber)
                else:
                    slinkedlst.delete(slinkedlst.first_node())
                    olinkedlst.delete(olinkedlst.first_node())
        if slinkedlst.is_empty() and olinkedlst.is_empty():
            return True
        elif slinkedlst.is_empty():
            return False
        else:
            return True

def main():
    first = CompactString('abd')
    second = CompactString('ab')
    print(first > second)
main()
