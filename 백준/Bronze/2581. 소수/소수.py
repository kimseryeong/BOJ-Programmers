import sys

m = int(sys.stdin.readline())
n = int(sys.stdin.readline())

sosu_sum = 0
sosu_list = []

for x in range(m, n+1):
  cnt = 0
  for i in range(1, x+1):
    if x % i == 0:
      cnt += 1
  if cnt == 2:
    sosu_sum += x
    sosu_list.append(x)

if sosu_sum == 0:
  print('-1')
else:
  print(sosu_sum, min(sosu_list), sep = '\n')