class Solution:
    def countCharacters(self, words: 'List[str]', chars: str) -> int:
        s = 0
        d = {}
        for char in chars:
            if char in d:
                d[char] += 1
            else:
                d[char] = 1
        for word in words:
            for c in word:
                if c not in d or word.count(c) > d[c]:
                    break
            else:
                s += len(word)
        return s
