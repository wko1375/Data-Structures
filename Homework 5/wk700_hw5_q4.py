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
    def __iter__(self):
        for i in range(len(self.data)):
            yield self.data[i]
class MaxStack:
    def __init__(self):
        self.s = ArrayStack()
        self.m = None
    def is_empty(self):
        return (len(s) == 0)
    def len(self):
        return len(s)
    def push(self, e):
        t = (self.m, e)
        self.s.push(t)
        if self.m == None or e > self.m:
            self.m = e
    def top(self):
        if self.s.is_empty():
            raise EmptyCollection('MaxStack is empty')
        return self.s.top()[1]
    def pop(self):
        if self.s.is_empty():
            raise EmptyCollection('MaxStack is empty')
        self.m = self.s.top()[0]
        return self.s.pop()[1]

    def max(self):
        if self.s.is_empty():
            raise EmptyCollection('MaxStack is empty')
        return self.m
