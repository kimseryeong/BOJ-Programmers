from bisect import bisect_left, bisect_right #이진탐색 모듈
from sys import stdin

n = stdin.readline().rstrip()
card = list(map(int, stdin.readline().split()))
m = stdin.readline().rstrip()
confirm = list(map(int, stdin.readline().split()))
card.sort() #이진탐색을 위한 오름차순 정렬

def count_by_range(a, left, right):
  idxRight = bisect_right(a, right) #list에서 value가 들어갈 가장 오쪽 인덱스
  idxLeft = bisect_left(a, left) #list에서 value가 들어갈 가장 왼쪽 인덱스
  return idxRight - idxLeft

for i in range(len(confirm)):
  print(count_by_range(card, confirm[i], confirm[i]), end=' ')
