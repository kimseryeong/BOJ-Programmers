n = int(input())
mem = []

for _ in range(n):
  [age, name] = map(str, input().split())
  mem.append([int(age), name])

mem.sort(key=lambda x:x[0])


for i in range(n):
  print(mem[i][0], mem[i][1])