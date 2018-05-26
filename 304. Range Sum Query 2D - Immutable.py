class NumMatrix(object):

	def __init__(self, matrix):
		"""
		:type matrix: List[List[int]]
		"""
		self.matrix = matrix
		self.accumSum = self.getaccumSum()
   
	def getaccumSum(self):
		if not self.matrix:
			return [[]]
		dp = [[0 for j in range(len(self.matrix[0]))] for i in range(len(self.matrix))]
		dp[0][0] = self.matrix[0][0]
		for j in range(1, len(self.matrix[0])):
			# print self.matrix[0][j]
			# print dp[0][j - 1]
			dp[0][j] = dp[0][j -1] + self.matrix[0][j]
		
		for i in range(1, len(self.matrix)):
			dp[i][0] = dp[i - 1][0] + self.matrix[i][0]
		
		for i in range(1, len(self.matrix)):
			for j in range(1, len(self.matrix[0])):
				dp[i][j] = dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1] + self.matrix[i][j]
		return dp

	def sumRegion(self, row1, col1, row2, col2):
		"""
		:type row1: int
		:type col1: int
		:type row2: int
		:type col2: int
		:rtype: int
		"""
		# print self.accumSum
		# row1, col1, row2, col2 = row1 - 1, col1 - 1, row2 - 1, col2 - 1
		left = self.accumSum[row2][col1 - 1] if col1 > 0 else 0
		top = self.accumSum[row1 - 1][col2] if row1 > 0 else 0
		topleft = self.accumSum[row1 - 1][col1 - 1] if row1 > 0 and col1 > 0 else 0

		return self.accumSum[row2][col2] + topleft - top - left