import sys

n, m = map(int, sys.stdin.readline().split())
arr = list(range(1, n+1))

for i in range(m):
  a, b = map(int, sys.stdin.readline().split())
  
  temp = arr[a-1:b]
  temp.reverse()
  arr[a-1:b] = temp

for i in range(n):
  print(arr[i], end=' ')
  
