

class Solution(object):
	def isSelfCrossing(self, x):
		"""
		:type x: List[int]
		:rtype: bool
		"""


		# point = 0
		
		# if len(x) < 4:
		# 	return False

		# ops = [lambda x: -x * 1j,
		# 		lambda x: -x,
		# 		lambda x: x * 1j,
		# 		lambda x: +x
		# 		]

		# for i in range(len(x)):
		# 	point += ops[i % 4](x[i])

		# point_r = point.real
		# point_img = point.imag

		# return True if point_r >= 0 and point_img <=0 else False
	  

if __name__ == '__main__':
	x = [1, 2, 2, 3, 4]
	# x = [1,1,2,1,1]
	# x = [1, 2, 3, 4]
	print Solution().isSelfCrossing(x)  



	# def isSelfCrossing(self, x):
	#     b = c = d = e = 0
	#     for a in x:
	#         if d >= b > 0 and (a >= c or a >= c-e >= 0 and f >= d-b):
	#             return True
	#         b, c, d, e, f = a, b, c, d, e
	#     return False