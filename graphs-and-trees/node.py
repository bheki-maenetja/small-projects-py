class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None
    
    def add_left_child(self, node):
        if self.left == None:
            self.left = node
        else:
            self.left.add_left_child(node)

    def add_right_child(self, node):
        if self.right == None:
            self.right = node
        else:
            self.right.add_right_child(node)
    
    def get_children(self):
        return [
            child for child in (self.left, self.right) 
            if child is not None
        ]
    
    def get_value(self):
        return self.value

    def __repr__(self) -> str:
        return f"{self.value}"

class Tree:
    def __init__(self, root, relationships):
        tree_builder = {root: Node(root)}

        for value, children in relationships.items():
            if value not in tree_builder:
                tree_builder[value] = Node(value)
            
            parent_node = tree_builder[value]
            
            for index, child in enumerate(children):
                if child not in tree_builder:
                    tree_builder[child] = Node(child)
                
                if index == 0:
                    parent_node.add_left_child(tree_builder[child])
                elif index == 1:
                    parent_node.add_right_child(tree_builder[child])
        
        self.root = tree_builder[root]
    
    def get_root(self):
        return self.root

                    
