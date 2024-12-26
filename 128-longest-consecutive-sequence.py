def longestConsecutive(nums: list[int]) -> int:
    # Handle edge case where nums is empty
    if not nums: 
        return 0

    nums.sort()

    longest = 1
    current_streak = 1

    for i in range(1, len(nums)):
        if nums[i] == nums[i-1]:
            continue
        elif nums[i] == nums[i-1] + 1:
            # Consecutive number, increment the current streak
            current_streak += 1
        else:
            # Sequence breaks, update the longest streak and reset current streak
            longest = max(longest, current_streak)
            current_streak = 1
    
    return max(longest, current_streak)
