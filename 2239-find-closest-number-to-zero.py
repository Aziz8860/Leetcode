def findClosestNumber(nums: list[int]) -> int:
    closest = float("inf")
    for num in nums:
        if abs(num) < abs(closest):
            closest = num
        elif abs(num) == abs(closest) and num > 0:
            closest = num
    return closest
