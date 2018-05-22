

class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        import math
        dp = [100 for i in range(n + 1)]
        dp[0] = 0
        # dp[1] = 1
        for i in range(n + 1):
            j = 1
            while j * j <= i:  
            # for j in range(int(math.sqrt(i)) + 1):
                dp[i] = min(dp[i], dp[i - j * j] + 1)
                j += 1
        return dp[n]

if __name__ == '__main__':
	# n = 12
	n = 12
	print Solution().numSquares(n)