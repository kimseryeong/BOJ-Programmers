import sys

n, m = map(int, sys.stdin.readline().split())
arr = [0 for i in range(n)]

for t in range(1, m + 1):
  i, j, k = map(int, sys.stdin.readline().split())
  for z in range(i, j + 1):
    arr[z - 1] = k

for t in range(n):
    print(arr[t], end=' ')