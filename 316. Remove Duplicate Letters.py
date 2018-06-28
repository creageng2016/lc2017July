import collections
class Solution(object):
    def removeDuplicateLetters(self, s):
        rindex = {c: i for i, c in enumerate(s)}
        result = ''
        for i, c in enumerate(s):
            if c not in result:
                while c < result[-1:] and i < rindex[result[-1]]:
                    result = result[:-1]
                result += c
        return result

if __name__ == '__main__':
    # s = "bczbc"
    # return "abc"
    s = "cbacdcbc"
    # return "acdb"
    print Solution().removeDuplicateLetters(s)