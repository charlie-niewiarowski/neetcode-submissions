class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            s1, s2 = heapq.heappop(stones), (heapq.heappop(stones))
            print(s1, s2)
            if s1 < s2:
                heapq.heappush(stones, s1 - s2)
            
        if len(stones) == 0:
            return 0
        else:
            return abs(stones[0])
