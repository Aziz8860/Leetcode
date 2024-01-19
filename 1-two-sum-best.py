class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        dict = {}

        for i in range(len(nums)):
            temp = target - nums[i]
            if temp in dict:
                return [dict[temp], i]
                
                
            # If not, add the current element and its index to the seen dictionary
            dict[nums[i]] = i

