import time


def pythagorean():
    L = []
    start_time = time.time()
    for i in range(1, 999):
        a = i
        for j in range(1, 999):
            b = j
            for k in range(1, 999):
                c = k
                if a + b + c == 1000 and [a, b, c] not in L and a**2 + b**2 == c**2:
                    L.append([a, b, c])
    end_time = time.time()
    print(end_time - start_time)
    return L, L[0][0] * L[0][1] * L[0][2]


print(pythagorean())