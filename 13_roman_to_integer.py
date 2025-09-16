def romanToInt(s: str) -> int:
    ans = 0
    roman = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }

    for i in range(len(s)):
        current = roman[s[i]]
        next_val = roman[s[i+1]] if i+1 < len(s) else None

        if next_val and current < next_val:
            ans -= current
        else:
            ans += current
    
    return ans


print(romanToInt("III"))
print(romanToInt("IV"))
print(romanToInt("IX"))
print(romanToInt("LVIII"))
print(romanToInt("MCMXCIV"))