# Problem: Greedy florist
# Difficulty: Easy
# Link: https://www.hackerrank.com/challenges/greedy-florist/problem
# Time Complexity: O(n log n) as we sort and then reverse separately and then loop over O(n)
# Space Complexity: O(1) as we dont store result
# Approach: We need to realize since all flowers have to be bought then we would like to have the repetition over the flowers of the buyer which have the lowest costs.
# so we sort the flowers and first do the first buying for all customers with the most expensive flowers.
# then we find the remaining flowers and start looping the number of buyers over them and everytime each buyer buys their 2nd flower we increment count
# of how many they have bought already. This buyer loop increment their prev_bought count has to run in reverse on the remaining flowers after sorting or we can run it from the front 
# by reversing the remaining flowers. This is because the greedy factor of (prev_bought+1) will multiply the flower cost and make it much higher
# so we want the multiplier to be applied to smaller values to keep total cost minimum as required in the problem.

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the getMinimumCost function below.
def getMinimumCost(k, c):
    if k >= len(c):
        return sum(c)
    c.sort()
    base_cp = sum(c[-k:])
    prev_purchase_count=1
    remaining = len(c) - k
    c = c[0:remaining][::-1]
    cnt=0
    for i in range(remaining):
        if cnt==k:
            prev_purchase_count+=1
            cnt=0
        base_cp+=c[i]*(prev_purchase_count+1)
        cnt+=1
    return base_cp

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    minimumCost = getMinimumCost(k, c)

    fptr.write(str(minimumCost) + '\n')

    fptr.close()
