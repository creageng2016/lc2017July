

class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1:
            return True
        elif num == 0:
            return False

        else:
            if num % 4 == 0 and self.isPowerOfFour(num/4):
                return True
            else:
                return False

if __name__ == '__main__':
    num = 16
    print Solution().isPowerOfFour(num)