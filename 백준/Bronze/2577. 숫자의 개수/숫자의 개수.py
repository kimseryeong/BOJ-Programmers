a = int(input())
b = int(input())
c = int(input())

num = str(a*b*c)
numList = list(num)
#0~9
for x in range(10):
  print(numList.count(str(x)))