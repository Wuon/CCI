class Solution:
    def groupAnagrams(self, strs: 'List[str]') -> 'List[List[str]]':
        d = {}
        for word in strs:
            k = ''.join(sorted(word))
            if k in d:
                d[k].append(word)
            else:
                d[k] = [word]
        return list(d.values())
