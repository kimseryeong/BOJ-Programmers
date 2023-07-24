import sys

credit_dic = {'A+': 4.5, 'A0': 4.0, 
         'B+': 3.5, 'B0': 3.0,
         'C+': 2.5, 'C0': 2.0,
         'D+': 1.5, 'D0': 1.0,
         'F' : 0.0}
result = 0
total = 0

for _ in range(20):
  sub, credit, grade = sys.stdin.readline().split()
  if grade == 'P':
    continue  
  total += float(credit)
  result += float(credit) * float(credit_dic[grade])
  
print('{:.6f}'.format(result / total))