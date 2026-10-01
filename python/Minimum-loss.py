# Problem:  Minimum loss
# Difficulty: Medium
# Link: https://www.hackerrank.com/challenges/minimum-loss/problem?isFullScreen=true
# Time Complexity: O(n)
# Space Complexity: O(n) as we use a hashmap
# Approach: We know that difference between values should be minimum to find the minimum loss to have values as closely spaced as possible the 
# standard idea is to sort the array. but in sorting the indexation will be destroyed. So what we do is
# that we first map the indices in a hashmap and then we sort and go in reverse and differences are guaranteed to be the lowest.
# before taking difference we just check if the first element occurs before the second one and if yes we update our mn variable
# we return mn at the end.

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumLoss' function below.
#
# The function is expected to return an INTEGER.
# The function accepts LONG_INTEGER_ARRAY price as parameter.
#

def minimumLoss(price):
    # Write your code here
    mn = float('inf')
    d = {p:idx for idx,p in enumerate(price)}
    price.sort(reverse=True)
    for i in range(1,len(price)):
        if d[price[i-1]] < d[price[i]]:
            mn = min(mn,price[i-1]-price[i])
    return mn
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    price = list(map(int, input().rstrip().split()))

    result = minimumLoss(price)

    fptr.write(str(result) + '\n')

    fptr.close()
