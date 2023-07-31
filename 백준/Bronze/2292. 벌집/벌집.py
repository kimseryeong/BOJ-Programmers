n = int(input())

bee = 1

for i in range(n):
  bee += i*6
  if n <= bee:
    print(i+1)
    break