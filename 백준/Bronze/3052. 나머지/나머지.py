arr=[]

for i in range(10):
  a = int(input())
  arr.append(a%42)

arr_set = set(arr)

print(len(arr_set))