import sys
num = int(input())

for i in range(1, num+1):
  a, b = map(int, sys.stdin.readline().split())
  print('Case #{i}: {a} + {b} = {sum}' .format(i=i, a=a, b=b, sum=a+b))