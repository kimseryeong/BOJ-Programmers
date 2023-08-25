import sys
input = sys.stdin.readline

nDict = {}
res = []
cnt = 0

n, m = map(int, input().split())
for _ in range(n):
  nDict[input().strip()] = 1

for _ in range(m):
  name = input().strip()
  if name in nDict:
    cnt += 1
    res.append(name)

print(cnt)
print(*sorted(res))