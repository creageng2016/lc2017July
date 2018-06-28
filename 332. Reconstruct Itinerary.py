import collections

class Solution(object):
    def findItinerary(self, tickets):
    #     """
    #     :type tickets: List[List[str]]
    #     :rtype: List[str]
    #     """
        gr = collections.defaultdict(list)
        # for u, v in tickets:
        for u, v in tickets:
            gr[u].append(v)

        for u in gr:
            gr[u].sort()

        res = []
        air = "JFK"

        while air:
            res.append(air)
            if gr[air]:
                air = gr[air].pop(0)
            else:
                print gr
                return res

    # def findItinerary(self, tickets):
    #     targets = collections.defaultdict(list)
    #     for a, b in sorted(tickets)[::-1]:
    #         targets[a] += b,
    #     route = []
        
    #     def visit(airport):
    #         route.append(airport)
    #         while targets[airport]:
    #             visit(targets[airport].pop())

    #     visit('JFK')
    #     return route[::-1]


# def findItinerary(self, tickets):
#     targets = collections.defaultdict(list)
#     for a, b in sorted(tickets)[::-1]:
#         targets[a] += b,
#     route, stack = [], ['JFK']
#     while stack:
#         while targets[stack[-1]]:
#             stack += targets[stack[-1]].pop(),
#         route += stack.pop(),
#     return route[::-1]


if __name__ == '__main__':    
    # tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
    # tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
    tickets = [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]

    # ["JFK", "MUC", "LHR", "SFO", "SJC"]
    print Solution().findItinerary(tickets)        