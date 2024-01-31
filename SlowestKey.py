def slowestKey(releaseTimes: list[int], keysPressed: str) -> str:
    longestTime = releaseTimes[0]
    keys = ""
    idxTime = 0

    for idx in range(0, len(releaseTimes)):
        if idx == 0:
            idxTime = releaseTimes[0]
        else:
            idxTime = releaseTimes[idx] - releaseTimes[idx - 1]

        if idxTime > longestTime:
            longestTime = releaseTimes[idx] - releaseTimes[idx - 1]
            keys = keysPressed[idx]
        elif idxTime == longestTime:
            keys += keysPressed[idx]

    return max(keys)


print(slowestKey(releaseTimes=[1, 2], keysPressed="ba"))
