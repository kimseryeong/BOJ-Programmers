chess = [1, 1, 2, 2, 2, 8]

found = list(map(int, input().split()))

arr = [ai - bi for ai, bi in zip(chess, found)]
for i in arr:
  print(i, end=' ')