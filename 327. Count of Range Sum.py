

class Solution(object):
    def countRangeSum(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        nums.sort()






if __name__ == '__main__':
	nums = [-2,5,-1]
	lower = -2
	upper = 2
	# return 3 
	print Solution().countRangeSum(nums, lower, upper)