def topKFrequent(nums, k):
    countNum = {}
    output = [[] for i in range(len(nums) + 1)]
    for num in nums:
        countNum[num] = 1 + countNum.get(num, 0)

    print(countNum)

    for numKey, numValue in countNum.items():
        output[numValue].append(numKey)

    res = []
    for i in range(len(output)-1, 0, -1):
        for n in output[i]:
            res.append(n)
            if len(res) == k:
                return res

nums = [1,1,1,2,2,3]
topKFrequent(nums,2)
