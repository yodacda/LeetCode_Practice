def search(nums, target):
    pointer=0
    for n in range(len(nums)):
        if nums[n] == target:
            pointer=1
            return n
    if pointer==0:
        return -1

nums = [-1,0,3,5,9,12]
target = 2
search(nums,target)