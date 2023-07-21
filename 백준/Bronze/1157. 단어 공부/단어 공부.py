inStr = input().upper()
uniq = list(set(inStr))
cnt = []

for i in uniq:
  cnt.append(inStr.count(i))

if cnt.count(max(cnt)) > 1:
  print('?')
else:
  maxIndex = cnt.index(max(cnt))
  print(uniq[maxIndex])