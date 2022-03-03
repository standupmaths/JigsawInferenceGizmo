# JIG code from Stand-up Maths video "Why don't Jigsaw Puzzles have the correct number of pieces?"
def hasBetterRatio(ratio, gridRatio, currentBest):
    return abs(currentBest / ratio - 1) < abs(gridRatio / ratio - 1)


def lowFactors(n):
    # all the factors which are the lower half of each factor pair
    return [j for j in range(1, int(n ** 0.5) + 1) if n % j == 0]


def bestSolution(ratio, value):
    currentBest = 0
    idealSides = []
    for factor in lowFactors(value):
        wholeNumRatio = int(value / factor)  # must be a whole number anyway
        currentRatio = wholeNumRatio / factor
        if currentBest == 0:
            currentBest = currentRatio
            idealSides = [factor, wholeNumRatio]
        else:
            if abs(currentRatio / ratio - 1) < abs(currentBest / ratio - 1):
                currentBest = currentRatio
                idealSides = [factor, wholeNumRatio]
    return currentBest, idealSides


def getBestSolutionForRange(debugMode, numPieces, penalty, ratio, valueRange, opinion):
    gridRatio = 0
    idealNSides = []
    bestNumPieces = 0
    best = 100
    bestDeets = []
    for value in valueRange:
        currentBest, idealSides = bestSolution(ratio, value)

        if bestNumPieces == 0 or (hasBetterRatio(ratio, gridRatio, currentBest)):
            bestNumPieces = value
            gridRatio = currentBest
            idealNSides = idealSides
            pieceRatio = calcRatio(ratio, currentBest)
            badnessScore = (penalty ** (abs(value - numPieces))) * pieceRatio

            if badnessScore < best:
                best = badnessScore
                bestDeets = [bestNumPieces, idealNSides, gridRatio]
            print(
                f"{bestNumPieces} pieces in {idealNSides} (grid ratio {round(gridRatio, 4)}) needs piece ratio "
                f"{round(pieceRatio, 4)}"
            )
            if debugMode is True:
                print(f"[badness = {round(badnessScore, 5)}]")

    if opinion is True:
        print(f"for {numPieces} the best is {bestNumPieces} pieces with size {idealNSides}", end='\n\n')

    return best, bestDeets


def calcRatio(numA, numB):
    return max(numA, numB) / min(numA, numB)


def jig(width, height, numPieces, opinion=False, debugMode=False):
    # percentage we'll check in either direction
    threshold = 0.1

    penalty = 1.005

    maxCap = int((1 + threshold) * numPieces)
    minCap = int((1 - threshold) * numPieces)

    ratio = calcRatio(width, height)

    print("")
    print(f"{width} by {height} is picture ratio {round(ratio, 4)}", end='\n\n')
    print(f"Looking for >= {numPieces} solutions:", end='\n\n')

    upRange = list(range(numPieces, maxCap + 1))
    upBest, upBestDeets = getBestSolutionForRange(
        debugMode, numPieces, penalty,
        ratio, upRange, opinion
    )

    print("Just out of interest, here are smaller options:", end='\n\n')

    downRange = list(range(minCap, numPieces))  # do not want n included again
    downRange.reverse()

    downBest, downBestDeets = getBestSolutionForRange(
        debugMode, numPieces, penalty,
        ratio, downRange, opinion
    )

    if opinion is True:
        print(f"If I had to guess: I think it's {upBestDeets[0]} pieces.")
        if downBest < upBest:
            print("")
            print(f"BUT, fun fact, {downBestDeets[0]} would be even better.", end='\n\n')

    return 'DONE'


if __name__ == '__main__':
    print(jig(33, 22.8, 1000, opinion=True))
