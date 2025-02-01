def isArraySpecial(nums: list[int]) -> bool:
    for i in range(1, len(nums)):
        if (nums[i] + nums[i-1]) % 2 == 0: # jika jumlahnya odd berarti aman
            return False

    return True