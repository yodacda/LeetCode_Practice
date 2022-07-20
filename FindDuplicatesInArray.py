def containDuplicate(nums) -> bool:
    hashSet = set()
    result = False
    for num in nums:
        if num in hashSet:
            result = True
            return result
        hashSet.add(num)
    print(result)
    return result

containDuplicate([1,2,3,1])