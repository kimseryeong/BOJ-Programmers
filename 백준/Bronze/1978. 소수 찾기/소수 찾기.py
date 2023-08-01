N = int(input())
arr = list(map(int, input().split()))
sosu = 0
divisor = []

for i in arr:
  cnt = 0
  for num in range(1, i+1):
    if i % num == 0:
      cnt += 1
  divisor.append(cnt)

for x in divisor:
  if x == 2:
    sosu += 1
print(sosu)