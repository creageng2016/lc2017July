class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        dp = [0 for i in range(len(prices))]
        if len(prices) <= 1:
        	return 0

        dp[1] = prices[1] - prices[0] if prices[1] > prices[0] else 0

        for i in range(2, len(prices)):









if __name__ == '__main__':
	
	prices = [1,2,3,0,2]
	print Solution().maxProfit(prices)
