from node import Node
from bfs import bfs_traversal
from dfs import dfs_traversal

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')

a.add_left_child(b)
a.add_right_child(b)

b.add_left_child(c)
b.add_right_child(c)

c.add_left_child(d)
c.add_right_child(d)

d.add_left_child(e)
d.add_right_child(e)

e.add_left_child(f)
e.add_right_child(f)