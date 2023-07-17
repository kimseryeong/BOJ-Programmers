arr = [False for i in range(30)]

for i in range(28):
  num = int(input())
  arr[num-1] = True

for i in range(30):
  if arr[i] == False:
    print(i+1)