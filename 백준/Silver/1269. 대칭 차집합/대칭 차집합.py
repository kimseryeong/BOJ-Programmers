import sys
input = sys.stdin.readline
n, m = map(int, input().split())
A = set(map(int, input().split()))

cnt = 0

for b in map(int, input().split()):
  if b in A:
    cnt += 1

print(n+m-cnt*2)