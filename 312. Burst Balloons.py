

class Solution(object):
	def maxCoins(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		nums 	= [1] + nums + [1]
		n 		= len(nums)
		dp		= [[0] * n for i in range(n)]

		def calculate(i, j):
			if dp[i][j] or j = i + 1:
				return dp[i][j]
			coins = 0
			for k in range(i + 1, j):
				coins = max(coins, nums[i] * nums[k] * nums[j])






		# if len(nums) == 0:
		# 	return 1
		# if len(nums) == 1:
		# 	return nums[0]
				



		# maxres = 0
		# for i in range(len(nums)):
		# 	if i == 0:
		# 		prod = nums[i] * nums[i + 1]
		# 	elif i == len(nums) - 1:
		# 		prod = nums[i - 1] * nums[i]
		# 	else:
		# 		prod = nums[i] * nums[i - 1] * nums[i + 1]
		# 	# print i
		# 	maxres = max(self.maxCoins(nums[:i] + nums[i + 1:]) + prod, maxres)

		# return maxres


if __name__ == '__main__':
	# nums = [3, 1, 5, 8]
	nums = [35,16,83,87,84,59,48,41,20,54]

	# 1849648

	print Solution().maxCoins(nums)        