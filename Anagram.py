
# def isAnagram(s: str, t: str) -> bool:
#     result = False
#     print(s)
#     print(t)
#     if len(s) == len(t):
#         for i in range(len(s)):
#             for j in range(len(t)):
#                 print(i, j)
#                 if s[i] == t[j]:
#                     print(s[i], t[j])
#                     result = True
#                     break
#                 else:
#                     print(s[i], t[j])
#                     result = False
#     print(result)
#     return result

def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    countS, countT = {}, {}

    for i in range(len(s)):
        countS[s[i]] = 1 + countS.get(s[i],0)
        countT[t[i]] = 1 + countT.get(t[i],0)

    for c in countS:
        if countS[c] != countT.get(c,0):
            return False

    return True


isAnagram("aacc", "ccac");