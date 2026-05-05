def max_sum(s):
    s = s + s
    n = len(s) // 2

    left = 0
    curr = 0
    ans = 0
    seen = set()

    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            curr -= ord(s[left]) - 96
            left += 1

        seen.add(s[right])
        curr += ord(s[right]) - 96

        if right - left + 1 <= n:
            ans = max(ans, curr)

    return ans


s = input()
print(max_sum(s))