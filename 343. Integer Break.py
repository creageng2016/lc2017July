
class Solution(object):
	def integerBreak(self, n):
		"""
		:type n: int
		:rtype: int
		"""
		if n <= 2:
			return 1
		if n == 3:
			return 2
		
		dp = [i for i in range(n + 1)]
		for i in range(2, n + 1):
			for j in range(1, i):
				dp[i] = max(dp[i], dp[j] * dp[i - j])

		return dp[n]



if __name__ == '__main__':
	n = 10
	# You may assume that n is not less than 2 and not larger than 58
	print Solution().integerBreak(n)