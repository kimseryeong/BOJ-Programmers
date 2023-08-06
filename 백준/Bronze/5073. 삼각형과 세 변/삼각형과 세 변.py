import sys
while True:
  byeon = []
  a, b, c = map(int, sys.stdin.readline().split())
  
  if a == b == c == 0:
    break
    
  byeon.extend([a, b, c])
  byeon.sort()

  if byeon[2] >= byeon[0] + byeon[1]:
    print('Invalid')
  elif a==b==c:
    print('Equilateral')
  elif a==b or a==c or b==c:
    print('Isosceles')
  elif a != b != c:
    print('Scalene')
