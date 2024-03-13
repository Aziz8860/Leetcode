def canJump(nums: list[int]) -> bool:
    # time complexity for brute force with cache is O(n^2)
    # greedy is O(n) by shifting goal location until first element of array
    goal = len(nums) - 1
    
    for i in range(len(nums) - 1, -1, -1):
        print("current index", i)
        if i + nums[i] >= goal:
            goal = i
            print("goal changed to", goal)
    
    return goal == 0 # equal to: return True if goal == 0 else False

canJump([2,3,1,1,4])
# canJump([3,2,1,0,4])
