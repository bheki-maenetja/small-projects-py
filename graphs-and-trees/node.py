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
    
    def __repr__(self) -> str:
        return f"{self.value}"