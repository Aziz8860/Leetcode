def maxProduct(nums: list[int]) -> int:
    res = max(nums) # handling if nums is single value
    current_min, current_max = 1, 1

    for n in nums:
        temp = current_max * n
        current_max = max(n * current_max, n * current_min, n) # 6 , -2
        current_min = min(temp, n * current_min, n) # 3, -12
        res = max(res, current_max)
    return res
