def sortNumbers(nums):
    for idx in range(0, len(nums)):
        for idx1 in range(idx+1, len(nums)):
            if nums[idx] > nums[idx1]:
                temp = nums[idx]
                nums[idx] = nums[idx1]
                nums[idx1] = temp
    print(nums)

nums = [5, 2, 8, 7, 1]
sortNumbers(nums)