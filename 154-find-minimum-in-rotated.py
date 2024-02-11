def findMin(nums: list[int]) -> int:
    left, right = 0, len(nums) - 1

    while left < right:
        mid = (left + right) // 2
        
        if nums[mid] > nums[right]:
            # minimum must be in the right half
            left = mid + 1
        elif nums[mid] < nums[right]:
            # Minimum could be at mid or in the left half
            right = mid
        else:
            # arr[mid] == arr[right], hard to say, but right can be reduced
            right -= 1

    print(nums[left])
    return nums[left]

# findMin([2,2,2,0,1])
findMin([10,1,10,10,10])
# findMin([3,4,5,1,2])
# findMin([9,9,8,7,6])