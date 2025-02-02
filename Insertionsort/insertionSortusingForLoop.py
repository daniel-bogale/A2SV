def insertionSort1(n, arr):
    val = arr[n-1]
    for i in range(n-2, -1, -1):
        if arr[i] > val:
            arr[i+1] = arr[i]
            print(*arr)
        else:
            arr[i+1] = val
            print(*arr)
            break
    else:
        arr[0] = val
        print(*arr)
