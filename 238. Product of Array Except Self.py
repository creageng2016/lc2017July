# class Solution:
#     # @param {integer[]} nums
#     # @return {integer[]}
#     def productExceptSelf(self, nums):
#         p = 1
#         n = len(nums)
#         output = []
#         for i in range(0,n):
#             output.append(p)
#             p = p * nums[i]
#         p = 1
#         for i in range(n-1,-1,-1):
#             output[i] = output[i] * p
#             p = p * nums[i]
#         return output

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        prod = []
        prev = 1

        for l in range(len(nums)):
            prod.append(prev)
            prev *= nums[l]

        right = 1
        for r in range(len(nums)-1, -1, -1):
            prod[r] = prod[r] * right
            right *= nums[r]

        return prod





if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    print Solution().productExceptSelf(nums)        