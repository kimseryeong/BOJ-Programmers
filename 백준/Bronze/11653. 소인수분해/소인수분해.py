import sys

N = int(sys.stdin.readline())

for i in range(2, N+1): #소수는 2부터
  if N % i == 0:
    #해당 숫자로 나눌 수 없을 때까지 나누기
      while N % i == 0:
          print(i)
          N /= i