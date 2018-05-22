class Solution(object):
    def wordPattern(self, pattern, word):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        words = word.split(" ")
        if len(pattern) != len(words):
            return False
        
        p2s = collections.defaultdict(str)
        s2p = collections.defaultdict(str)

        for i in range(len(pattern)):
            p = pattern[i]
            s = words[i]
            
            if p not in p2s and s not in s2p:
                p2s[p] = s
                s2p[s] = p
            else:
                if p2s[p] != s or s2p[s] != p:
                    return False
        return True


# def wordPattern(self, pattern, str):
#     s = pattern
#     t = str.split()
#     return len(set(zip(s, t))) == len(set(s)) == len(set(t)) and len(s) == len(t)