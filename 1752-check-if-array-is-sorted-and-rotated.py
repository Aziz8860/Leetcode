def check(nums: list[int]) -> bool:
    # optimum solution
    N = len(nums)
    count = 1

    # sliding window
    for i in range(1, 2 * N):
        if nums[(i - 1) % N] <= nums[i % N]:
            count += 1
        else:
            count = 1
        if count == N:
            return True
        
    return N == 1 # check if len is one, else return false

    # sorted_arr = sorted(nums) 

    # for i in range(len(nums)):
    #     rotated = nums[i:] + nums[:i]  # Manually rotate the array
    #     if rotated == sorted_arr:
    #         return True
    
    # return False

    # deque
    # sorted_arr = sorted(nums)

    #     my_deque = deque(nums)

    #     for _ in range(len(nums)):  # Rotate up to n times
    #         if list(my_deque) == sorted_arr: 
    #             return True
    #         my_deque.rotate(-1)  # Left rotate by 1
        
    #     return False

    