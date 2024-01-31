def minOperations() -> int:
    # we can add 1 if result is less than or equal to half its necessary result and we're not 1 away already
    # we can double if all elements will be equal to, still less than half or 1 away from their target
    totalOps = 0
    nums = [1, 5]
    arr = [0] * len(nums)

    while arr != nums:
        for index in range(len(arr)):
            print("New Iteration: ", arr)
            if arr[index] + 1 <= nums[index] / 2 and nums[index] - arr[index] != 1:
                print(f"Modifying index {index} by + 1")
                arr = modify(arr, 0, index)
                totalOps += 1
                print(arr)

            if canDouble(arr, nums):
                print(f"Eligible for double")
                arr = modify(arr, 1, 0)
                print(arr)

    return totalOps


def canDouble(arr, nums):
    canArray = [False] * len(arr)
    for x in range(len(arr)):
        if (
            arr[x] * 2 == nums[x]
            or arr[x] * 2 <= nums[x] / 2
            or arr[x] * 2 == nums[x] - 1
        ):
            canArray[x] = True

    return all(canArray)


def modify(arr, op, idx):
    if op == 0:
        arr[idx] += 1

    if op == 1:
        for number in arr:
            number *= 2

    return arr


print(minOperations())
