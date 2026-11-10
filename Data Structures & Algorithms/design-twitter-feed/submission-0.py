from collections import defaultdict
class Twitter:

    def __init__(self):
        self.time = 0
        self.tweet_map = defaultdict(list)
        self.follow_map = defaultdict(set)
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweet_map[userId].append([self.time,tweetId])
        self.time -=1

    def getNewsFeed(self, userId: int) -> List[int]:
        res= []
        min_heap=[]

        self.follow_map[userId].add(userId)

        for followeeId in self.follow_map[userId]:
            if followeeId in self.tweet_map:
                index = len(self.tweet_map[followeeId])-1
                tweet_time, tweetId  = self.tweet_map[followeeId][index]
                min_heap.append([tweet_time,tweetId,followeeId,index-1])
            
        heapq.heapify(min_heap)
        while min_heap and len(res) < 10:
            tweet_time, tweetId, followeeId, index = heapq.heappop(min_heap)
            res.append(tweetId)
            
            if index >= 0:
                tweet_time, tweetId = self.tweet_map[followeeId][index]
                heapq.heappush(min_heap, [tweet_time, tweetId, followeeId, index - 1])
        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        self.follow_map[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follow_map[followerId]:
            self.follow_map[followerId].remove(followeeId)
