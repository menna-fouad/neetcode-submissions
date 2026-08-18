class Twitter:

    def __init__(self):
        self.tweets = defaultdict(list)
        self.following = defaultdict(set)
        self.count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append([self.count, tweetId])
        if len(self.tweets[userId]) > 10:
            self.tweets[userId].pop(0)
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        min_heap = []

        self.following[userId].add(userId)
        if len(self.following[userId]) > 10:
            max_heap = []
            for followeeId in self.following[userId]:
                if followeeId in self.tweets:
                    index = len(self.tweets[followeeId]) - 1
                    count, tweetId = self.tweets[followeeId][index]
                    heapq.heappush(max_heap, (-count, tweetId, followeeId, index - 1))
                    if len(max_heap) > 10:
                        heapq.heappop(max_heap)
            
            while max_heap:
                count, tweetId, followeeId, index = heapq.heappop(max_heap)
                heapq.heappush(min_heap, (-count, tweetId, followeeId, index))
        
        else:
            for followeeId in self.following[userId]:
                if followeeId in self.tweets:
                    index = len(self.tweets[followeeId]) - 1
                    count, tweetId = self.tweets[followeeId][index]
                    heapq.heappush(min_heap, (count, tweetId, followeeId, index - 1))
        
        while len(res) < 10 and min_heap:
            count, tweetId, followeeId, next_index = heapq.heappop(min_heap)
            res.append(tweetId)
            if next_index >= 0:
                count, tweetId = self.tweets[followeeId][next_index]
                heapq.heappush(min_heap, (count, tweetId, followeeId, next_index - 1))
        
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)
