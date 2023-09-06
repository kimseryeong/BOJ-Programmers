import sys
import math

input = sys.stdin.readline
n = int(input())
garo = [int(input()) for i in range(n)]
distance = [(garo[i+1] - garo[i]) for i in range(n-1)]

g = distance[0]
for j in range(1, len(distance)):
    g = math.gcd(g, distance[j])
res = 0

for d in distance:
  res += d // g - 1

print(res)