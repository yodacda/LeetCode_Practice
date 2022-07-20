# from collections import Counter
# def checkInclusion(s1, s2):
#     if len(s1) > len(s2):
#         return False
#     length_of_s1 = len(s1)
#     s1_Counter = Counter(s1)
#     window_Counter = Counter()
#
#     for i, c in enumerate(s2):
#         window_Counter[c] += 1
#
#         if i >= length_of_s1:
#             element_from_left = s2[i - length_of_s1]
#
#             if window_Counter[element_from_left] == 1:
#                 del window_Counter[element_from_left]
#             else:
#                 window_Counter[element_from_left] -= 1
#
#         if window_Counter == s1_Counter:
#             return True
#
#     return False



def secondSolution(s1, s2):

    if len(s1) > len(s2):
        return False

    s1_Count = dict()
    for i in s1:
        s1_Count[i] = s1_Count.get(i, 0) + 1

    window_Count = dict()
    len_Of_S1 = len(s1)

    for i,c in enumerate(s2):
        window_Count[c] = window_Count.get(c, 0) + 1

        if i >= len_Of_S1:
            element_Of_Left = s2[i- len_Of_S1]

            if window_Count[element_Of_Left] == 1:
                del window_Count[element_Of_Left]
            else:
                window_Count[element_Of_Left] -= 1

        if window_Count == s1_Count:
            return True

    return False




s1 = "ab"
s2 = "eidbaooo"
#checkInclusion(s1, s2)
secondSolution(s1, s2)