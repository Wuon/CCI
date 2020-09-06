def formatLine(currentLine, l):
    if len(currentLine) == 1:
        return currentLine[0] + ' ' * (l - len(' '.join(currentLine)))
    whitespace = l - len(''.join(currentLine))
    i = 0
    while whitespace > 0:
        currentLine[i] += ' '
        whitespace -= 1
        i += 1
        if i == len(currentLine) - 1:
            i = 0
    return currentLine

def textJustification(words, l):
    output = []
    currentLine = []
    for word in words:
        currentLine.append(word)
        if len(' '.join(currentLine)) > l:
            nextLine = [currentLine.pop()]
            output.append(''.join(formatLine(currentLine, l)))
            currentLine = nextLine
    output.append(' '.join(currentLine) + ' ' * (l - len(' '.join(currentLine))))
    return output
