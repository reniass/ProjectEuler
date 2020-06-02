'''
def nthTriangleNumber(n):
    if n == 1:
        return 0
    else:
        return n-1 + nthTriangleNumber(n-1)
'''
def nthTriangleNumber(n):
    v = 0
    for i in range(1, n):
        v += 1
    return v

def f():
    nthNumber = 0
    numberDivisors = 0
    triangleNumber = 1
    while numberDivisors < 501:
        nthNumber += 1

        numberDivisors = 0
        triangleNumber = nthTriangleNumber(nthNumber)

        for el in range(1, triangleNumber + 1):
            if triangleNumber % el == 0:
                numberDivisors += 1

    return triangleNumber, nthNumber



print(f())


