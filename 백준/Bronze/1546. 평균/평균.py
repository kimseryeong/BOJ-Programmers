import sys

n = int(input())
arr = list(map(int, sys.stdin.readline().split()))
arr2 = []

for i in range(n):
  arr2.append(arr[i]/max(arr)*100)

print(sum(arr2)/n)