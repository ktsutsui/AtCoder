N, M = map(int, input().split())
rel = [set() for _ in range(N)]
for _ in range(M):
    x,y = map(int, input().split())
    rel[x-1].add(y-1)
    rel[y-1].add(x-1)

ans = 0
for bit in range(1<<N):
    arr = []
    for i in range(N):
        if (1<<i)&bit:
            arr.append(i)
    ok = True
    n = len(arr)
    for i in range(n):
        for j in range(i+1, n):
            if not (arr[j] in rel[arr[i]] and arr[i] in rel[arr[j]]):
                ok = False
                break
    if ok:
        ans = max(ans, n)
print(ans)