#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'toolchanger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING_ARRAY tools
#  2. INTEGER startIndex
#  3. STRING target
#

def toolchanger(tools, startIndex, target):
    # Write your code here
    duplicates = False
    if tools.count(target) > 1:
        target_indices = [i for i, elem in enumerate(tools) if elem == target]
        target_indices = (min(target_indices), max(target_indices))
        duplicates = True
        
    target_index = tools.index(target)
    
    if target_index == startIndex:
        return 0
    elif target_index >= startIndex:
        forward_distance = target_indices[0] - startIndex if duplicates else target_index - startIndex
        backward_distance = len(tools) - (target_indices[1] - startIndex) if duplicates else len(tools) - forward_distance
    elif target_index < startIndex:
        backward_distance = startIndex - target_indices[1] if duplicates else startIndex - target_index
        forward_distance = len(tools) - (startIndex - target_indices[0]) if duplicates else len(tools) - backward_distance
    
    print(forward_distance, backward_distance)
    return min(forward_distance, backward_distance)
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    tools_count = int(input().strip())

    tools = []

    for _ in range(tools_count):
        tools_item = input()
        tools.append(tools_item)

    startIndex = int(input().strip())

    target = input()

    result = toolchanger(tools, startIndex, target)

    fptr.write(str(result) + '\n')

    fptr.close()
