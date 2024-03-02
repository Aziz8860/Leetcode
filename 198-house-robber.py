def rob(nums: list[int]) -> int:
    rob1, rob2 = 0, 0

    # [rob1, rob2, n, n+1, ...]
    for n in nums:
        temp = max(n + rob1, rob2)
        rob1 = rob2
        rob2 = temp
    return rob2

rob([1,2,3,1]) # output 4
rob([2,7,9,3,1]) # output 12