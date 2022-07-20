class Solution:
    def twoSum(nums, target):
        result = []
        for num in range(0, len(nums)):
            for idx in range(num+1, len(nums)):
                if nums[num] + nums[idx] == target:
                    result.append(num)
                    result.append(idx)
        print(result)
        return result

    nums = [3,2,3]
    twoSum(nums, 6)