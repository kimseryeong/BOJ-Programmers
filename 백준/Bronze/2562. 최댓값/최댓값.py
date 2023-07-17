arr = []
for i in range(1, 10):
  a = int(input())
  arr.append(a)
print(max(arr), arr.index(max(arr))+1)