# Problem: Bear and steady gene
# Difficulty: Medium
# Link: https://www.hackerrank.com/challenges/bear-and-steady-gene/problem?isFullScreen=true
# Time Complexity: O(n^2) as we check substrings
# Space Complexity: O(n) as we use hashmaps
# we basically convert the given gene into a hashmap and check if any particular type is coming more than n//4 times
# as that means something else is less than n//4 and this has to be changed. based on this idea we build our substring 
# which we have to replace. Now if this substring occurs exactly in gene then ofcourse its the smallest that we can replace.
# otherwise we just go finding the smallest substring that includes all the character of the target string which we are trying to find in gene.
# for this we use the standard minimum window substring idea which find the minimum substring length
# which has all the required character of the target string and some more character stuck in between which we dont need.
# we return the best length that we find.

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

#
# Complete the 'steadyGene' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING gene as parameter.
#

def minWindow(gene,sub):
    if not sub:
        return 0
    need = Counter(sub)
    required = len(need)
    window = {}
    formed = 0
    left = 0
    best_len= float('inf')
    best_left= 0 
    for right, char in enumerate(gene):
        window[char] = window.get(char,0)+1
        if char in need and window[char] == need[char]:
            formed+=1
        while formed==required:
            if right-left+1 < best_len:
                best_len = right-left+1
                best_left = left
            left_char = gene[left]
            window[left_char]-=1
            if left_char in need and window[left_char] < need[left_char]:
                formed-=1
            left+=1
    return best_len if best_len!=float('inf') else 0
def steadyGene(gene):
    # Write your code here
    n = len(gene)
    d = Counter(gene)
    sub = ""
    for g,v in d.items():
        if v>n//4:
            sub+=g*(v-n//4)
    return minWindow(gene,sub)
    
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    gene = input()

    result = steadyGene(gene)

    fptr.write(str(result) + '\n')

    fptr.close()
