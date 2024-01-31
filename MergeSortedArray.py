class Solution:
    def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        nums1[:] = nums1[:m]

        j = 0

        while len(nums2) > 0:
            inserted = False
            for i in range(j, len(nums1)):
                if nums1[i] >= nums2[0]:
                    nums1.insert(i, nums2[0])
                    del nums2[0]
                    inserted = True
                    j = i
                    break


arr1 = [1, 3, 6, 7, 19, 23]
arr2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

m = len(arr1)
n = len(arr2)

print(arr1)

Solution.merge(arr1, m, arr2, n)

print(arr1)
