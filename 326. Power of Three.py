

# class Solution(object):
# 	def isPowerOfThree(self, n):
		"""
		:type n: int
		:rtype: bool
		"""
		# n = abs(n)
        
		# if n <= 0:
		# 	return False
		# elif n == 1:
		# 	return True
		# else:
		# 	return n % 3  == 0 and self.isPowerOfThree(n / 3)
class Solution:
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n < 1:
            return False
        while n % 3 == 0:
            n //= 3
        return True if n == 1 else False




if __name__ == '__main__':
	n = 5
	print Solution().isPowerOfThree(n)