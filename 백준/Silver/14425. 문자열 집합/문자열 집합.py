import sys
input = sys.stdin.readline

N, M = map(int, input().split())
n_set = set()
m_list = []
cnt = 0

for _ in range(N):
  
  n_set.add(input())

for _ in range(M):
  m_list.append(input())

for m in m_list:
  if m in n_set:
    cnt += 1

print(cnt)