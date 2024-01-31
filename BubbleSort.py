import time

arr = [1, 6, 4, 3, 7, 8, 4, 3, 3, 5, 6, 345, 56, 234, 23, 4, 5, 5, 67, 64]

swapped = True
counter = 0
indexOfLastSorted = len(arr)

start = time.perf_counter_ns()


while swapped:
    swapped = False
    for i in range(1, indexOfLastSorted):
        left = arr[i - 1]
        right = arr[i]
        if left > right:
            # swap left to right
            arr[i] = left
            arr[i - 1] = right
            swapped = True
            counter += 1


end = time.perf_counter_ns()


print("swapped: ", arr, " in ", counter, " moves and ", end - start, " time")
