'''
You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].

Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:

0 <= j <= nums[i] and
i + j < n
Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].

 

Example 1:

Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [2,3,0,1,4]
Output: 2
 

Constraints:

1 <= nums.length <= 104
0 <= nums[i] <= 1000
It's guaranteed that you can reach nums[n - 1].
'''

class Solution:
    def jump(nums: list[int]) -> int:
        if len(nums) == 1:
            return 0
        if len(nums) == 2:
            return 1
        reached = False
        totalJumps = 0

        index = 0

        iteration = 1

        while not reached:
            jump = nums[index]
            if index + jump >= len(nums) - 1:
                reached = True

            choices = nums[index + 1 : index + 1 + jump]
            bestIdx = 0
            bestPotential = bestIdx + choices[0]

            for x in range(len(choices)):
                if x + choices[x] >= bestPotential:
                    bestIdx = x
                    bestPotential = x + choices[x]

            index += bestIdx + 1
            totalJumps += 1
            iteration += 1

        return totalJumps

nums = [2, 3, 0 , 1, 4]
print(Solution.jump(nums))