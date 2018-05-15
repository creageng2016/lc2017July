


class Solution(object):
	def searchMatrix(self, matrix, target):
		"""
		:type matrix: List[List[int]]
		:type target: int
		:rtype: bool
		"""
		if not matrix:
			return False

		m 	=	len(matrix)
		n 	= 	len(matrix[0])

		row = m - 1
		col = 0

		while row >= 0 and col < n:
			# print row, col
			if matrix[row][col] > target:
				row -= 1
			elif matrix[row][col] < target:
				col += 1
			else:
				# print col, row
				return True
		return False

if __name__ == '__main__':

	matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
	  
	target = 20

	print Solution().searchMatrix(matrix, target)