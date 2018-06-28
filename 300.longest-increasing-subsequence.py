import bisect
class Solution(object):
	def lengthOfLIS(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		ins = []

		for x in nums:
			pos = bisect.bisect_left(ins, x)
			if pos == len(ins):
				ins.append(x)
			else:
				ins[pos] = x
		return len(ins)



		# if not nums:
		# 	return 0

		# # maxl = 0
		# instack = []
		# instack.append(nums[0])
		# maxl = 1

		# for i in range(1,len(nums)):		
		# 	if nums[i] <= instack[-1]:
		# 		while instack and instack[-1] >= nums[i]:
		# 			instack.pop()

		# 	instack.append(nums[i])
		# 	maxl = max(maxl, len(instack))
		# return maxl


if __name__ == '__main__':
	# nums = [10,9,2,5,3,4]
	nums = [1,3,6,7,9,4,10,5,6]
	# nums = [-2, -1]
	print Solution().lengthOfLIS(nums)


