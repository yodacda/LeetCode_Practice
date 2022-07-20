# def lengthOfLongestSubstring(s):
#     start=0
#     end=0
#     max_len=0
#     storeDict={}
#     while end < len(s):
#         if s[end] in storeDict and storeDict[s[end]] >= start:
#             start = storeDict[s[end]] + 1
#         max_len = max(max_len, end-start+1)
#         storeDict[s[end]] = end
#         end += 1
#     print(max_len)
#     return max_len

### Another solution

def lengthOfLongestSubstring(s):
    left = 0
    max_len = 0
    hashSet = set()
    for right in range(len(s)):
        while s[right] in hashSet:
            hashSet.remove(s[left])
            left += 1
        hashSet.add(s[right])
        max_len = max(max_len, right-left+1)
    print(max_len)
    return max_len



s="Hello World!"
lengthOfLongestSubstring(s)