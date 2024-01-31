def checkArithmeticSubarrays(nums: list[int], l: list[int], r: list[int]) -> list[bool]:
    finalTable = [False] * len(l)

    for idx in range(len(l)):
        subarray = nums[l[idx] : r[idx]]
        subarray.append(nums[r[idx]])
        subarray.sort()

        diff = subarray[1] - subarray[0]
        table = [False] * (r[idx] - l[idx])
        table[0] = True

        for num in range(1, len(subarray) - 1):
            if subarray[num + 1] - subarray[num] == diff:
                table[num] = True
            else:
                finalTable[idx] = False
                break

        if all(table):
            finalTable[idx] = True

    return finalTable


print(checkArithmeticSubarrays([4, 6, 5, 9, 3, 7], [0, 0, 2], [2, 3, 5]))
