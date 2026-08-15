from collections import defaultdict
import heapq

class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = []
        heapq.heapify(self.tweets)

        self.follows = defaultdict(set) 

    def postTweet(self, userId: int, tweetId: int) -> None:
        heapq.heappush(self.tweets, (-self.time, tweetId, userId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        users = [userId] + list(self.follows[userId])
        ans = []
        temp = self.tweets.copy()
    
        while temp and len(ans) < 10:
            tweet = heapq.heappop(temp)
            if tweet[2] in users:
                ans.append(tweet[1])    
        
        return ans

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].discard(followeeId)
        
