import heapq

class Solution(object):

    # def nthSuperUglyNumber(self, n, primes):
    #     uglies = []

    #     def gen(prime):
    #         for ugly in uglies:
    #             yield ugly * prime

    #     merged = heapq.merge(*map(gen, primes))
    #     uglies.append(1)

    #     while len(uglies) < n:
    #         _next = next(merged)

    #         if _next != uglies[-1]:
    #             uglies.append(_next)

    #     return uglies[-1] 

    def nthSuperUglyNumber(self, n, primes):
        i_list = [-1 for i in range(len(primes))]
        v_list = [1 for i in range(len(primes))]

        uglies = [0 for i in range(n)]

        k = 0
        while k < n:
            minv = min(v_list)
            uglies[k] = minv

            for i in range(len(v_list)):
                if v_list[i] == minv:
                    i_list[i] += 1
                    v_list[i] = uglies[i_list[i]] * primes[i]
            k += 1

        # print uglies
        return uglies[-1]

if __name__ == '__main__':

    n     = 12
    primes  = [2,7,13,19] 
    print Solution().nthSuperUglyNumber(n, primes)

    # def nthSuperUglyNumber(self, n, primes):
    #     urglies = [1]
    #     def gen(prime):
    #         for urg in urglies:
    #             yield urg * prime

    #     merged = heapq.merge(*map(gen, primes))

    #     while  len(urglies) < n:
    #         urgly = next(merged)
    #         if urgly != urglies[-1]:
    #             urglies.append(urgly)
    #     return urglies[-1]

    # def nthSuperUglyNumber2(self, n, primes):
    #     """
    #     :type n: int
    #     :type primes: List[int]
    #     :rtype: int
    #     """
    #     ugly = [1] * n
    #     i_list = [-1] * len(primes)
    #     v_list = [1] * len(primes)

    #     k = 0
    #     while k < n:
    #         x    = min(v_list)
    #         ugly[k] = x
    #         for i in xrange(len(v_list)):
    #             if x == v_list[i]:
    #                 i_list[i] += 1
    #                 v_list[i] = ugly[i_list[i]] * primes[i]
    #         k += 1

    #     return ugly[-1]
