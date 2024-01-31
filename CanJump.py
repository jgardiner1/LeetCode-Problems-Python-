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

    def canJump2(nums: list[int]) -> int:
        if len(nums) == 1:
            return 0
        if len(nums) == 2 or nums[0] >= len(nums) - 1:
            return 1

        index = 0
        totalJumps = 0

        reachedEnd = False
        while not reachedEnd:
            print("current Pos: {}".format(index))
            jumpRange = nums[index]

            # checks if we can reach the end at the current spot
            if index + jumpRange >= len(nums) - 1:
                return totalJumps + 1

            print("Current pos range: {}".format(jumpRange))
            choices = nums[index + 1 : index + jumpRange + 1]
            best = 0
            bestJump = choices[best]
            print("Choices: {}".format(choices))

            for x in range(1, len(choices)):
                if choices[x] >= bestJump:
                    best = x
                    bestJump = choices[x]

            print("Best choice: {} range at index {}".format(bestJump, best))

            totalJumps += 1
            index += best + 1
            print("Increased index position by: {}\n\n".format(best + 1))

            if index >= len(nums) - 1:
                reachedEnd = True

        return totalJumps


print("solved in : {}".format(Solution.canJump2([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 0])))
