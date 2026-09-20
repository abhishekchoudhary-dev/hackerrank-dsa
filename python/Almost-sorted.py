
import math
import os
import random
import re
import sys

#
# Complete the 'almostSorted' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#
def canSwapSort(arr)->(bool,int,int):
    s = sorted(arr)
    diff = [i for i in range(len(arr)) if arr[i]!=s[i]]
    if len(diff)!=2:
        return (False,-1,-1)
    left,right = diff[0],diff[1]
    arr[left],arr[right] = arr[right],arr[left]
    if arr==s:
        return (True,left+1,right+1)
    return (False,-1,-1)
    
    
def canReverseSegmentSort(arr)->(bool,int,int):
    i = 0
    s = sorted(arr)
    left,right = 0,0
    while i < len(arr)-1:
        if arr[i] > arr[i+1]:
            left = i
            while i+1< len(arr) and arr[i] > arr[i+1]:
                i+=1
            right=i
            arr[left:right+1] = arr[left:right+1][::-1]
            break
        else:
            i+=1
    if arr == s:
        return (True,left+1,right+1)
    return (False,-1,-1)
    
    
def almostSorted(arr):
    # Write your code here
    if all(arr[i]<=arr[i+1] for i in range(len(arr)-1)):
        print("yes")
        return
    possible,left,right = canSwapSort(arr[:])
    if possible:
        print("yes")
        print("swap",left,right)
        return
    possible, left,right = canReverseSegmentSort(arr[:])
    if possible:
        print("yes")
        print("reverse",left,right)
        return
    print("no")
        
    

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    almostSorted(arr)
