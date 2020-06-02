def sumSquares(n):
    sum = 0
    for number in range(1, n+1):
        sum += number ** 2

    return sum


def squareSum(n):
    sum = 0
    for number in range(1, n+1):
        sum += number
    return sum ** 2

print(sumSquares(100))
print(squareSum(100))

print(squareSum(100) - sumSquares(100))