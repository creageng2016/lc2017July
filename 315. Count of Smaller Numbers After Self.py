

import collections
import bisect
class Solution(object):
	"""
	:type nums: List[int]
	:rtype: List[int]
	"""
	# res = [0 for i in range(len(nums))]

	# for i in range(len(nums) - 1):
	# 	cnt = 0
	# 	for j in range(i, len(nums)):
	# 		if nums[j] < nums[i]:
	# 			cnt += 1
	# 	res[i] = cnt
	# return res

	def countSmaller(self, nums):
		# tmp = collections.deque() 
		tmp = []
		ret = [] 
		for n in nums[::-1]:
			idx = bisect.bisect_left(tmp, n)
			ret += idx,
			# print idx
			tmp.insert(idx, n)
			print tmp
		return ret[::-1]



if __name__ == '__main__':
	nums = [5,2,6,1]
	Solution().countSmaller(nums)