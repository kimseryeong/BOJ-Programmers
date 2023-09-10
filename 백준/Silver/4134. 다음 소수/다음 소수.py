import sys
import math

input = sys.stdin.readline
n = int(input())

#약수찾기는 대칭을 이루고 있으므로 제곱근 까지의 반복만 돌아도 됨
def IsPrime(x):
  if x == 0 or x == 1:
    return False
  for i in range(2, int(math.sqrt(x))+1):
    if x % i == 0:
        return False
  return True

for _ in range(n):
  y = int(input())
  while True:
    if IsPrime(y):
      print(y)
      break
    else:
      y+=1