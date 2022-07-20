def findMin(nums):
    left, right = 0, len(nums)-1
    res = nums[left]

    while left <= right:
        if nums[left] < nums[right]:
            res = min(res, nums[left])
            break

        mid = (left + right) // 2
        res = min(res, mid)
        if nums[mid] >= nums[left]:
            left = mid + 1
        else:
            right = mid -1

    print(res)
    return res


nums = [4,5,6,7,0,1,2]
findMin(nums)