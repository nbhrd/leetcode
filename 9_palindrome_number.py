def isPalindrome(x: int) -> bool:
    s = str(x)
    return s == s[::-1]

print(isPalindrome(121))
print(isPalindrome(-121))
print(isPalindrome(10))