import math
import os
import random
import re
import sys

def countSwaps(a):
    swap = 0

    for i in range(0,len(a)):
        for j in range(0,len(a)-1):
            if a[j+1]<a[j]:
                temp = a[j]
                a[j] = a[j+1]
                a[j+1] = temp
                swap+=1

        
    print("Array is sorted in "+ str(swap) + " swaps.")
    print("First Element: " + str(a[0]))

    print("Last Element: " + str(a[len(a)-1]))
    return

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
