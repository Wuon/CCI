class Solution:
    def heightChecker(self, heights: 'List[int]') -> int:
        sh = sorted(heights)
        count = 0
        for i in range(len(heights)):
            if heights[i] != sh[i]:
                count += 1
        return count
