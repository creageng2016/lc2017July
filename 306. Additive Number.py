
class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        Just trying all possibilities 
        for the first two numbers and checking whether the rest fits.
        """
        n = len(num)

        for i in range(1, n/2 +  1):
            if num[0] == '0' and i > 1:continue
            for j in range(i + 1, n):
                if num[i] == '0' and j - i > 1:
                    continue
                # print i, j
                # if num[i] == '0': continue
                # if num[j] == '0':
                #     continue
                if self.dfs(0, i, j, num):
                    # print i, j
                    return True
        return False

    def dfs(self, i, j, k, num):
        x1 = num[i: j]
        x2 = num[j: k]
        # print i, j, k, x1, x2
        total = str(int(x1) + int(x2))
        # newstart = len(total)
        if not num[k:].startswith(total): return False
        if k + len(total) == len(num): return True

        return self.dfs(j, k, k + len(total), num)

if __name__ == '__main__':
    # main()
    # num = "199100199"
    num = '000'
    print Solution().isAdditiveNumber(num)
    # def isAdditiveNumber(self, num):
    #     n = len(num)
    #     for i, j in itertools.combinations(range(1, n), 2):
    #         a, b = num[:i], num[i:j]
    #         if a != str(int(a)) or b != str(int(b)):
    #             continue
    #         while j < n:
    #             c = str(int(a) + int(b))
    #             if not num.startswith(c, j):
    #                 break
    #             j += len(c)
    #             a, b = b, c
    #         if j == n:
    #             return True
    #     return False