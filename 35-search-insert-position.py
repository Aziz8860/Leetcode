def searchInsert(nums: list[int], target: int) -> int:
    low = 0
    high = len(nums) - 1
    mid = 0

    while low <= high:
        mid = (high + low) // 2

        # If target is greater, ignore left half
        if nums[mid] < target:
            low = mid + 1

        # If target is smaller, ignore right half
        elif nums[mid] > target:
            high = mid - 1

        # means target is present at mid
        else:
            return mid
    return low
