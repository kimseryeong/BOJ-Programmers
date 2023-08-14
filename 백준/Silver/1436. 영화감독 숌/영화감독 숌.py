n = int(input()) #n:n번째666
cnt, title = 0, 0 #cnt:666횟수,title:n번째종말의수

while True:
  if '666' in str(title):
    cnt += 1
  if cnt == n:
    break
  title += 1

print(title)