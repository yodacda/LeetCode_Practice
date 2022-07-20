def maxArea(height):
    # res = 0
    # for l in range(len(height)):
    #     for r in range(l+1, len(height)):
    #         area = (r-l) * min(height[l], height[r])
    #         res = max(res, area)
    # return res

    # above code giving Time limit exceeded when we submit in Leet Code

    res = 0
    l, r = 0, len(height)-1
    while l<r:
        area = (r - l) * min(height[l], height[r])
        res = max(res, area)

        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
    print(res)
    return res


height = [1,8,6,2,5,4,8,3,7]
maxArea(height)
