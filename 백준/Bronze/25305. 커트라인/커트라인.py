n, k = map(int, input().split())
score = list(map(int, input().split()))

score = sorted(score)

print(score[::-1][k-1])