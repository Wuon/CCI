# [('calc1', 'calc2'), ('iti1', 'iti2'), ('calc2', 'csi1'), ('iti2', 'calc2'), ('iti2', 'ceg1'), ('ceg1', 'ceg2'), ('ceg2', 'csi1')]
# calc1 -> calc2 --------> csi1
#            ^                ^
#            |                |
#           iti2 -> ceg1 -> ceg2
#            |
#           iti1
# return [calc2, iti2, ceg1]

from collections import deque

def findMidway(original):
    start = set()
    end = set()
    edge = {}
    for pair in original:
        start.add(pair[0])
        end.add(pair[1])
        if pair[0] not in edge:
            edge[pair[0]] = []
        edge[pair[0]].append(pair[1])

    startingPoints = start.difference(end)

    output = []

    for startingPoint in startingPoints:
        queue = deque([([startingPoint], startingPoint)])
        while queue:
            curSequence, curPoint = queue.popleft()
            for nextPoint in edge[curPoint]:
                if nextPoint in edge:
                    news = curSequence.copy()
                    news.append(nextPoint)
                    queue.append([news, nextPoint])
                else:
                    output.append(curSequence[len(curSequence) // 2])
    return output


testCase1 = [('calc1', 'calc2'), ('iti1', 'iti2'), ('calc2', 'csi1'), ('iti2', 'calc2'), ('iti2', 'ceg1'), ('ceg1', 'ceg2'), ('ceg2', 'csi1')]

print(findMidway(testCase1))
