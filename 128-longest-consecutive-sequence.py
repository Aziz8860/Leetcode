def longestConsecutive(nums: list[int]) -> int:
    # cannot use sort because O(n log n)
    numSet = set(nums)
    longest = 0

    for n in nums:
        # check if its the start of a sequence
        if (n - 1) not in numSet:
            length = 0
            while (n + length) in numSet:
                length += 1
            longest = max(length, longest)
    return longest
