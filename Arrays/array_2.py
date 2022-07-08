def maxProfit( prices):
    profit = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i-1]:
            profit += prices[i] - prices[i-1]

    print(profit)
    return profit


maxProfit([7,1,5,3,6,4])
maxProfit([1,2,3,4,5])