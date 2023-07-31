n = int(input())
cnt = 2

for i in range(n):
  cnt += (2**i)
  
print(cnt**2)