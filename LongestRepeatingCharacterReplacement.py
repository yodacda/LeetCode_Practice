def characterReplacement(s, k):
    l, r = 0, 0
    count = {}
    res = 0
    for r in range(len(s)):
        count[s[r]] = 1 + count.get(s[r], 0)

        while(r-l+1)-max(count.values())>k:
            count[s[l]] -= 1
            l += 1
        res= max(res, r-l+1)
    print(res)
    return res

s = "AABABBA"
k = 1
characterReplacement(s, k)