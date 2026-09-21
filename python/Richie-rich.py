#!/bin/python3
# Problem:  Richie rich - Highest value palindrome
# Difficulty: Medium
# Link: https://www.hackerrank.com/challenges/richie-rich/problem?isFullScreen=true
# Time Complexity: O(n) as we separately check first fix mismatch loop and then maximize loop
# Space Complexity: O(k) as we use a set but it only stores k indices
# Approach: We first mandatorily check if mismatches >k and return -1. If not which means it can be fixed
# and in that case we first make it palindrome and decrement k. then after that we go into maximization idea where we 
# go from outer to inner indices as per greedy approach and if either the left or right indices of a palindromic pairs is in changed set
# then it means that the cost of k to make both as 9 is 1 else the cost is 2. Before incurring the cost we check if we have that much k available
# because if not we would like to save the unspent k for future indices. For off length string we introduce a separate check for middle element
# which is not part of any pair and if k is left unspent we just make the middle element as '9

import math
import os
import random
import re
import sys

#
# Complete the 'highestValuePalindrome' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER n
#  3. INTEGER k
#

def highestValuePalindrome(s, n, k):
    def expandAndConstruct(arr,left,right,k)->list:
        changed = set()
        while left>=0 and right<len(s) and k>0:
            if arr[left]!=arr[right]:
                if arr[left]<arr[right]:
                    arr[left] = arr[right]
                    changed.add(left)
                elif arr[left] > arr[right]:
                    arr[right] = arr[left]
                    changed.add(right)
                k-=1
            left-=1
            right+=1
        return arr,k,changed
    # Write your code here
    mismatch = sum(1 for i in range(len(s)//2) if s[i]!=s[len(s)-i-1])
    if mismatch > k:
        return '-1'
    ans = [d for d in s]
    left,right = 0,0
    if len(ans)%2==0:
        left = len(s)//2-1
        right = len(s)//2
        res,k,indices = expandAndConstruct(ans,left,right,k)
        start,end = 0, len(res)-1
        while start<end and k>0:
            if res[start]!='9':
                if start in indices or end in indices:
                    res[start] = '9'
                    res[end] = '9'
                    k-=1
                else:
                    if k>=2:
                        res[start] = '9'
                        res[end]='9'
                        k-=2
            start+=1
            end-=1
        return ''.join(res)
                
    
    else:
        left = right = len(s)//2
        res,k,indices = expandAndConstruct(ans,left,right,k)
        start,end = 0, len(res)-1
        while start<end and k>0:
            if res[start]!='9':
                if start in indices or end in indices:
                    res[start] = '9'
                    res[end] = '9'
                    k-=1
                else:
                    if k>=2:
                        res[start] = '9'
                        res[end]='9'
                        k-=2
            start+=1
            end-=1
        if k>=1:
            res[len(res)//2] = '9'
        return ''.join(res)

        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = input()

    result = highestValuePalindrome(s, n, k)

    fptr.write(result + '\n')

    fptr.close()
