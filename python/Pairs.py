# Problem:  Pairs
# Difficulty: Medium
# Link: https://www.hackerrank.com/challenges/pairs/
# Time Complexity: O(n) as we do a single pass through the numbers from 1 to n.
# Space Complexity: O(n) as we use a hashmap
# Approach: We simply make a hashmap and for every element we check if element - target is in hashmap which is O(1) 
# and works for 10^5 input size. Since all elemenets are unique we dont need to keep a freq count of each element 
# as that count will be 1. Then we return cnt at the end.

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
#
# Complete the 'pairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

def pairs(k, arr):
    # Write your code here
    cnt = 0
    d = Counter(arr)
    for num in arr:
        if num - k in d:
            cnt+=1
    return cnt
    #if repetition then we need a defaultdict(int)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = pairs(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
