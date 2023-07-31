import sys

N, b = map(int, sys.stdin.readline().split())
jinbeob = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
result = ''

while True:
  if N == 0:
    break

  result += str(jinbeob[N%b])
  N = N//b
  
print(result[::-1])