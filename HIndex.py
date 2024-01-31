class Solution:
    def hIndex(citations: list[int]) -> int:
        # First we order the values of f from the largest to the lowest value.
        # Then, we look for the last position in which f is greater than or equal to the position

        citations.sort(reverse=True)
        hIndex = 0
        for x in range(len(citations)):
            if citations[x] >= x + 1:
                hIndex = x + 1

        return hIndex


citations = [10, 8, 5, 4, 3]
print(Solution.hIndex(citations=citations))
