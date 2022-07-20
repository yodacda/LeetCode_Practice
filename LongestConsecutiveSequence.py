def longestConsecutive(nums):
    numSet = set(nums)
    longest=0
    for n in nums:
        #Check if its start of a sequence
        if (n-1) not in numSet:
            length=0
            while (n+length) in numSet:
                length += 1
            longest = max(length, longest)
    print(longest)
    return longest

nums = [100,4,200,1,3,2]
longestConsecutive(nums)