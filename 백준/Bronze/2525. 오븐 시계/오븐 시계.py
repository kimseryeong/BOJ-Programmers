import sys

h, m = map(int, sys.stdin.readline().split())
t = int(input())

hour = (m+t)//60
min = (m+t)%60

if(m+t >= 60):
  if(h+hour >= 24):
    h = h - 24
  h = h + hour
  print(h, min)

else:
  if(h >= 24):
    h = h - 24
  print(h, m+t)