import sys
input = sys.stdin.readline
n = int(input())

xList = list(map(int, input().split()))
xList2 = sorted(list(set(xList))) #중복제거
xDic = {xList2[i] : i for i in range(len(xList2))}

for i in xList:
  print(xDic[i], end=' ')