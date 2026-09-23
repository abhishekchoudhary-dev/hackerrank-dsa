# Problem:  Max min
# Difficulty: Medium
# Link: https://www.hackerrank.com/challenges/angry-children/problem?isFullScreen=true
# Time Complexity: O(n)
# Space Complexity: O(1)
# Approach: We need to have the observation that the difference will be minimized between the max and min of any subarray
# if the array is sorted. 10^5 allows us to sort the array and then for each subarray either we can slice it and check max and min diff and take minimum 
# otherwise directly compare max and min with indices on the array itself and max and min are guaranteed to be the first and last element
# of the subarray.

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maxMin' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

def maxMin(k, arr):
    # Write your code here
    arr.sort()
    
    unfair = float('inf')
    for i in range(len(arr)-k+1):
        #sub = arr[i:i+k]
        #unfair = min(unfair,sub[-1]-sub[0])
        unfair = min(unfair,arr[i+k-1]-arr[i])
    return unfair
    
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    k = int(input().strip())

    arr = []

    for _ in range(n):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = maxMin(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
