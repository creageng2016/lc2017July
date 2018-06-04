

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # Assume dp[i] is the fewest number of coins making up amount i, 
        # then for every coin in coins, dp[i] = min(dp[i - coin] + 1).
        
        MAX = float('inf')
        dp = [MAX for i in range(amount + 1)]     
        dp[0] = 0

        for i in range(1, amount + 1):
            # print [dp[i - c] if c < i else MAX for c in coins]
            dp[i] = min(dp[i - c]  if c <= i else MAX for c in coins) + 1

        return dp[amount]



        # MAX = float('inf')
        # dp = [0] + [MAX] * amount

        # for i in range(1, amount + 1):
        # 	dp[i] = min([dp[i - c] if i >= c else MAX for c in coins] ) + 1

        # return dp[amount]
# class Solution(object):
#     def coinChange(self, coins, amount):
#         MAX = float('inf')
#         dp = [0] + [MAX] * amount

#         for i in xrange(1, amount + 1):
#             dp[i] = min([dp[i - c] if i - c >= 0 else MAX for c in coins]) + 1

#         return [dp[amount], -1][dp[amount] == MAX]



        # coins.sort()
        # if not coins:
        # 	return -1
        # if amount < coins[0]:
        # 	return -1

        # if amount == :
        # 	return 1
        # else:
        # 	res = 1000000
        # 	for c in coins:
        # 		res = min(res, self.coinChange(coins, amount - c) + 1)
        # 		print res 
        # 	return res


if __name__ == '__main__':
	coins = [1, 2, 5]
	amount = 11
	print Solution().coinChange(coins, amount)