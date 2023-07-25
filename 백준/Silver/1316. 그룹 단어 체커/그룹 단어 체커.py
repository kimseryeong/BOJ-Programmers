n = int(input())
groupWord = n

for _ in range(n):
  word = input()
  for i in range(len(word)-1):
    if word[i] == word[i+1]:
      pass
    elif word[i] in word[i+1:]:
      groupWord -= 1
      break
print(groupWord)