class Solution(object):
	def summaryRanges(self, nums):
	    ranges, r = [], []
	    for n in nums:
	        if n-1 not in r:
	            r = []
	            ranges += r,
	        r[1:] = n,
	    return ['->'.join(map(str, r)) for r in ranges]


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