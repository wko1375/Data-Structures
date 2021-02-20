import random
import string
class UnsortedArrayMap:
    class Item:
        def __init__(self, key, value=None):
            self.key = key
            self.value = value
    def __init__(self):
        self.table = []

    def __len__(self):
        return len(self.table)

    def is_empty(self):
        return (len(self) == 0)

    def __getitem__(self, key):
        for item in self.table:
            if key == item.key:
                return item.value
        raise KeyError("Key Error: " + str(key))

    def __setitem__(self, key, value):
        for item in self.table:
            if key == item.key:
                item.value = value
                return
        self.table.append(UnsortedArrayMap.Item(key, value))

    def __delitem__(self, key):
        for j in range(len(self.table)):
            if key == self.table[j].key:
                self.table.pop(j)
                return
        raise KeyError("Key Error: " + str(key))

    def __iter__(self):
        for item in self.table:
            yield item.key
class ChainingHashTableMap:
    def __init__(self, N=64, p=6460101079):
        self.N = N
        self.table = [None] * self.N
        self.n = 0
        self.p = p
        self.a = random.randrange(1, self.p - 1)
        self.b = random.randrange(0, self.p - 1)

    def hash_function(self, k):
        return ((self.a * hash(k) + self.b) % self.p) % self.N

    def __len__(self):
        return self.n

    def __getitem__(self, key):
        j = self.hash_function(key)
        curr_bucket = self.table[j]
        if curr_bucket is None:
            raise KeyError("Key Error: " + str(key))
        return curr_bucket[key]

    def __setitem__(self, key, value):
        j = self.hash_function(key)
        if self.table[j] is None:
            self.table[j] = UnsortedArrayMap()
        old_size = len(self.table[j])
        self.table[j][key] = value
        new_size = len(self.table[j])
        if (new_size > old_size):
            self.n += 1
        if (self.n > self.N):
            self.rehash(2 * self.N)

    def __delitem__(self, key):
        j = self.hash_function(key)
        curr_bucket = self.table[j]
        if curr_bucket is None:
            raise KeyError("Key Error: " + str(key))
        del curr_bucket[key]
        self.n -= 1
        if (curr_bucket.is_empty()):
            self.table[j] = None
        if (self.n < self.N // 4):
            self.rehash(self.N // 2)

    def __iter__(self):
        for curr_bucket in self.table:
            if (curr_bucket is not None):
                for key in curr_bucket:
                    yield key

    def rehash(self, new_size):
        old = []
        for key in self:
            value = self[key]
            old.append((key, value))
        self.table = [None] * new_size
        self.n = 0
        self.N = new_size
        for (key, value) in old:
            self[key] = value
def inverted_file_string_split(string, next_string):
    string[0].lower
    next_string[0].lower
    unsplit_string = string + next_string
    if string[len(string)-1] == ',':
        lst = unsplit_string.split(',')
    elif string[len(string)-1] == '.':
        lst = unsplit_string.split('.')
    elif string[len(string-1)] == '!':
        lst = unsplit_string.split('!')
    elif string[len(string-1)] == '?':
        lst = unsplit_string.split('?')
    front_string = lst[0]
    back_string = lst[1]
    return (front_string, back_string)


class InvertedFile:
    def __init__(self, file_name):
        self.table = ChainingHashTableMap()
        self.file_name = file_name
        txt_file = open(self.file_name, 'r')
        words_lnk_lst = DoublyLinkedList()
        for line in txt_file:
            line_words = line.split(' ')
        for elem in line_words:
            words_lnk_lst.add_last(DoublyLinkedList.Node(elem))
        pointer1 = words_lnk_lst.header.next
        pointer2 = words_lnk_lst.header.next.next
        while pointer2 != words_lnk_lst.trailer and pointer1 != words_lnk_lst.trailer:
            tup = inverted_file_string_split(pointer1.data, pointer2.data)
            pointer1.data = tup[0]
            pointer2.data = tup[0]
            pointer1 = pointer2
            pointer2 = pointer2.next
        count = 0
        for elem in words_lnk_lst:
            self.table[elem] = count
    def indices(self, word):
        return self.table[word]
