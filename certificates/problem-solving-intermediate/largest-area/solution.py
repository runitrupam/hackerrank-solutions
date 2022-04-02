#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'getMaxArea' function below.
#
# The function is expected to return a LONG_INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER w
#  2. INTEGER h
#  3. BOOLEAN_ARRAY isVertical
#  4. INTEGER_ARRAY distance
#
import bisect 


def getMaxArea(w, h, isVertical, distance):
    
    A_w = [0,w]
    B_h = [0,h]
    n = len(isVertical)
    res = []
    for i in range(n):
        if isVertical[i] == 0:
            #B_h.append(distance[i])
            #B_h.sort()
            bisect.insort(B_h, distance[i])  # O(N)
        else:
            #A_w.append(distance[i])
            #A_w.sort()
            bisect.insort(A_w, distance[i])  # O(N)

        diff_h =  0
        st = B_h[0]
        for x in B_h:
            diff_h = max(diff_h, x - st )
            st = x
            
        diff_w =  0
        st = A_w[0]
        for x in A_w:
            diff_w = max(diff_w, x - st )
            st = x    
        res.append(diff_h * diff_w)    
    return res        
        
    
    
    
    # Write your code here
if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    w = int(input().strip())

    h = int(input().strip())

    isVertical_count = int(input().strip())

    isVertical = []

    for _ in range(isVertical_count):
        isVertical_item = int(input().strip()) != 0
        isVertical.append(isVertical_item)

    distance_count = int(input().strip())

    distance = []

    for _ in range(distance_count):
        distance_item = int(input().strip())
        distance.append(distance_item)

    result = getMaxArea(w, h, isVertical, distance)
    print( '\n'.join(map(str, result)  ))
    #fptr.write('\n'.join(map(str, result)))
    #fptr.write('\n')

    #fptr.close()
