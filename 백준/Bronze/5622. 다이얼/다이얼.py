dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
val = input()
sec = 0

for i in range(len(val)):
  for a in dial:
    if val[i] in a:
      sec += dial.index(a)+3
print(sec)
