

class Solution(object):
	def wiggleSort(self, nums):
		"""
		:type nums: List[int]
		:rtype: void Do not return anything, modify nums in-place instead.
		"""
		size = len(nums)
		snums = sorted(nums)
		for x in range(1, size, 2) + range(0, size, 2):
			nums[x] = snums.pop()
		return nums



if __name__ == '__main__':
	nums = [1, 5, 1, 1, 6, 4]
	print Solution().wiggleSort(nums)