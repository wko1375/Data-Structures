class BinarySearchTreeMap:
    class Item:
        def __init__(self, key, value=None):
            self.key = key
            self.value = value
    class Node:
        def __init__(self, item):
            self.item = item
            self.parent = None
            self.left = None
            self.right = None
            self.count = 1

        def num_children(self):
            count = 0
            if (self.left is not None):
                count += 1
            if (self.right is not None):
                count += 1
            return count

        def disconnect(self):
            self.item = None
            self.parent = None
            self.left = None
            self.right = None
    def __init__(self):
        self.root = None
        self.size = 0
    def __len__(self):
        return self.size
    def is_empty(self):
        return len(self) == 0
    # raises exception if not found
    def __getitem__(self, key):
        node = self.subtree_find(self.root, key)
        if (node is None):
            raise KeyError(str(key) + " not found")
        else:
            return node.item.value
    # returns None if not found
    def subtree_find(self, subtree_root, key):
        curr = subtree_root
        while (curr is not None):
            if (curr.item.key == key):
                return curr
            elif (curr.item.key > key):
                curr = curr.left
            else:  # (curr.item.key < key)
                curr = curr.right
        return None
    # updates value if key already exists
    def __setitem__(self, key, value):
        node = self.subtree_find(self.root, key)
        if (node is None):
            self.subtree_insert(key, value)
        else:
            node.item.value = value
    # assumes key not in tree
    def subtree_insert(self, key, value=None):
        item = BinarySearchTreeMap.Item(key, value)
        new_node = BinarySearchTreeMap.Node(item)
        if (self.is_empty()):
            self.root = new_node
            self.size = 1
        else:
            parent = self.root
            if(key < self.root.item.key):
                self.root.count += 1
                curr = self.root.left
            else:
                curr = self.root.right

            while (curr is not None):
                parent = curr
                if (key < curr.item.key):
                    curr = curr.left
                else:
                    curr = curr.right
            if (key < parent.item.key):
                parent.left = new_node
            else:
                parent.right = new_node
            new_node.parent = parent
            self.size += 1


    #raises exception if key not in tree
    def __delitem__(self, key):
        if (self.subtree_find(self.root, key) is None):
            raise KeyError(str(key) + " is not found")
        else:
            self.subtree_delete(self.root, key)

    #assumes key is in tree + returns value assosiated
    def subtree_delete(self, node, key):
        node_to_delete = self.subtree_find(node, key)
        value = node_to_delete.item.value
        num_children = node_to_delete.num_children()

        if (node_to_delete is self.root):
            if (num_children == 0):
                self.root = None
                node_to_delete.disconnect()
                self.size -= 1

            elif (num_children == 1):
                if (self.root.left is not None):
                    self.root = self.root.left
                else:
                    self.root = self.root.right
                self.root.parent = None
                node_to_delete.disconnect()
                self.size -= 1

            else: #num_children == 2
                max_of_left = self.subtree_max(node_to_delete.left)
                node_to_delete.item = max_of_left.item
                self.subtree_delete(node_to_delete.left, max_of_left.item.key)

        else:
            if (num_children == 0):
                parent = node_to_delete.parent
                if (node_to_delete is parent.left):
                    parent.left = None
                else:
                    parent.right = None

                node_to_delete.disconnect()
                self.size -= 1

            elif (num_children == 1):
                parent = node_to_delete.parent
                if(node_to_delete.left is not None):
                    child = node_to_delete.left
                else:
                    child = node_to_delete.right

                child.parent = parent
                if (node_to_delete is parent.left):
                    parent.left = child
                else:
                    parent.right = child

                node_to_delete.disconnect()
                self.size -= 1

            else: #num_children == 2
                max_of_left = self.subtree_max(node_to_delete.left)
                node_to_delete.item = max_of_left.item
                self.subtree_delete(node_to_delete.left, max_of_left.item.key)

        return value

    # assumes non empty subtree
    def subtree_max(self, curr_root):
        node = curr_root
        while (node.right is not None):
            node = node.right
        return node


    def inorder(self):
        for node in self.subtree_inorder(self.root):
            yield node

    def preorder(self):
        yield from self.subtree_preorder(self.root)

    def subtree_preorder(self, subtree_root):
        if subtree_root is not None:
            yield subtree_root
            yield from self.subtree_preorder(subtree_root.left)
            yield from self.subtree_preorder(subtree_root.right)

    def subtree_inorder(self, curr_root):
        if(curr_root is None):
            pass
        else:
            yield from self.subtree_inorder(curr_root.left)
            yield curr_root
            yield from self.subtree_inorder(curr_root.right)

    def __iter__(self):
        for node in self.inorder():
            yield (node.item.key, node.item.value)
    def get_ith_smallest(self, i):
        return self.get_ith_smallest_helper(self.root, i)
    def get_ith_smallest_helper(self, subtree_root,i):
        if i > self.size:
            raise IndexError
        bst_lst = []*i
        while True:
            while subtree_root is not None:
                bst_lst.append(subtree_root)
                subtree_root = subtree_root.left
            subtree_root = bst_lst.pop()
            if i == 1:
                return subtree_root.item.key
            else:
                i -= 1
                subtree_root = subtree_root.right

def create_chain_bst(n):
    if n == 0:
        new_tree = BinarySearchTreeMap()
        return new_tree
    else:
        new_tree = BinarySearchTreeMap()
        for i in range(1, n+1):
            new_tree.subtree_insert(i)
        return new_tree

def create_complete_bst(n):
    bst = BinarySearchTreeMap()
    add_items(bst, 1, n)
    return bst

def add_items(bst, low, high):
    if low == high:
        bst.subtree_insert(low)
    elif low - high == 1:
        bst.subtree_insert(high)
        bst.subtree_insert(low)
    elif low + high % 2 != 0:
        mid_num = (low+high //2) + 1
        bst.subtree_insert(mid_num)
        for i in range(low, mid_num):
            bst.subtree_insert(i)
        for i in range(mid_num + 1, high+1):
            bst.subtree_insert(i)
    else:
        mid_num = low + high // 2
        bst.root == tree_root
        for i in range(low, mid_num):
            bst.subtree_insert(i)
        for i in range(mid_num + 1, high+1):
            bst.subtree_insert(i)

def restore_bst(prefix_lst):
    if len(prefix_lst)==0:
        return BinarySearchTreeMap()
    new_tree = BinarySearchTreeMap()
    new_tree.root = restore_bst_helper(prefix_lst, 0)
    return new_tree

def restore_bst_helper(prefix_lst, index):
    if len(prefix_lst) == 1:
        return BinarySearchTreeMap.Node(BinarySearchTreeMap.Item(prefix_lst[0]))
    elif len(prefix_lst) == 0:
        return
    else:
        left_lst = []
        right_lst = []
        root = BinarySearchTreeMap.Node(BinarySearchTreeMap.Item(prefix_lst[0]))
        for i in range(1, len(prefix_lst)):
            if prefix_lst[i] < root.item.key:
                left_lst.append(prefix_lst[i])
            else:
                right_lst.append(prefix_lst[i])
        root.left = restore_bst_helper(left_lst, 0)
        root.right = restore_bst_helper(right_lst, 0)
        return root

def find_min_abs_difference(bst):
    lst = []
    for elem in bst.inorder():
        lst.append(elem.item.key)
    differences_lst = []
    for i in range(len(lst) - 1):
        next_item = lst[i + 1]
        curr_item = lst[i]
        differences_lst.append(next_item - curr_item)
    return min(differences_lst)
