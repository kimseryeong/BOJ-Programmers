#진법변환
import sys

N, b = map(str, sys.stdin.readline().split())
b = int(b)
N = ''.join(reversed(N))

sum = 0
jinbeob = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for i in range(len(N)-1, -1, -1):
  sum += jinbeob.index(N[i])*(b**i)
print(sum)