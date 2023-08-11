n = int(input())

for i in range(1, n+1):
  num = sum((map(int, str(i))))
  num_sum = i + num
  if num_sum == n:
      print(i)
      break
  if i == n:  # 생성자 i와 입력값이 같다는 것은 생성자가 없다는 뜻
      print(0)