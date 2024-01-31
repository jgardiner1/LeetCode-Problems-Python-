# def rotate(nums: list[int], k: int) -> None:
#     """
#     Do not return anything, modify nums in-place instead.
#     """
#     for x in range(k):
#         temp = nums.pop()
#         print(temp)
#         nums.insert(0, temp)


def rotate(nums: list[int], k: int) -> None:
    # any numbers target position can be calculated as
    # original index position + k - len(arr)
    # eg - [1, 2, 3, 4] k = 2
    # 4 - index pos 3
    # 3 + 2 - 4 = 1

    index = 0
    value = nums[index]

    visited = list()

    for x in range(len(nums)):
        targetIndex = index + k - len(nums)
        if targetIndex < 0:
            targetIndex += len(nums)
        print("target index: {}".format(targetIndex))
        replaced = nums[targetIndex]
        print("Replacing value: {}".format(replaced))
        nums[targetIndex] = value

        print("new array: {}".format(nums))

        index = targetIndex
        value = replaced


nums = [1, 2]
print("Before: {}".format(nums))
rotate(nums, 1)
print("After: {}".format(nums))
