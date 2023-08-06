import sys
a, b, c = map(int, sys.stdin.readline().split())

byeon=[]
byeon.extend([a, b, c])
byeon.sort()

if byeon[2] < byeon[0] + byeon[1]:
  print(sum(byeon))
else:
  print(byeon[0]+byeon[1]+byeon[0]+byeon[1]-1)
