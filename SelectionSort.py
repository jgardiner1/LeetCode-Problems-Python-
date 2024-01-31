import time
from numpy import random

start = time.perf_counter()
for j in range(1000):
    arr = random.randint(1000, size=(1000))
    sorted = 0

    for x in range(len(arr)):
        minimum = arr[sorted]
        minPos = sorted

        for y in range(sorted, len(arr)):
            if arr[y] < minimum:
                minimum = arr[y]
                minPos = y

        sorted += 1

        temp = arr[x]
        arr[x] = minimum
        arr[minPos] = temp

print(
    "Finished 1000 runs of sorting 100 int arrays in ascending order with selection sort. time: {}".format(
        time.perf_counter() - start
    )
)
