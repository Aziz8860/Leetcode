class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        dict = {}

        for i in range(len(nums)):
            temp = target - nums[i]
            if temp in dict:
                return [dict[temp], i]
                
                
            # If not, add the current element and its index to the seen dictionary
            dict[nums[i]] = i

