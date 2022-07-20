def maxProfit(prices):
    # profit=0
    # for pr1 in range(len(prices)):
    #     for pr2 in range(pr1+1, len(prices)):
    #         if prices[pr1] > prices[pr2]:
    #             break
    #         else:
    #             res = prices[pr2]-prices[pr1]
    #             profit = max(res,profit)
    # print(profit)


    #### Above one taking long time and it has two loops
    #### Below one time complexity is O(n)

    l, r = 0, 1
    maxP = 0
    while r < len(prices):
        if prices[l] < prices[r]:
            profit = prices[r] - prices[l]
            maxP = max(profit, maxP)
        else:
            l = r
        r += 1
    print(maxP)



prices = [7,6,4,3,1]
maxProfit(prices)