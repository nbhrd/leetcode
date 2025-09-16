def reverse(x) -> int:
    res = 0
    if x >= 0:
        s = str(x)
        res = int(s[::-1])
    else:
        y = str(abs(x))
        res = int(y[::-1]) * -1

    if res < -(2**31) or (2**31) - 1 < res:
        return 0

    return res

print(reverse(123))
print(reverse(-123))
print(reverse(120))
print(reverse(1534236469))