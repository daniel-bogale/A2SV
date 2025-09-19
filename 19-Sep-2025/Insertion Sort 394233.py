# Problem: Insertion Sort - https://www.hackerrank.com/challenges/insertionsort1/problem

def insertionSort1(n, arr):
    key = arr[-1]   
    i = n - 2       
    while i >= 0 and arr[i] > key:
        arr[i + 1] = arr[i]   
        print(" ".join(map(str, arr)))
        i -= 1

    arr[i + 1] = key   
    print(" ".join(map(str, arr)))