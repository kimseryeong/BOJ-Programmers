import sys
import math


#약수찾기는 대칭을 이루고 있으므로 제곱근 까지의 반복만 돌아도 됨
def IsPrime(x):
  if x == 1:
    return False
  for i in range(2, int(math.sqrt(x)) + 1):
    if x % i == 0:
      return False
  return True


allList = list(range(2, 246912))  #2부터 2*123,456 범위
memo = [i for i in allList if IsPrime(i)]

while True:
  n = int(sys.stdin.readline())
  if n == 0: break
  cnt = 0
  for x in memo:
    if n < x <= 2 * n:
      cnt += 1
  print(cnt)