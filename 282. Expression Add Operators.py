import 	collections
from 	operator import add, sub, mul

class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        nums 	= map(int, list(num))
       	ops 	= {"+":add, 
       				"-":sub,
       				"*": mul}
       	curr 	= 0
       	res 	= []
	
		def build(lo, hi, path, total):
			res = []

			if lo == hi:
				if path == target:
					res.append(path)
				return

			for i in range(lo, i):
				
				









if __name__ == '__main__':
	num = "232"
	target = 8
	print Solution().addOperators(num, target)
        