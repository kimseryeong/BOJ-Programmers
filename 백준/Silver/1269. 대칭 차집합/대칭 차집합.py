import sys
input = sys.stdin.readline

a, b = map(int, input().split())
A = {}
cnt = 0

for i in map(int,input().split()):
  A[i] = 1

for B in map(int,input().split()):
  if B in A:
    cnt += 1

print(a+b-cnt*2)