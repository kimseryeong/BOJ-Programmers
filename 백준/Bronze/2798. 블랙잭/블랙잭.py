from itertools import combinations

n, m = map(int, input().split())
cardList = list(map(int, input().split()))


cardSum = [sum(card) for card in combinations(cardList, 3) if sum(card) <= m]
print(max(cardSum))