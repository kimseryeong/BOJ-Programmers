import sys

a = int(sys.stdin.readline())

if a >= 90:
  print('A')
elif a >= 80:
  print('B')
elif a >= 70:
  print('C')
elif a >= 60:
  print('D')
else:
  print('F')