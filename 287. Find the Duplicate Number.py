

class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = 0
        r = len(nums) - 1

        while l <= r:
        	mid = (l + r)/2
        	count  = 0
        	for i in range(len(nums)):
        		if nums[i] <= mid:
        			count += 1

        	if count > mid:
        		r = mid - 1
        	else:
        		l = mid + 1
        return l



if __name__ == '__main__':
	nums = [1,3,4,4,2]
	print Solution().findDuplicate(nums)