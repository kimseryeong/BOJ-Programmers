import sys
string = sys.stdin.readline().strip()

stringSet = set()

for s in range(len(string)):
  for t in range(s+1, len(string)+1):
    stringSet.add(string[s:t])

print(len(stringSet))