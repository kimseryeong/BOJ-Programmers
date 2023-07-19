str = input()
arr = []
sum = 0

for i in str:
  arr.append(i)
  
arr_re = list(reversed(arr))

for i in range(len(str)):
  if arr[i] == arr_re[i]:
    sum += 1

if sum == len(str):
  print(1)
else:
  print(0)