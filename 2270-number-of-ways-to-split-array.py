def waysToSplitArray(nums: list[int]) -> int:
    prefix_sum = [0] * (len(nums) + 1)
    for i in range(len(nums)):
        prefix_sum[i + 1] = prefix_sum[i] + nums[i]

    # prefix_sum = [0, 10, 14, 6, 13]
    res = 0
    for i in range(len(nums) - 1): # stop before last element
        first_i = prefix_sum[i+1]
        last_i = prefix_sum[len(nums)] - prefix_sum[i+1]
        if first_i >= last_i:
            res += 1

    return res
        

