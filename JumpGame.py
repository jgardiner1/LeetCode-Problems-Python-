'''
55. Jump Game
Solved
Medium
Topics
Companies
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

 

Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
 

Constraints:

1 <= nums.length <= 104
0 <= nums[i] <= 105
'''

class Solution:
    def canJump(nums: list[int]) -> bool:
        goalIndex = len(nums) - 1
        reachedStart = False

        while reachedStart == False:
            for x in range(goalIndex - 1, -1, -1):
                print("x + nums[x]: {} + {}".format(x, nums[x]))
                if x + nums[x] >= goalIndex:
                    print("{} attainable with {} + {}".format(goalIndex, x, nums[x]))
                    goalIndex = x
                    break

                if x == 0:
                    return False

            if goalIndex <= 0:
                reachedStart = True

        return reachedStart


print("solved in : {}".format(Solution.canJump([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 0])))
