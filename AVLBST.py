from BinarySearchTree import BinarySearchTree

# class Node:
#     def __init__(self, item, key, skew):
#         self.item = item
#         self.skew = skew
#         self.item = item
#         self.key = key

class AVLBST(BinarySearchTree):
    
    def __init__(self, item, key, left_child = None, right_child = None, parent = None):
        super().__init__(item, key, left_child, right_child, parent)
        right_height = self._right_child._height if self._right_child is not None else -1
        left_height = self._left_child._height if self._left_child is not None else -1
        self._skew =  right_height - left_height
        self._height = 1 + max(right_height, left_height)
        
    def _swap_key_item(self, node):
        self._item, node._item = node._item, self._item
        self._key, node._key = node._key, self._key
    
    def _update_avl_property(self):
        """This functions is called whenever the node is newly added
        and there might be some ancestor which might have a skew with
        large absolute value."""
        current = self
        while current is not None:
            if current._skew < -1:
                current._rotate_right()
                return
            if current._skew > 1:
                current._rotate_left()
                return
            current = current._parent
    
    def _update_ancestors(self):
        """update the skew and heights for all ancestors of node.
        """
        current = self._parent
        while current is not None:
            current._update_height()
            current._update_skew()
            current = current._parent
    
    def add(self, item, key):
        if self._key == key:
            return None
        elif self._key < key:
            if self._right_child == None:
                self._right_child = AVLBST(item, key, parent = self)
                self._right_child._update_ancestors()
                self._right_child._update_avl_property()
                return self._right_child
            else:
                return self._right_child.add(item, key)
        else:
            if self._left_child == None:
                self._left_child = AVLBST(item, key, parent = self)
                self._left_child._update_ancestors()
                self._left_child._update_avl_property()
                return self._left_child
            else:
                return self._left_child.add(item, key)
    
    def _update_skew(self):
        right_height = self._right_child._height if self._right_child is not None else -1
        left_height = self._left_child._height if self._left_child is not None else -1
        self._skew = right_height - left_height
    
    def _update_height(self):
        right_height = self._right_child._height if self._right_child is not None else -1
        left_height = self._left_child._height if self._left_child is not None else -1
        self._height = 1 + max(right_height, left_height)
    
    def _rotate_right(self):
        """First the following transition will happen:
            ---S---              ---S---
         --SL--    SR    ->     SLL   --SL--
        SLL  SLR                     SLR    SR
        and then we will swap (key, item) between S and SL
        """
        if self._left_child is None:
            raise "A node must have left child in order to rotate it to right."

        parent = self._parent
        self_left = self._left_child
        self_left_left = self._left_child._left_child if self_left is not None else None
        self_left_right = self._left_child._right_child if self_left is not None else None
        self_right = self._right_child
        
        # Setting all pointers
        self._right_child = self_left
        self._left_child = self_left_left
        if self_left_left is not None:
            self_left_left._parent = self
        self_left._right_child = self_right
        self_left._left_child = self_left_right
        if self_right is not None:
            self_right._parent = self_left
        if self_left_right is not None:
            self_left_right._parent = self
        
        
        # Swap key and item between S and SL
        self._swap_key_item(self_left)
        
        # Update all skews and heights
        self_left._update_height()
        self_left._update_skew()
        self._update_height()
        self._update_skew()
    
        # Update all ancestors
        self._update_ancestors()
    
    def _rotate_left(self):
        
        if self._right_child is None:
            raise "A node must have left child in order to rotate it to right."

        parent = self._parent
        self_right = self._right_child
        self_right_right = self._right_child._right_child if self_right is not None else None
        self_right_left = self._right_child._left_child if self_right is not None else None
        self_left = self._left_child
        
        # Setting all pointers
        self._left_child = self_right
        self._right_child = self_right_right
        if self_right_right is not None:
            self_right_right._parent = self
        self_right._left_child = self_left
        self_right._right_child = self_right_left
        if self_left is not None:
            self_left._parent = self_right
        if self_right_left is not None:
            self_right_left._parent = self
        
        
        # Swap key and item between S and SL
        self._swap_key_item(self_right)
        
        # Update all skews and heights
        self_right._update_height()
        self_right._update_skew()
        self._update_height()
        self._update_skew()
        
        # Update all ancestors
        self._update_ancestors()
        