def xorAllNums(nums1: list[int], nums2: list[int]) -> int:
    # Brute force: n^2
    # res = 0
    # for n1 in nums1:
    #     for n2 in nums2:
    #         res ^= n1 ^ n2
    # return res

    '''
    Three useful properties of XOR:

    1. a XOR b = b XOR a
    2. a XOR a = 0
    3. a XOR 0 = a
    '''

    res = 0

    if len(nums2) % 2 == 1:
        for n in nums1:
            res ^= n
    if len(nums1) % 2 == 1:
        for n in nums2:
            res ^= n
            
    return res