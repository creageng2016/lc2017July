class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        # The idea is to do binary search 
         to find the min index such that citations[i] >= 
         len(citations) - i, 
         then the answer is len(citations)-i
        """
        n = len(citations)
        l = 0
        r = n - 1
        
        while l <= r:
            m = (l + r) / 2
            hm = n - m
            if hm >= citations[m]:
                l = m + 1
            elif hm < citations[m]:
                r = m - 1
        
        return n-l
        
        
        
        
        
        