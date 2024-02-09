# remove ngative prefix, jadi kalo nilai sub array nya negatif gausah dipake
# sliding window

def maxSubArray(nums: list[int]) -> int:
    # O(n)
    max_subarray = nums[0]
    current_sum = 0

    for n in nums:
        if current_sum < 0:
            current_sum = 0
        current_sum += n
        max_subarray = max(max_subarray, current_sum)
    return max_subarray
        
maxSubArray([-2,1,-3,4,-1,2,1,-5,4])