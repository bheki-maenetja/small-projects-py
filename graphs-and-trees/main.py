from node import Node, Tree
from bfs import bfs_traversal
from dfs import dfs_traversal
from tree_traversals import in_order_traversal, pre_order_traversal, post_order_traversal

first_tree_dict = {
    "a": ("b", "c"),
    "b": ("d", "e"),
    "c": ("h", "i"),
    "d": ("f", "g")
}

other_tree_dict = {
    "a": ("b", "b"),
    "b": ("c", "c"),
    "c": ("d", "d"),
    "d": ("e", "e"),
    "e": ("f", "f")
}



if __name__ == "__main__":
    first_tree = Tree("a", first_tree_dict)
    other_tree = Tree("a", other_tree_dict)
    print(other_tree.get_root().get_children())
    print(dfs_traversal(first_tree.get_root()))
    print(dfs_traversal(other_tree.get_root()))