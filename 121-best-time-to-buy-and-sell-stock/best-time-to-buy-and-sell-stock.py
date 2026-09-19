class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_arr=prices[0]
        min_arr=0
        for i in range(len(prices)):
            if prices[i]<max_arr:
                max_arr=prices[i]
            min_arr=max(min_arr,prices[i]-max_arr)
        return min_arr