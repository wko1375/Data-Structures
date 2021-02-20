import ctypes
import math
# Question 1
def split_by_sign(lst, low, high):
    if high-low == 1:
        if lst[low] > 0 and lst[high] < 0:
            lst[high], lst[low] = lst[low], lst[high]
        return lst
    elif low == high:
        return lst
    elif lst[low] > 0 and lst[high] < 0:
        lst[high], lst[low] = lst[low], lst[high]
        return split_by_sign(lst, low+1, high-1)
    elif lst[low] < 0 and lst[high] < 0:
        return split_by_sign(lst, low+1, high)
    elif lst[low] < 0 and lst[high] > 0:
        return split_by_sign(lst, low+1, high -1)
    elif lst[low] > 0 and lst[high] > 0:
        return split_by_sign(lst, low, high-1)
    else:
        return lst

# Question 2
def permutations(lst, low, high):
    t = lst[low:high]
    if len(t) == 0:
        return []
    if len(t)==1:
        return[t]
    l = []
    for i in range(low, len(t) - low):
        x = t[i]
        print(x)
        rest = t[:i] + t[i+1:]
        print(rest)
        for p in permutations(rest, low, high):
            l.append([x] + p)
    return l
print(permutations([1,2,3], 0, 3))


#Question 3
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
            raise IndexError
        return self.a[k]
    def append(self,obj):
        if self.n == self.capacity:
            self.resize(2*self.capacity)
        self.a[self.n] = obj
        self.n += 1
    def resize(self,c):
        b = self.make_array(c)
        for k in range(self.n):
            b[k] = self.a[k]
        self.a = b
        self.capacity = c
    def make_array(self,c):
        return (c*ctypes.py_object)()
    def __str__(self):
        s = '['
        for i in range (len(self)):
            s += str(self[i])
            if i != len(self)-1:
                s += ', '
        s += ']'
        return s
    def __repr__(self):
        print(str(self))
    def insert(self,index, val):
        x = self.a[len(self)-1]
        if self.n == self.capacity:
            self.resize(2*self.capacity)
            self.n+=1
        for i in range(self.n, index, -1):
            self.a[i] = self.a[i-1]
        self.a[index] = val
        self.append(x)
        return self
    def pop(self):
        if len(self) == 0:
            raise IndexError
        x = self.a[len(self)-1]
        self.a[len(self)-1] = None
        self.n -= 1
        if self.n < self.capacity / 4:
            self.capacity = int(self.capacity/2)
        return x
#Question 4
def find_duplicates(lst):
    l = []
    f = []
    e = []
    final = []
    for i in range (len(lst)):
        if lst[i] not in l:
            l.append(i)
    for i in range(len(lst)):
        if i not in l:
            f.append(i)
    for i in range (len(f)):
        f[i] = lst[f[i]]
    for i in range(len(f)):
        if f[i] not in final:
            final.append(f[i])
    return final

#Question 5
def remove_all(lst, value):
    l = []
    if value not in lst:
        raise ValueError
    for i in range(lst):
        if lst[i] != value:
            l.append(lst[i])
    return l
