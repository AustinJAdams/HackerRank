### Alice and Bob each created one problem for HackerRank. A reviewer rates the two challenges, awarding points on a scale from  to  for three categories: problem clarity, originality, and difficulty.

We define the rating for Alice's challenge to be the triplet , and the rating for Bob's challenge to be the triplet .

Your task is to find their comparison points by comparing  with ,  with , and  with .

If A > B, then Alice is awarded  point.
If B > A, then Bob is awarded  point.
If B = A, then neither person receives a point.
###
#Completed by HackerRank
#!/bin/python3

import math
import os
import random
import re
import sys

# Completed by Me
def compareTriplets(a, b):
    count1 = 0
    count2 = 0
    for a, b in zip(a,b):
        if a > b:
            count1+=1
        elif b > a:
            count2+=1
    return count1, count2

#Completed by HackerRank
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
