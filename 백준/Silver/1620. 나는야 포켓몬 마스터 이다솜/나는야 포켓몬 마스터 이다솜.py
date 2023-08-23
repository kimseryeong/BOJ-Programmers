import sys
input = sys.stdin.readline

n, m = map(int, input().split())

pocket = {}

for i in range(1, n+1):
  p = input().rstrip()
  pocket[p] = i
  pocket[i] = p
  
for i in range(m):
    quest = input().rstrip()
    if quest.isdigit():
        print(pocket[int(quest)])
    else:
        print(pocket[quest])