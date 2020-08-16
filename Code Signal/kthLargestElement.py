import heapq

def kthLargestElement(nums, k):
    inverted = []
    for num in nums:
        inverted.append(num * -1)
    heapq.heapify(inverted)
    for i in range(len(inverted)):
        cur = heapq.heappop(inverted)
        if i + 1 == k:
            return cur * -1
    return None
