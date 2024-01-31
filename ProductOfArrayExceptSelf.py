"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]


Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
 

Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)
"""

# [1, 2, 3, 4, 5]
# [1, 5, 1, 10, 2]
# [100, 20, 100, 10, 50]
# [3, 6, 1, 4, 8]
# [192, 96, 576, 144, 72]
# [3, 5, 2, 5]
# [50, 30, 75, 30]

# duplicate numbers will have same value
# find smallest number not 0 and thats the largest total.
# if there is a 1 then the total 
import operator
from functools import reduce


class Solution:
    def productExceptSelf(nums: list[int]) -> list[int]:
        answers = [0] * len(nums)
        answered = [False] * len(nums)

        while not all(answered):
            for x in range(len(nums)):
                if answered[x] == True:
                    continue

                if x == 0:
                    print("at beginning. Calculating prod({})".format(nums[x + 1 :]))
                    answers[x] = reduce(operator.mul, nums[x + 1 :])
                elif x == len(nums) - 1:
                    print("at end. Calculating prod({})".format(nums[0:x]))
                    answers[x] = reduce(operator.mul, nums[0:x])
                else:
                    left = reduce(operator.mul, nums[0:x])
                    right = reduce(operator.mul, nums[x + 1 :])

                    answers[x] = left * right

                answered[x] = True

        return answers


nums = [1, 2, 3, 4]
print(Solution.productExceptSelf(nums=nums))
