# Problem:  The time in words
# Difficulty: Medium
# Link: https://www.hackerrank.com/challenges/the-time-in-words
# Time Complexity: O(k) as we process the time string of length k
# Space Complexity: O(1) as we use constant arrays of ones, tens and teens places
# Approach: We simply make arrays of ones placed , teens places and tens places and then based on what the minute hand is
# we accordingly calculate what we have to append to our answer. We handle the exception cases first for mins equal to 0,15,30,45 
# and then the minutes >30 or minutes<30 and we have predefined string ready to apppend (past,quarter, to) etc.
# Then based on minute value we append and return the joint string of the list at the end.
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeInWords' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER h
#  2. INTEGER m
#

def timeInWords(h, m):
    # Write your code here
    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine","ten","eleven","twelve"]
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
         "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    q = "quarter"
    to = "to"
    past = "past"
    half = "half"
    minutes = "minutes"
    minute = "minute"
    o = "o' clock"
    ans = []
    if m == 0:
        ans.append(ones[h])
        ans.append(o)
        return ' '.join(ans)
    if m == 30:
        ans.append(half)
        ans.append(past)
        ans.append(ones[h])
        return ' '.join(ans)
    if m == 15:
        ans.append(q)
        ans.append(past)
        ans.append(ones[h])
        return ' '.join(ans)
    if m == 45:
        ans.append(q)
        ans.append(to)
        ans.append(ones[h+1])
        return ' '.join(ans)
    #all special cases handles
    if m>30:
        mins = 60-m
        if mins<10:
            ans.append(ones[mins])
        elif mins<20:
            ans.append(teens[mins-10])
        else:
            ten = mins//10
            one = mins%10
            if one == 0:
                ans.append(tens[ten])
            else:
                ans.append(tens[ten])
                ans.append(ones[one])
        ans.append(minutes if mins>1 else minute)
        ans.append(to)
        ans.append(ones[h+1])
        return ' '.join(ans)
    if m<=30:
        mins = m
        if mins<10:
            ans.append(ones[mins])
        elif mins<20:
            ans.append(teens[mins-10])
        else:
            ten = mins//10
            one = mins%10
            if one == 0:
                ans.append(tens[ten])
            else:
                ans.append(tens[ten])
                ans.append(ones[one])
        ans.append(minutes if mins>1 else minute)
        ans.append(past)
        ans.append(ones[h])
        return ' '.join(ans)
        
        
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = int(input().strip())

    m = int(input().strip())

    result = timeInWords(h, m)

    fptr.write(result + '\n')

    fptr.close()
