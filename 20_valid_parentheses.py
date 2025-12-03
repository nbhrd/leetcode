def isValid(s: str) -> bool:
    """
    :type s: str
    :rtype: bool
    """
    dic = {
        ")" : "(",
        "]" : "[",
        "}" : "{",
    }
    stack = []

    for ch in s:
        if ch in dic.values():
            stack.append(ch)
        elif stack != [] and dic[ch] == stack[-1]:
            stack.pop()
        else:
            return False
    
    return stack == []

print(isValid("()"))
print(isValid("()[]{}"))
print(isValid("(]"))
print(isValid("([])"))
print(isValid("([)]"))