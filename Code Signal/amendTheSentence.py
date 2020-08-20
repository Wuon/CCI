def amendTheSentence(s):
    output = ''
    for char in s:
        if char.isupper():
            output += ' '
        output += char.lower()
    return output.strip()
