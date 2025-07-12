import heapq
import sys

input = sys.stdin.read
data = input().splitlines()

n = int(data[0])
operations = data[1:]

heap = []
result = []

for op in operations:
    parts = op.split()
    
    if parts[0] == "insert":
        x = int(parts[1])
        heapq.heappush(heap, x)
        result.append(f"insert {x}")
    
    elif parts[0] == "getMin":
        x = int(parts[1])
        # Remove elements less than x
        while heap and heap[0] < x:
            heapq.heappop(heap)
            result.append("removeMin")
        # If top is not x or heap is empty
        if not heap or heap[0] > x:
            heapq.heappush(heap, x)
            result.append(f"insert {x}")
        result.append(f"getMin {x}")
    
    elif parts[0] == "removeMin":
        if not heap:
            heapq.heappush(heap, 0)
            result.append("insert 0")
        heapq.heappop(heap)
        result.append("removeMin")

print(len(result))
print("\n".join(result))
