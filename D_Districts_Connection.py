# from collections import Counter
# t = int(input())
# for _ in range(t):
#     n = int(input())
#     arr = list(map(int,input().split()))
#     most_frequent = max(arr, key=arr.count)
#     frequency = arr.count(most_frequent)
#     possible =  n-frequency>= frequency
#     print("YES" if possible else "NO")
#     if possible:


# t = int(input())

# for _ in range(t):
#     n = int(input())
#     a = list(map(int, input().split()))

#     # Find the first node that is different from the first one
#     root = -1
#     for i in range(1, n):
#         if a[i] != a[0]:
#             root = i
#             break

#     if root == -1:
#         print("NO")
#         continue

#     print("YES")
#     edges = []
    
#     # Step 1: Connect all nodes with a[i] != a[0] to node 1
#     for i in range(1, n):
#         if a[i] != a[0]:
#             edges.append((1, i + 1))
    
#     # Step 2: Connect all nodes with a[i] == a[0] to the 'root' node we found earlier
#     for i in range(1, n):
#         if a[i] == a[0]:
#             edges.append((root + 1, i + 1))

#     # Print only n-1 edges
#     for u, v in edges[:n-1]:
#         print(u, v)
