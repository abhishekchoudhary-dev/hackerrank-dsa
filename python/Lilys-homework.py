# Problem:  Lily's homework
# Difficulty: Medium
# Link: https://www.hackerrank.com/challenges/lilys-homework  /
# Time Complexity: O(n log n) since we sort and then loop
# Space Complexity: O(n) for our visited array
# Approach: We have to use the traditional min swaps to sort the array appraoch where the permutation decomposes into disjoing cycles
# and each cycle swap to sort needs cycle-1 swaps. Only exception is that since for this specific question we have to look both ways
# meaning is sorting array will be faster than reverse sorting. both sorting speeds have to be compared and the least one \
# will be returned.

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'lilysHomework' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#
def min_swaps(arr)->int:
    swaps=0
    visited = [False]*len(arr)
    arr_pos = sorted(range(len(arr)),key = lambda i: arr[i])
    for i in range(len(arr)):
        if visited[i] or arr_pos[i] == i:
            continue
        #otherwise
        j=i
        cycle_size = 0
        while not visited[j]:
            visited[j] = True
            j = arr_pos[j]
            cycle_size+=1
        swaps+=cycle_size-1
    return swaps
    
def lilysHomework(arr):
    # Write your code here
    swaps = min_swaps(arr)
    r_swaps = min_swaps(arr[::-1])
    return min(swaps,r_swaps)
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = lilysHomework(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
