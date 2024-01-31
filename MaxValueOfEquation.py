def findMaxValueOfEquation(points: list[list[int]], k: int) -> int:
    # find qualifying coords that satisfy |xi - xj| <= k

    maxSum = 0

    for i in points:
        for j in points:
            if i != j:
                constraint = abs(i[0] - j[0])
                print(
                    "checking if |{} - {}| satisfy. total: {}".format(
                        i[0], j[0], constraint
                    )
                )

                if constraint <= k:
                    print("{} and {} satisfy".format(i, j))
                    total = i[1] + j[1] + abs(i[0] - j[0])
                    print(total)
                    if total > maxSum:
                        print("updating max")
                        maxSum = total

    print(maxSum)
    return maxSum


points = [[-19, 9], [-15, -19], [-5, -8]]
k = 10

findMaxValueOfEquation(points, k)
