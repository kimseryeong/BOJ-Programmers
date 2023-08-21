N = input()
arrN = [i for i in N]
arrN = sorted(arrN)

arrN.reverse()

result = ''.join(s for s in arrN)
print(result)