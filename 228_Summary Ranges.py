class Solution(object):
	def summaryRanges(self, nums):
	    ranges, r = [], []
	    for n in nums:
	        if n-1 not in r:
	            r = []
	            ranges += r,
	        r[1:] = n,
	    return ['->'.join(map(str, r)) for r in ranges]


# class Solution(object):
#     def summaryRanges(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[str]
#         """
#         if not nums:
#             return []
#         if len(nums) == 1:
#             return [str(nums[0])]
        
#         res = []
#         prev = nums[0]
#         path    = str(prev)
#         for i in range(1, len(nums)):
#             curr = nums[i]
#             if curr != prev + 1:
#                 if str(prev) != path:
#                     path += "->" + str(prev)
#                 # if i == len(nums) - 1:
#                 #     path += "->" + curr
#                 res.append(path)
#                 path = str(curr)

#             if i == len(nums) - 1:
#                 # print path, curr
#                 if path != str(curr):
#                     path += "->" + str(curr)
#                 res.append(path)
#             prev = curr
        
#         return res      



#  About the commas :-)

# Three people asked about them in the comments, so I'll also explain it here as well. I have these two basic cases:

# ranges += [],
# r[1:] = n,
# Why the trailing commas? Because it turns the right hand side into a tuple and I get the same effects as these more common alternatives:

# ranges += [[]]
# or
# ranges.append([])

# r[1:] = [n]
# Without the comma, ...

# ranges += [] wouldn't add [] itself but only its elements, i.e., nothing.
# r[1:] = n wouldn't work, because my n is not an iterable.   