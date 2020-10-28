def is_list_permutation(L1, L2):
    '''
    L1 and L2: lists containing integers and strings
    Returns False if L1 and L2 are not permutations of each other. 
            If they are permutations of each other, returns a 
            tuple of 3 items in this order: 
            the element occurring most, how many times it occurs, and its type
    '''
    # Your code here
    if set(L1) != set(L2) or len(L1) != len(L2):
        return False
    elif L1 == [] and L2 == []:
        return (None, None, None)
    else:
        l1_set = { (y, L1.count(y)) for y in L1 }
        l2_set = { (y, L2.count(y)) for y in L2 }
        if l1_set != l2_set:
            return False
        else:
            common_element = max(l1_set, key=lambda x: x[1])
            return (common_element[0], common_element[1], type(common_element[0]))