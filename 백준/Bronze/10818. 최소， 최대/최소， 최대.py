import sys

n = int(input())
arr = list(map(int, sys.stdin.readline().split()))

print(min(arr), max(arr))