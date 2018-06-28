import collections

class Twitter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # self.news   = []
        # size = 10
        self.userposts      = collections.defaultdict(list)
        self.followlist     = collections.defaultdict(list)
        self.globalposts    = []

    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: void
        """
        self.userposts[userId].append(tweetId)
        self.globalposts.append(tweetId)
        
    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        follower = self.followlist[userId]

        news = self.userposts[userId][-10 :]
        for user in follower:
            news += self.userposts[user][-10:]
        newsset  = set(news)
        resix = []
        for new in newsset:
            resix.append(self.globalposts.index(new))
        latest10ix = sorted(resix, reverse = True)[:10]
        latest10 = map(lambda x: self.globalposts[x], latest10ix)
        return latest10

    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followeeId not in self.followlist[followerId]:
            self.followlist[followerId].append(followeeId)

    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followeeId in self.followlist[followerId]:
            self.followlist[followerId].remove(followeeId)



# class Twitter(object):

#     def __init__(self):
#         self.timer = itertools.count(step=-1)
#         self.tweets = collections.defaultdict(collections.deque)
#         self.followees = collections.defaultdict(set)

#     def postTweet(self, userId, tweetId):
#         self.tweets[userId].appendleft((next(self.timer), tweetId))

#     def getNewsFeed(self, userId):
#         tweets = heapq.merge(*(self.tweets[u] for u in self.followees[userId] | {userId}))
#         return [t for _, t in itertools.islice(tweets, 10)]

#     def follow(self, followerId, followeeId):
#         self.followees[followerId].add(followeeId)

#     def unfollow(self, followerId, followeeId):
#         self.followees[followerId].discard(followeeId)


# if __name__ == '__main__':

#     obj = Twitter()
#     obj.postTweet(1,5)
#     param_2 = obj.getNewsFeed(1)
#     obj.follow(followerId,followeeId)
#     # obj.unfollow(followerId,followeeId)
#     ["Twitter","postTweet","getNewsFeed","follow","postTweet","getNewsFeed","unfollow","getNewsFeed"]
#     [[],[1,5],[1],[1,2],[2,6],[1],[1,2],[1]]
