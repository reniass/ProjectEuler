def isPalindrome(s):
    reverseS = s[::-1]
    if s == reverseS:
        return True
    else:
        return False


print(isPalindrome('mama'))

def largestPalindrome():
    n = 1
    biggestPalindromeNumber = 0
    for n1 in range(100, 999):
        for n2 in range(100, 999):
            n = n1 * n2
            s = str(n)

            if isPalindrome(s) == True and n > biggestPalindromeNumber:
                biggestPalindromeNumber = n
    return biggestPalindromeNumber

print(largestPalindrome())