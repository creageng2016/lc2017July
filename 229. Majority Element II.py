
import collections
class Solution(object):
	"""
	:type nums: List[int]
	:rtype: List[int]
	"""
		# c = collections.Counter(nums)
		# num_cut = len(nums)/3

		# res = []
		# for i, v in c.items():
		#     if v > num_cut:
		#         res.append(i)
		# return res
	def majorityElement(self, nums):
		ctr = collections.Counter()
		for n in nums:
			ctr[n] += 1
			print ctr
			if len(ctr) == 3:
				print "diminishing"
				ctr -= collections.Counter(set(ctr))
				print ctr
		return [n for n in ctr if nums.count(n) > len(nums)/3]


if __name__ == '__main__':
	nums = [1,1,4, 5, 1,1, 1, 3,3,2,2,2]
	print Solution().majorityElement(nums)