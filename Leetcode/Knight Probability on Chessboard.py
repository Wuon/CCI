class Solution:
    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        currentLayer = {
            (r, c): 1
        }
        for _ in range(K):
            newLayer = {}
            for coordinate in currentLayer:
                self.addToLayer(
                    coordinate[0] + 2, coordinate[1] - 1, N, newLayer, currentLayer[coordinate])
                self.addToLayer(
                    coordinate[0] + 2, coordinate[1] + 1, N, newLayer, currentLayer[coordinate])
                self.addToLayer(
                    coordinate[0] - 2, coordinate[1] - 1, N, newLayer, currentLayer[coordinate])
                self.addToLayer(
                    coordinate[0] - 2, coordinate[1] + 1, N, newLayer, currentLayer[coordinate])
                self.addToLayer(
                    coordinate[0] + 1, coordinate[1] - 2, N, newLayer, currentLayer[coordinate])
                self.addToLayer(
                    coordinate[0] + 1, coordinate[1] + 2, N, newLayer, currentLayer[coordinate])
                self.addToLayer(
                    coordinate[0] - 1, coordinate[1] - 2, N, newLayer, currentLayer[coordinate])
                self.addToLayer(
                    coordinate[0] - 1, coordinate[1] + 2, N, newLayer, currentLayer[coordinate])
            currentLayer = newLayer
        return sum(currentLayer.values())/(8**K)

    def addToLayer(self, r, c, N, newLayer, val):
        if 0 <= r < N and 0 <= c < N:
            if (r, c) in newLayer:
                newLayer[(r, c)] += val
            else:
                newLayer[(r, c)] = val
