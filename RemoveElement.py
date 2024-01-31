import time

nums = [2]
val = 3

endIdx = len(nums) - 1
num = 0

start = time.perf_counter_ns()
for x in range(len(nums)):
    if x >= endIdx:
        if len(nums) == 1 and nums[0] != val:
            num = 1
        break

    if nums[x] == val:
        while nums[endIdx] == val:
            endIdx -= 1

        temp = nums[x]
        nums[x] = nums[endIdx]
        nums[endIdx] = temp

    num += 1

print("Finished in {}".format(time.perf_counter_ns() - start))
print(num)

start = time.perf_counter_ns()
for x in range(len(nums) - 1, -1, -1):
    if nums[x] == val:
        nums.pop(x)
print("Finished in {}".format(time.perf_counter_ns() - start))
