# Problem:  Sherlock and valid string
# Difficulty: Medium
# Link: https://www.hackerrank.com/challenges/sherlock-and-valid-string/
# Time Complexity: O(n)
# Space Complexity: O(n) as we use freq hashmaps
# Approach: We make a freq hashmaps and then make hashmap of the frequencies to basically find the most commmonly occuring frequency.
# Then We loop over the original first hashmap and check that if the freq of a character is not equal to the most common freq then two things are possible 
# if this difference freq character has a freq of 1 then we can just drop it or if it has a freq greater than the common freq then the difference can only be one. 
# So in both these cases we just return No. If no is not returned it means that we can resolve this mismatch and the nwe keep a count which 
# we increment to 1. If cnt goes beyond 1 we again return NO. If loop ends successfully we return "YES."

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isValid(s):
    # Write your code here
    d = Counter(s)
    f = [freq for freq in d.values()]
    if len(set(f))==1:
        return "YES"
    f1 = Counter(f)
    val = max(f1,key=f1.get)
    cnt = 0
    for v in d.values():
        if v != val:
            if v > val and v-val>1:
                return "NO"
            if v < val and v!=1:
                return "NO"
            cnt+=1
            if cnt>1:
                return "NO"
    return "YES"
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
