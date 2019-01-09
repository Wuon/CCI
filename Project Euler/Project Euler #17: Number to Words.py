words = {
    1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five',
    6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten',
    11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen',
    15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen',
    19: 'Nineteen', 20: 'Twenty', 30: 'Thirty', 40: 'Forty',
    50: 'Fifty', 60: 'Sixty', 70: 'Seventy', 80: 'Eighty',
    90: 'Ninety',
}


def hundred(n):
    word = []
    while n != 0:
        if n in words:
            word.append(words[n])
            n %= n
        else:
            if n // 100 != 0:
                word.append(words[n//100])
                word.append('Hundred')
                n %= 100
            if n in words:
                word.append(words[n])
                n %= n
            else:
                if n // 10 != 0:
                    word.append(words[n - n % 10])
                    n %= 10
    return word


for a0 in range(int(input().strip())):
    n = int(input().strip())
    sequence = ''
    if n > 999999999999:
        for word in hundred(n//1000000000000):
            sequence += ' ' + word
        sequence += ' Trillion'
        n %= 1000000000000
    if n > 999999999:
        for word in hundred(n//1000000000):
            sequence += ' ' + word
        sequence += ' Billion'
        n %= 1000000000
    if n > 999999:
        for word in hundred(n//1000000):
            sequence += ' ' + word
        sequence += ' Million'
        n %= 1000000
    if n > 999:
        for word in hundred(n//1000):
            sequence += ' ' + word
        sequence += ' Thousand'
        n %= 1000
    for word in hundred(n):
        sequence += ' ' + word
    print(sequence.strip())


