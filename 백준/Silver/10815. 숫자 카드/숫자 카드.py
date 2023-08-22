import sys
input = sys.stdin.readline

N = int(input())
nList = set(map(int, input().split()))
M = int(input())
mList = list(map(int, input().split()))

res = []
for m in mList:
  if m in nList:
    res.append(1)
  else:
    res.append(0)

print(*res)