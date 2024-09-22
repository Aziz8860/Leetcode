def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # for i in range(m, m + n):
        #     nums1[i] = nums2[i - m]
        # nums1.sort()

        x, y = m-1, n-1

        for z in range(m + n - 1, -1, -1):
            if x < 0:
                nums1[z] = nums2[y]
                y -= 1
            elif y < 0:
                break
            elif nums1[x] > nums2[y]:
                nums1[z] = nums1[x]
                x -= 1
            else:
                nums1[z] = nums2[y]
                y -= 1

merge([1,2,3,0,0,0], 3, [2,5,6], 3)
merge([1], 1, [], 0)
merge([0], 0, [1], 1)