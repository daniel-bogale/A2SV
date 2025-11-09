q = int(input())
for _ in range(q):
    n = int(input())
    p = list(map(int, input().split()))

    perm = [x - 1 for x in p]
    ans = []
    visited = [False] * n
    for i in range(n):
        if not visited[i]:
            cycle = []
            cur = i
            while not visited[cur]:
                visited[cur] = True
                cycle.append(cur)
                cur = perm[cur]
            cycle_length = len(cycle)
            for node in cycle:
                ans.append((node, cycle_length))

    ans.sort()

    result = [str(cycle_len) for (node, cycle_len) in ans]
    print(" ".join(result))