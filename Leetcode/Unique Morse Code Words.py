class Solution:
    def uniqueMorseRepresentations(self, words: 'List[str]') -> 'int':
        store = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        o = []
        for word in words:
            s = ""
            for char in word:
                s += store[ord(char) - 97]
            o.append(s)
        return len(list(set(o)))
