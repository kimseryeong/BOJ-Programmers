import sys
input = sys.stdin.readline

n = int(input())
logDic = {}
nameSet = set()

for _ in range(n):
  name, log = map(str, input().split())
  if log == 'enter':
    logDic[name] = log
  else:
    del logDic[name]

logDic = sorted(logDic.keys(), reverse = True)
for p in logDic:
  print(p)
