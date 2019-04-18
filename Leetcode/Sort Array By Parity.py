class Solution:
    def sortArrayByParity(self, A: 'List[int]') -> 'List[int]':
        even = []
        odd = []
        for number in A:
            if number % 2 == 0:
                even.append(number)
            else:
                odd.append(number)
        return even + odd
