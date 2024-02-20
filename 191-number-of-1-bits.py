def hammingWeight(n: int) -> int:
    res = 0
    while n:
        n &= (n - 1) # equal to n = n & (n - 1), operation ini untuk get rid of 1
        res += 1
    return res
    
    # time complexity ini O(1) artinya constant
    # while n: # equal to n > 0
    #     res += n % 2
    #     n = n >> 1
    # return res
