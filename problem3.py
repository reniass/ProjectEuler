

def largestPrimeFactor(n):
    primeFactor = 1
    PrimeDivisors = []
    number = n
    while number != 1:
        for n1 in range(2, int(number + 1)):
            L = []
            for n2 in range(1, n1 + 1):
                if n1 % n2 == 0:
                    L.append(n2)

            if len(L) == 2 and number % n1 == 0:
                if n1 not in PrimeDivisors:
                    PrimeDivisors.append(n1)
                primeFactor = n1

                number = number / primeFactor
                break
    #return PrimeDivisors
    largestDivisor = 1
    for prime in PrimeDivisors:
        if prime > largestDivisor:
            largestDivisor = prime
    return largestDivisor

print(largestPrimeFactor(600851475143))





