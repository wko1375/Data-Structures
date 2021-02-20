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
def merge_sublists(lst1, lst2, index1, index2):
    lst = DoublyLinkedList()
    if index1 == len(lst1) and index2 == len(lst2):
        return lst
    if index1 == len(lst1):
        for i in range(index2, len(lst2)):
            lst.add_last(lst2[i])
        return lst
    if index2 == len(lst2):
        for i in range(index1, len(lst1)):
            lst.add_last(lst1[i])
        return lst
    if lst1[index1] > lst2[index2]:
        lst.add_last(lst2[index2])
        index2 += 1
        for elem in merge_sublists(lst1, lst2, index1, index2):
            lst.add_last(elem)
        return lst
    elif lst1[index1] < lst2[index2]:
        lst.add_last(lst1[index1])
        index1 += 1
        for elem in merge_sublists(lst1, lst2, index1, index2):
            lst.add_last(elem)
        return lst
    else:
        lst.add_last(lst1[index1])
        lst.add_last(lst2[index2])
        index1 += 1
        index2 += 1
        for elem in merge_sublists(lst1, lst2, index1, index2):
            lst.add_last(elem)
        return lst
def merge_linked_lists(srt_lnk_lst1, srt_lnk_lst2):
    return merge_sublists([elem for elem in srt_lnk_lst1], [elem for elem in srt_lnk_lst2], 0, 0)
