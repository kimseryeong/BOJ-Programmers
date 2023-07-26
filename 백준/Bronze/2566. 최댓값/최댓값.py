arr = [list(map(int, input().split())) for _ in range(9)]
maxVal = 0
row, col = 0, 0

for i in range(9):
  for j in range(9):
    if maxVal <= arr[i][j]:
      maxVal = arr[i][j]
      row = i+1
      col = j+1
      
print(maxVal)
print(row, col)