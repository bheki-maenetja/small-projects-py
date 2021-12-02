def bfs_traversal(start):
    array = [start]
    frontier = start.get_children()

    while frontier != []:
        node = frontier[0]
        del frontier[0]
        if node not in array: 
            array.append(node)
        
        for child in node.get_children():
            if child not in frontier and child not in array:
                frontier.append(child)
    
    return array