def search(nums, target):
    low, high = 0, len(nums)-1

    while low <= high:
        mid = (low+high)//2
        if target == nums[mid]:
            print(mid)
            return mid

        if target < nums[mid]:
            if nums[low] > nums[mid] or target >= nums[low]:
                high = mid - 1
            else:
                low = mid + 1
        else:
            if nums[mid] > nums[high] or target <= nums[high]:
                low = mid + 1
            else:
                high = mid - 1

    return -1


nums = [4,5,6,7,0,1,2]
target = 0
search(nums,target)