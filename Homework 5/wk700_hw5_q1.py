
class Empty(Exception):
    pass


class ArrayQueue:
    INIT_CAPACITY = 10

    def __init__(self):
        self.data = [None] * ArrayQueue.INIT_CAPACITY
        self.front_ind = 0
        self.num_of_elems = 0

    def __len__(self):
        return self.num_of_elems

    def is_empty(self):
        return (len(self) == 0)

    def enqueue(self, elem):
        if (self.num_of_elems == len(self.data)):
            self.resize(2 * len(self.data))
        back_ind = (self.front_ind + self.num_of_elems) % len(self.data)
        self.data[back_ind] = elem
        self.num_of_elems += 1

    def dequeue(self):
        if (self.is_empty()):
            raise Empty("Queue is empty")
        elem = self.data[self.front_ind]
        self.data[self.front_ind] = None
        self.front_ind = (self.front_ind + 1) % len(self.data)
        self.num_of_elems -= 1
        if (self.num_of_elems < len(self.data) // 4):
            self.resize(len(self.data) // 2)
        return elem

    def front(self):
        if (self.is_empty()):
            raise Empty("Queue is empty")
        return self.data[self.front_ind]

    def resize(self, new_capacity):
        old_data = self.data
        self.data = [None] * new_capacity
        old_ind = self.front_ind
        for new_ind in range(self.num_of_elems):
            self.data[new_ind] = old_data[old_ind]
            old_ind = (old_ind + 1) % len(old_data)
        self.front_ind = 0


class Queue:
    def __init__(self):
        self.stack = ArrayStack()
        self.rstack = ArrayStack()
    def enqueue(self,elem):
        if self.stack.is_empty():
            for x in range (len(self.rstack)):
                self.stack.push(self.rstack.pop())
            return self.stack.push(elem)
        return self.stack.push(elem)

    def dequeue(self):
        if self.stack.is_empty() and self.rstack.is_empty():
            raise Empty('Queue is empty')
        elif self.rstack.is_empty():
            for x in range(len(self.stack)):
                self.rstack.push(self.stack.pop())
            return self.rstack.pop()
        return self.rstack.pop()

    def first(self):
        if self.stack.is_empty() and self.rstack.is_empty():
            raise Empty('Queue is empty')
        elif self.rstack.is_empty():
            for x in range(len(self.stack)):
                self.rstack.push(self.stack.pop())
            return self.rstack.top()
        return self.rstack.top()

    def len(self):
        if self.stack.is_empty():
            return len(self.rstack())
        return len(self.stack)

    def is_empty():
        if len(self.stack) == 0 and len(self.rstack) == 0:
            return True
