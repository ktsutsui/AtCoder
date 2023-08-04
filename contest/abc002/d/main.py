from itertools import combinations

N, M = map(int, input().split())
C = set()
for _ in range(M):
    x, y = map(int, input().split())
    C.add((x-1, y-1))

print(C)