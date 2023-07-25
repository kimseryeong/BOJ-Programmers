n, m = map(int, input().split())
A, B = [], []

for _ in range(n):
  row = list(map(int, input().split()))
  A.append(row)
for _ in range(n):
  row = list(map(int, input().split()))
  B.append(row)

for row in range(n):
  for col in range(m):
    print(A[row][col] + B[row][col], end = ' ')
  print()