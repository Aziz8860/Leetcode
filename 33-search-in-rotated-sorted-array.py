def search(nums: list[int], target: int) -> int:
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        
        if nums[mid] >= nums[left]: # left side is sorted
            if nums[mid] > target >= nums[left]: # target is in the left half
                right = mid - 1
            else: # target is in the right half
                left = mid + 1
        else: # right side is sorted
            if nums[right] >= target > nums[mid]: # target is in the right half
                left = mid + 1
            else: # target is in the left half
                right = mid - 1

    return -1


# search([5,6,7,8,9,0,1,2,3], 0)
search([4,5,6,7,0,1,2], 3)
