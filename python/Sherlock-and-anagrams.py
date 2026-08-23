# Problem:  Sherlock and anagrams
# Difficulty: Medium
# Link: https://www.hackerrank.com/challenges/sherlock-and-anagrams/
# Time Complexity: O(n) as we do a single pass through the numbers from 1 to n.
# Space Complexity: O(n) as we only use a dictionary to hold remainders
# Approach: We take all substring and enter them in a hashmap after sorting to see if they are annogrammatic pairs of each other
# after each key has been counted in hashmap we iterate over key values and calculate how many pairs it will make by the formula n*(n-1)/2.
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sherlockAndAnagrams' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#
from collections import defaultdict
def sherlockAndAnagrams(s):
    # Write your code here
    d = defaultdict(int)
    for i in range(len(s)):
        for j in range(i,len(s)):
            key = ''.join(sorted(s[i:j+1]))
            d[key]+=1
    pairs=0
    for key,val in d.items():
        pairs += (val*(val-1))//2
    return pairs
            
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()