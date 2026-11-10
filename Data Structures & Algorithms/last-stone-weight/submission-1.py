class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        '''
        max_heap = [-s for s in stones]
        heapq.heapify(max_heap)

        while len(max_heap)>1:
            first = heapq.heappop(max_heap)
            second = heapq.heappop(max_heap)

            if first == second:
                continue
            elif first < second:
                heapq.heappush(max_heap,first - second)
        
        return abs(max_heap[0]) if len(max_heap)==1 else 0
        '''
        heapq.heapify_max(stones)
        while len(stones)>1:
            first = heapq.heappop_max(stones)
            second = heapq.heappop_max(stones)

            if first-second>0:
                heapq.heappush_max(stones, first-second)
        return stones[0] if len(stones)>0 else 0