import collections

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        c = collections.Counter(nums)
        return [num[0] for num in c.most_common()[-2:]]




if __name__ == '__main__':
	nums = [1,2,1,3,2,5]
	print Solution().singleNumber(nums)



# You first xor all numbers and then find a bit that is different in those two distinct numbers. This bit is used to divide all numbers into two group. Finally xor them individually, the two numbers left are the two distinct numbers.
# Great use of mask!

# class Solution(object):
#     def singleNumber(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[int]
#         """
#         xor = 0
#         a = 0
#         b = 0
#         for num in nums:
#             xor ^= num
#         mask = 1
#         while(xor&mask == 0):
#             mask = mask << 1
#         for num in nums:
#             if num&mask:
#                 a ^= num
#             else:
#                 b ^= num
#         return [a, b]