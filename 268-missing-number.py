def missingNumber(nums: list[int]) -> int:
    # // cara sendiri //
    ex_sum = 0
    real_sum = 0

    for i in range(len(nums)):
        real_sum += nums[i]
        ex_sum += i

    ex_sum += len(nums) # bagaimana pun pasti ada angka yg hilang
    res = ex_sum - real_sum
    return res 

    # // punya orang di leetcode //
    # nums.sort()
    # for i in range(len(nums)):
    #     if nums[i] != i:
    #         return i
    # return len(nums)

    # // cara neetcode //
    # res = len(nums)
    # for i in range(len(nums)):
    #   res += (i - nums[i])
    # return res
