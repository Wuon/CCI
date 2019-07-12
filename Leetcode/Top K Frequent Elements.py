import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        result = []
        for num in nums:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1
        heap = [(-1 * freq, num) for num, freq in d.items()]
        heapq.heapify(heap)
        for i in range(k):
            result.append(heapq.heappop(heap)[1])
        return result
