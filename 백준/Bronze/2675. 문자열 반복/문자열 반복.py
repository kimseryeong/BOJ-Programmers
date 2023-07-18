case = int(input())

for i in range(case):
  a, b = input().split()
  for j in b:
    print(int(a)*j, end='')
  print()