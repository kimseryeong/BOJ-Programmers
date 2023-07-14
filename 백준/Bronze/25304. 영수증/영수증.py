import sys

x = int(input())
n = int(input())
count = 0

for i in range(n):
  a, b = map(int, sys.stdin.readline().split())
  count += a*b
if x == count:
  print('Yes')
else:
  print('No')