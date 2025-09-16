def longest_common_prefix(strs):
    if not strs:
        return ""
    first_str = strs[0]
    ans = ""
    for ch in first_str:
        ans += ch
        if all(s.startswith(ans) for s in strs):
            continue
        else:
            return ans[:-1]
    return ans

print(longest_common_prefix(["flower", "flow", "flight"]))
print(longest_common_prefix(["dog", "racecar", "car"]))