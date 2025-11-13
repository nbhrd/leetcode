def isPalindrome(x: int) -> bool:
    # ans = str(x)
    # return ans == ans[::-1]
    
    # without converting the integer to a string
    if x < 0:
        return False
    
    ans = 0
    num = x
    while num:
        ans = (ans * 10) + (num % 10)
        num //= 10
    
    return ans == x

print(isPalindrome(121))
print(isPalindrome(-121))
print(isPalindrome(10))