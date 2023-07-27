text = [input() for _ in range(5)]

for x in range(max(len(t) for t in text)):
  for y in range(5):
    if x < len(text[y]):
      print(text[y][x], end='')