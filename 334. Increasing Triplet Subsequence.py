

class Solution(object):
    # def increasingTriplet(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: bool
    #     """
    #     n = len(nums)
    #     if n < 3:
    #         return False

    #     lmin = i = 0 
    #     rmax = j = n - 1

    #     while i < n - 1:
    #         if nums[i] <= nums[lmin]:
    #             lmin = i
    #         i += 1

    #     while j > 0:
    #         if nums[j] >= nums[rmax]:
    #             rmax = j
    #         j -= 1
    #     print rmax, lmin
    #     return rmax - lmin > 1
    # def increasingTriplet(self, nums):
    #     try:
    #         inc = [float('inf')] * 2
    #         for x in nums:
    #             print x, inc
    #             inc[bisect.bisect_left(inc, x)] = x
    #         return False
    #     except:
    #         return True

def increasingTriplet(self, nums):
    inc = [float('inf')] * 2
    for x in nums:
        i = bisect.bisect_left(inc, x)
        if i >= 2:
            return True
        inc[i] = x
    return False

if __name__ == '__main__':

    # nums = [5, 4, 3, 2, 1]
    # nums = [1, 1, 1, 1, 1, 1, 1, 1]
    nums = [2, 5, 3, 4, 5]
    # nums = [1, 4, 3, 2, 5]
    print Solution().increasingTriplet(nums)