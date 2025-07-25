class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r=0,1
        maxp=0

        while r<len(prices):
            if prices[l]<prices[r]:
                profit=prices[r]-prices[l]
                maxp=max(maxp,profit)
            else:
                l=r
            r+=1
        return maxp
    
#    class Solution:
#    def maxProfit(self, prices: List[int]) -> int:
#        currentMinPrice = max(prices)
#        MaxProfit = 0
#        for price in prices:
#            if currentMinPrice > price:
#                currentMinPrice = price
#            elif price > MaxProfit:
#                diff = price - currentMinPrice
#                if diff > MaxProfit:
#                    MaxProfit = diff
#        return MaxProfit