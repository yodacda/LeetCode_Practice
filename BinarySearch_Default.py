def binarySearch(nums, target):
    low=0
    high=len(nums)-1

    while low<=high:
        mid= (low+high)//2

        if nums[mid] == target:
            print(mid)
            return mid

        if nums[mid] > target:
            high = mid - 1
        else:
            low = mid + 1

    return -1

nums=[1,2,3,4,5,6,7]
target=6
binarySearch(nums, target)