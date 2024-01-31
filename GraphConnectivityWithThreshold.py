def areConnected(n: int, threshold: int, queries: list[list[int]]) -> list[bool]:
    if threshold < 1:
        return [True] * len(queries)

    answers = [False] * len(queries)

    divisors = {1: set()}

    for x in range(1, n + 1):  # number
        for y in range(2, n + 1):  # common divisor
            if x % y == 0 and y > threshold:
                divisors.setdefault(x, set()).add(y)
            else:
                divisors.setdefault(x, set())

    print(queries)
    print(threshold)
    print("Divisors: ", divisors)

    for query in range(len(queries)):
        a = divisors[queries[query][0]]
        b = divisors[queries[query][1]]

        print("query: ", queries[query])

        if len(a.intersection(b)) > 0:
            print("intersection found: ", a.intersection(b))
            answers[query] = True

    return answers


areConnected(9, 1, [[6, 8], [6, 9], [8, 9]])
