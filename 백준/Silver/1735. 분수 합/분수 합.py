import sys
import math
input = sys.stdin.readline
a, b = map(int, input().split())
c, d = map(int, input().split())

bunja = (a*d + b*c)
bunmo = b*d

gong = math.gcd(bunja, bunmo)

print(bunja//gong, bunmo//gong)