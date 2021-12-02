def bfs_traversal(start):
    array = [start]
    frontier = start.get_children()
    loop_count = 0
    node_expansions = 0

    while frontier != []:
        node = frontier[0]
        del frontier[0]
        if node not in array: 
            array.append(node)
        
        for child in node.get_children():
            if child not in frontier and child not in array:
                frontier.append(child)
                node_expansions += 1
        print(frontier)
        print(f"Size of frontier: {len(frontier)}")
        loop_count += 1
    
    print(f"Number of loops: {loop_count}")
    print(f"Expansions: {node_expansions}")
    return array