class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        # myPrime = [2, 3, 5]
        # d       = False
        # num = abs(num)
        
        # while num > 1:
        #     print num
        #     for _prime in myPrime:
        #         if num % _prime == 0:
        #             d = True
        #             num /= _prime
        #     if not d:
        #         break
        #     else:
        #         d = False
        

        # if num > 1:
        #     return False
        # else:
        #     return True

        for p in 2, 3, 5:
    while num % p == 0 < num:
        num /= p
return num == 1
            

if __name__ == '__main__':
    num = -2147483648
    print Solution().isUgly(num)