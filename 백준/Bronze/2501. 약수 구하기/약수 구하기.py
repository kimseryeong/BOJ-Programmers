N, k = map(int, input().split())
divisor = []

for n in range(1, N+1):
  if  N % n == 0:
    divisor.append(n)

if len(divisor) < k:
  print('0')
else:
  print(divisor[k-1])