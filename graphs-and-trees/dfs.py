def dfs_traversal(start):
    array = [start]
    frontier = start.get_children()

    while frontier != []:
        node = frontier[0]
        del frontier[0]
        if node not in array: 
            array.append(node)
        
        children = node.get_children().copy()
        while children != []:
            child = children.pop()
            if child not in frontier and child not in array:
                frontier.insert(0, child)

    return array