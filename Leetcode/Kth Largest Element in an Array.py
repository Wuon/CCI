import heapq

class Solution:
    def findKthLargest(self, nums: 'List[int]', k: int) -> int:
        if k == 0:
            return -1
        d = {}
        pos = 0
        for num in nums:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1
        heap = [(num * -1, freq) for num, freq in d.items()]
        heapq.heapify(heap)
        while heap:
            cur = heapq.heappop(heap)
            if pos + (cur[1]) >= k:
                return cur[0] * -1
            pos += cur[1]
        return
