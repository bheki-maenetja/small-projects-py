def pre_order_traversal(tree, array):
    if tree is None:
        return array
    else:
        return [tree.value] + pre_order_traversal(tree.left, array) + pre_order_traversal(tree.right, array)

def post_order_traversal(tree, array):
    if tree is None:
        return array
    else:
        return post_order_traversal(tree.left, array) + post_order_traversal(tree.right, array) + [tree.value]

def in_order_traversal(tree, array):
    if tree is None:
        return array
    else:
        return  in_order_traversal(tree.left, array) + [tree.value] + in_order_traversal(tree.right, array)