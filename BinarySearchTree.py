from BinaryTree import BinaryTree

class BinarySearchTree(BinaryTree):
    
    def __init__(self, item, key, left_child = None, right_child = None, parent = None):
        super().__init__(item, left_child, right_child, parent)
        self._key = key

    def find(self, key):
        if self.key == key:
            return self
        if key > self.key:
            if self._right_child == None:
                return None
            else:
                return self._right_child.find(key)
        if key < self.key:
            if self._left_child == None:
                return None
            else:
                return self._left_child.find(key)

    def add(self, item, key):
        if self._key == key:
            return None
        elif self._key < key:
            if self._right_child == None:
                self._right_child = BinarySearchTree(item, key)
                return self._right_child
            else:
                return self._right_child.add(item, key)
        else:
            if self._left_child == None:
                self._left_child = BinarySearchTree(item, key)
                return self._left_child
            else:
                return self._left_child.add(item, key)

    def remove(self, key):
        if self.key == key:
            if self._parent.get_right_child() == self:
                self._parent.set_right_child(None)
            else:
                self._parent.set_right_child(None)
        elif self.key < key:
            self._right_child.remove(key)
        else:
            self._left_child.remove(key)