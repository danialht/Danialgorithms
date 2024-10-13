class BinaryTree:
    def __init__(self, item, left_child = None, right_child = None, parent = None):
        self._item = item
        self._left_child = left_child
        self._right_child = right_child
        self._parent = parent
        return self
    
    def set_left_child(self, left_child):
        self._left_child = left_child
    
    def set_right_child(self, right_child):
        self._right_child = right_child
    
    def set_parent(self, parent):
        self._parent = parent
        
    def get_parent(self):
        return self._parent
    
    def get_right_child(self):
        return self._right_child
    
    def get_left_child(self):
        return self._left_child
    
    def get_item(self):
        return self._item
    
    def set_item(self, item):
        self.item = item