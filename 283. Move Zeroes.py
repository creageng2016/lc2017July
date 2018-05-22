class Solution(object):
	def moveZeroes(self, nums):
		"""
		:type nums: List[int]
		:rtype: void Do not return anything, modify nums in-place instead.
		"""

		# Solution 1: traverse and swap last 0 and last non 0
		lastNoneZero = 0
		for i in range(len(nums)):
			if nums[i] != 0:
				nums[i], nums[lastNoneZero] = nums[lastNoneZero], nums[i]
				lastNoneZero += 1
				# print lastNoneZero
		# print nums




if __name__ == '__main__':
	nums = [0,1,0,3,12]
	# nums = [0, 0, 0]
	print Solution().moveZeroes(nums)