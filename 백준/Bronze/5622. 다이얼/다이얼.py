dial = input()
sec = 0

for i in dial:
  if i == 'A' or i == 'B' or i == 'C':
    sec += 3
  elif i == 'D' or i == 'E' or i == 'F':
    sec += 4
  elif i == 'G' or i == 'H' or i == 'I':
    sec += 5
  elif i == 'J' or i == 'K' or i == 'L':
    sec += 6
  elif i == 'M' or i == 'N' or i == 'O':
    sec += 7
  elif i == 'P' or i == 'Q' or i == 'R' or i == 'S':
    sec += 8
  elif i == 'T' or i == 'U' or i == 'V':
    sec += 9
  elif i == 'W' or i == 'X' or i == 'Y' or i == 'Z':
    sec += 10
print(sec)