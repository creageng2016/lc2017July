

class MedianFinder(object):

	def __init__(self):
		"""
		initialize your data structure here.
		"""
		self.hq = []
		
	def addNum(self, num):
		"""
		:type num: int
		:rtype: void
		"""
		import bisect 
		# t = self.lt
		bisect.insort(self.hq, num)
		# print self.hq
		return
		
	def findMedian(self):
		"""
		:rtype: float
		"""
		n = len(self.hq)

		if n == 0:
			return
		elif n % 2 == 0:
			return (self.hq[n/2 - 1] + self.hq[n/2])/2.0
		else:
			return self.hq[n/2]


if __name__ == '__main__':
	obj = MedianFinder()
	obj.addNum(-1)
	obj.addNum(-2)
	obj.addNum(-3)
	obj.addNum(-4)
	obj.addNum(-5)

	print obj.findMedian()




# from heapq import *

# class MedianFinder:

#     def __init__(self):
#         self.heaps = [], []

#     def addNum(self, num):
#         small, large = self.heaps
#         heappush(small, -heappushpop(large, num))
#         if len(large) < len(small):
#             heappush(large, -heappop(small))

#     def findMedian(self):
#         small, large = self.heaps
#         if len(large) > len(small):
#             return float(large[0])
#         return (large[0] - small[0]) / 2.0


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()


