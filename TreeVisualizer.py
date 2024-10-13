from DFS import DFS

# TODO: Choosing a library for graphical visualization

class TreeVisualizer():
    
    def __init__(self, tree):
        self._tree = tree
        
    def _find_tree_height(self, node):
        if node is None:
            return 0
        return 1 + max(self._find_tree_height(node.get_left_child()),
                       self._find_tree_height(node.get_right_child()))
        
    def print_tree(self):
        dfs = DFS()
        def representation_function(node):
            print(f'NODE: {node._item} ' +
                  f'LEFT_CHILD: {node._left_child._item if node._left_child is not None else None} ' +
                  f'RIGHT_CHILD: {node._right_child._item if node._right_child is not None else None}')
        dfs.search(self._tree, representation_function)