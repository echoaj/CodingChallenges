

def routePairs(mtd, frl, rrl):
    best = []
    lowestDiff = 100000
    for forward in frl:
        for retrn in rrl:
            dist = forward[1] + retrn[1]
            if dist <= mtd:
                diff = mtd - dist
                if len(best) == 0:
                    best.append([forward[0], retrn[0]])
                elif diff < lowestDiff:
                    lowestDiff = diff
                    best[0][0] = forward[0]
                    best[0][1] = retrn[0]
                lowestDiff = min(lowestDiff, diff)
                print(lowestDiff)
    return best

maxTravelDist = 10000
forwardRouteList = [[1, 3000], [2, 5000], [3, 7000], [4, 10000]]
returnRoutList = [[1, 2000], [2, 3000], [3, 4000], [4, 5000]]

print(routePairs(maxTravelDist, forwardRouteList, returnRoutList))