xList = []
yList = []
for _ in range(3):
  x, y = map(int, input().split())
  xList.append(x)
  yList.append(y)
X, Y = 0, 0
for x in xList:
  if xList.count(x) == 1:
    X = x
for y in yList:
  if yList.count(y) == 1:
    Y = y

print(X, Y, sep = ' ')
