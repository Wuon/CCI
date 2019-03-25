class Solution:
    def firstBadVersion(self, n, m = 0):
        guess = (n + 1 + m) // 2
        if isBadVersion(guess):
            if not isBadVersion(guess-1):
                return guess
            return self.firstBadVersion(guess, m)
        return self.firstBadVersion(n, guess)
