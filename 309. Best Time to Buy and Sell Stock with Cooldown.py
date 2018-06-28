class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n       = len(prices)
        if n <= 1:
            return 0

        hold    = [0 for i in range(n)]
        unhold  = [0 for i in range(n)]

        hold[0] = -prices[0]

        for i in range(1, n):
            if i == 1:
                hold[i] = max(hold[0], -prices[i])
                # hold[i] = 0
            else:
                hold[i] = max(hold[i - 1], unhold[i - 2] - prices[i])

            unhold[i]   = max(unhold[i - 1], hold[i - 1] + prices[i])
        
        return unhold[-1]

        # dp = [0 for i in range(len(prices))]
        # if len(prices) <= 1:
        # 	return 0

        # dp[1] = prices[1] - prices[0] if prices[1] > prices[0] else 0

        # for i in range(2, len(prices)):


if __name__ == '__main__':
	
	prices = [1,2,3,0,2]
	print Solution().maxProfit(prices)
