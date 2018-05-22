class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        ugs = [1]
        i2 = i3 = i5 = 0
        
        while n >= 0 :
            # i index is the last index, of urgly number that limit the ugly number
            u2 = ugs[i2] * 2
            u3 = ugs[i3] * 3
            u5 = ugs[i5] * 5
            
            newug = min(u2, u3, u5)
            if newug == u2:
                i2 += 1
            elif newug == u3:
                i3 += 1
            else:
                i5 += 1
            if ugs[-1] != newug:
                # skip duplicates
                ugs.append(newug)
            n -= 1
        # print ugs
        return ugs[-1]



if __name__ == '__main__':
    n = 10
    print Solution().nthUglyNumber(n)