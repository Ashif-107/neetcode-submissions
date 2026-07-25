class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)

        maxHeap = [-count for count in freq.values()]
        heapq.heapify(maxHeap)

        cooldown = deque()

        time = 0

        while maxHeap or cooldown:
            time += 1

            if maxHeap:
                cnt = heapq.heappop(maxHeap) + 1
                if cnt != 0:
                    cooldown.append((time + n, cnt))

            if cooldown and cooldown[0][0] == time:
                _, cnt = cooldown.popleft()
                heapq.heappush(maxHeap, cnt)

        return time

