import re
import operator

class Solution(object):
	def diffWaysToCompute(self, s):
		"""
		:type input: str
		:rtype: List[int]

		"""
		# replace empty space
		tokens = re.split('(\D)', s)
		nums = map(int, tokens[::2])
		ops = map({'+': operator.add, '-': operator.sub, '*': operator.mul}.get, tokens[1::2])
		res = []
		def build(lo, hi):
			_t = []
			if lo == hi:
				return [nums[lo]]
			for i in xrange(lo, hi):
				# print i,hi
				for a in build(lo,i):
					for b in build(i + 1, hi):
						_t.append(ops[i](a, b))
			return _t

		   # return [ops[i](a, b)
				 #   for i in xrange(lo, hi)
				 #   for a in build(lo, i)
				 #   for b in build(i + 1, hi)]
		return build(0, len(nums) - 1)

		# pattern     = re.compile("\s+")
		# s           = re.sub(pattern, '', s)
		# # print s
		# tokens      = re.split("(\D)", s)
		# # print tokens
		# nums        = map(int, tokens[::2])

		# ops = {
		#     "+": operator.add,
		#     "-": operator.sub,
		#     "*": operator.mul
		# }

		# res = []
		# def build(lo, hi):
		#     _tmp = 
		#     if lo == hi:
		#         res.append(nums[lo])

		#     for i in range(lo, hi):
		#         for a in 












			
		
		
		
		
		
		



if __name__ == '__main__':
	s = "2*3-4*5"
	print Solution().diffWaysToCompute(s)



# import re
# import operator

# class Solution(object):
#     def diffWaysToCompute(self, s):
#         """
#         :type input: str
#         :rtype: List[int]
#         """
#         pattern = re.compile("\s+")
#         s = re.sub(pattern, '', s)

#         tokens = re.split("(\D)", s)
#         nums = map(int, tokens[::2])

#         res = []

#         ops = map({
#             "+": operator.add,
#             "-": operator.sub,
#             "*": operator.mul
#             }.get, tokens[1::2])

#         def build(lo, hi):
#             if lo == hi:
#                 return [nums[lo]]

#             res = []
#             for i in range(lo, hi):
#                 for a in build(lo, i):
#                     for b in build(i + 1, hi):
#                         res.append(ops[i](a, b))
#             return res

#             # return [ops[i](a, b) 
#             #         for i in range(lo, hi)
#             #         for a in build(lo, i)
#             #         for b in build(i + 1, hi)
#             #         ]

#         res = build(0, len(nums) - 1)
#         return res










# if __name__ == '__main__':
#     input = "2  *3-4*5"
#     print Solution().diffWaysToCompute(input)

























	   # patttern    = re.compile(r'\s+')
		# input       = re.sub(patttern, '', input) 

		# token   = re.split("(\D)", input)
		# # print token
		# nums    = map(int, token[::2])
		# # print nums
		# ops     = map( {"+":    operator.add, 
		#                 "-":    operator.sub,
		#                 "*":    operator.mul}.get,
		#             token[1:-1:2]
		#     )
		# # print ops
		# def build(lo, hi):
		#     if lo == hi:
		#         return [nums[lo]]
		#     return [ops[i](a, b) 
		#             for i in xrange(lo, hi)
		#             for a in build(lo,i)
		#             for b in build(i + 1, hi)
		#         ]
		# return build(0, len(nums) - 1)