'''
def primeNumber(n):
    """
    n th prime number
    """
    k = 0
    l = 2

    while k <= n:
        L = []
        for p in range(1, l+1):
            if l % p == 0:
                L.append(p)
                if len(L) > 2:
                    break
        if len(L) == 2:
            k += 1

        l += 1

    return p
'''

'''
def primeNumber(n):
    """
    n th prime number
    """
    k = 0
    l = 2

    while k <= n:
        n_d = 0
        for d in range(1, l+1):
            if l % d == 0:
                n_d += 1
                if n_d == 2 and d == n:
                    k += 1
                elif n_d == 2 and d < l:
                    break
                else:
                    continue

        l += 1

    return d
'''

def primeNumber(n):
    """
    n th prime number
    """
    k = 0
    l = 2

    while k <= n:
        n_d = 0
        for d in range(1, l+1):
            print(d)
            if l % d == 0:
                n_d += 1
                if n_d == 2:
                    if d == n:
                        k += 1
                    else:
                        break
        l += 1

    return d

print(primeNumber(10))