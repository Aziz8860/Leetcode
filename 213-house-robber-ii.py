def rob(nums: list[int]) -> int:
    
    # Case 1: if only one element in the array -> nums[0]
    # Case 2: skipping first element
    # Case 3: skipping last element
    return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))


def helper(self, nums): # from house robber 1
    rob1, rob2 = 0, 0

    # [rob1, rob2, n, n+1, ...]
    for n in nums:
        newRob = max(rob1 + n, rob2)
        rob1 = rob2
        rob2 = newRob
    return rob2