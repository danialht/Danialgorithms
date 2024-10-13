class DFS:
    def search(self, start_node, representation_function = lambda x : x):
        traversal = []
        
        def recursive_search(node):
            if node is not None:
                traversal.append(representation_function(node))
            else:
                return
            if node.get_left_child() is not None:
                recursive_search(node.get_left_child())
            if node.get_right_child is not None:
                recursive_search(node.get_right_child())
        
        recursive_search(start_node)
        
        return traversal