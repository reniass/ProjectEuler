
def evenlyDivisible():
    n = 20
    while True:
        countDivisor = 0
        for d in range(1, 21):
            if n % d == 0:
                countDivisor += 1
            else:
                break
        if countDivisor == 20:
            return n
        n += 20

'''
def primeFactor(n):
    PrimeDivisor = []
    for n1 in range(2, n + 1):
        L = []
        for n2 in range(1, n1 + 1):
            if n1 % n2 == 0:
                L.append(n2)
        if len(L) == 2 and n % n1 == 0:
            PrimeDivisor.append(n1)
    return PrimeDivisor



def evenlyDivisible():
    n = 20
    L = [d for d in range(2, 20)]
    while len(L) != 0:
        L = [d for d in range(2, 20)]
        for d in reversed(range(2, 20)):
            if n % d == 0 and d in L:
                L.remove(d)
                for p in primeFactor(d):
                    if p in L:
                        L.remove(p)
            else:
                break
            if len(L) == 0:
                return n
        n += 20
  
'''








print(evenlyDivisible())
