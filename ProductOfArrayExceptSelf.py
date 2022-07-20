def productExceptSelf(nums):
    output=[]   #[1] * (len(nums))
    prefix=1
    for n in range(len(nums)):
        output[n] = prefix
        prefix *= nums[n]
    postfix=1
    for n in range(len(nums)-1, -1, -1):
        output[n] *= postfix
        postfix *= output[n]
    return output

nums = [1,2,3,4]
productExceptSelf(nums)




