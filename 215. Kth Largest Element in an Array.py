import heapq
class Solution(object):
	def findKthLargest(self, nums, k):
		"""
		:type nums: List[int]
		:type k: int
		:rtype: int
		"""
		h = []
		for num in nums:
			heapq.heappush(h, num)
			# print h
		for _ in xrange(len(nums) - k):
			heapq.heappop(h)
		return heapq.heappop(h)

if __name__ == '__main__':
	# nums = [3,2,1,5,6,4]
	nums = [3,2,3,1,2,4,5,5,6]
	k = 4
	print Solution().findKthLargest(nums, k)