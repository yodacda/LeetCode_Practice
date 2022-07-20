def maxSlidingWindow(nums, k):
    output=[]
    for n in range(len(nums)-k+1):
        res= max(nums[n], nums[n+1], nums[n+2])
        output.append(res)
    print(output)

nums = [1]
k = 1

maxSlidingWindow(nums,k)