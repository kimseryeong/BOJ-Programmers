T = int(input())
xList = []
yList = []

for _ in range(T):
  x, y = map(int, input().split())
  xList.append(x)
  yList.append(y)

print((max(xList)-min(xList)) * (max(yList)-min(yList)))
  