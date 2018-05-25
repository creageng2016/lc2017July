class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        secret = list(secret)
        guess = list(guess)
        n = len(secret)
        ak = 0
        for i in range(n):
            if secret[i] == guess[i]:
                ak += 1
                secret[i] = "S"
                guess[i] = "G"
        sa = set(secret)
        sg = set(guess)
        two = sa & sg
        bk = 0
        for _ in two:
            bk += min(secret.count(_), guess.count(_))
        return str(ak)+"A"+str(bk)+"B"
        
        