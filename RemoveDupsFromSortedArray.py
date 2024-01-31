nums = [1, 1, 1, 2, 3, 4, 5, 6, 6, 6, 7, 7, 8]

# REMOVE DUPS FROM SORTED ARRAY WITH 2 ORIGINAL VALUES OF EACH IF POSSIBLE


# replace = 1
# for x in range(1, len(nums)):
#     if nums[x - 1] != nums[x]:
#         nums[replace] = nums[x]
#         replace += 1

# print(nums)
# print(replace)


# dups = 0

# for x in range(1, len(nums)):
#     # found duplicate
#     if nums[x] == nums[x - 1]:
#         # Stores original number. UNIQUE
#         original = nums[x - 1]
#         originalIdx = x - 1

#         dups += 1
#         print("adding unique: {}".format(original))

#         # Duplicate info
#         duplicateCount = 1
#         # Starting point for search to find total dups for this number
#         start = x + 1

#         while start <= len(nums) - 1 and nums[start] == original:
#             duplicateCount += 1
#             start += 1

#         # move whole array down
#         # copy everything after all duplicates
#         temp = nums[x + duplicateCount :]
#         # everything after original gets replaced with temp above
#         nums[x:duplicateCount] = temp
#         nums[x + len(temp) :] = [original] * duplicateCount


# print(nums)
# print("Num of unique numbers: {}".format(len(nums) - dups))
