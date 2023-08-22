import sys
input = sys.stdin.readline

N = int(input())
xyList = []

for _ in range(N):
  [x, y] = map(int, input().split())
  xyList.append([x, y])

xyList.sort()

for i in range(N):
  print(xyList[i][0], xyList[i][1])