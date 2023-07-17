import sys

n, m = map(int, sys.stdin.readline().split())
arr = list(range(1, n+1))

for i in range(1, m+1):
  a, b = map(int, sys.stdin.readline().split())
  arr[a-1], arr[b-1] = arr[b-1], arr[a-1]

for i in range(n):
  print(arr[i], end=' ')