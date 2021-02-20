import ctypes
class myList:
    def __init__(self):
        self.n = 0
        self.capacity = 1
        self.a = self.make_array(self.capacity)
    def __len__(self):
        return self.n
    def __getitem__(self, k):
        if not 0 <= k < self.n:
            raise IndexError('invalid index')
        return self.a[k]
    def append(self, obj):
        if self.n == self.capacity:
            self.resize(2*self.capacity)
        self.a[self.n] = obj
        self.n += 1
    def resize(self, c):
        b = self.make_array(c)
        for k in range (self.n):
            b[k] = self.a[k]
        self.a = b
        self.caapcity = c
    def make_array(self, c):
        return (c * ctypes.py_object)()
    def __str__(self):
        s = '['
        for elem in self:
            s += str(elem)
        s += ']'
        return s
    def __repr__(self):
        print(str(self))
    def __add__(self,other):
        self.extend
x = myList()
x.append(1)
print(x)
