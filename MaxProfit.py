class Solution:
    def maxProfit(prices: list[int]) -> int:
        maxProfit = 0
        curLowest = prices[0]

        for x in range(1, len(prices)):
            if prices[x] < curLowest:
                curLowest = prices[x]
            elif (prices[x] - curLowest) > maxProfit:
                maxProfit = prices[x] - curLowest

        return maxProfit


class Solution2:
    def maxProfit2(prices: list[int]) -> int:
        maxProfit = 0

        for x in range(1, len(prices)):
            curPrice = prices[x]
            prevPrice = prices[x - 1]
            if curPrice > prevPrice:
                profit = curPrice - prevPrice
                maxProfit += profit

        return maxProfit


print(Solution2.maxProfit2([5, 4, 3, 2, 1]))
