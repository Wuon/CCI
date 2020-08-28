"""
Given a string s and an integer k.

Return the maximum number of vowel letters in any substring of s with length k.

Vowel letters in English are (a, e, i, o, u).

Example 1:

Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.

Example 2:

Input: s = "aeiou", k = 2
Output: 2
Explanation: Any substring of length 2 contains 2 vowels.
"""

"""
1. use queue
2. append elements one by one, if they are vowel then increase count.
3. If the queue lengeth exceeds k, poll the next node and if its a vowel decrease
4. keep track of max
"""

from collections import deque
def maxVowel(s, k):
    q = deque()
    vowels = {'a', 'e', 'i', 'o', 'u'}
    numberVowels = 0
    result = -1
    for char in s:
        if len(q) >= k:
            cur = q.popleft()
            if cur in vowels:
                numberVowels -= 1
        if char in vowels:
            numberVowels += 1
            result = max(result, numberVowels)
        q.append(char)
    return result

print(maxVowel("abciiidef", 3))
print(maxVowel("leetcode", 2))
