def containsDuplicate(nums: list[int]) -> bool:
    
    dict = {}

    for i in range(len(nums)):
        dict[nums[i]] = i

    print(dict)

    if len(nums) != len(dict):
        print('true')
        return True
    else:
        print('false')
        return False
    

    '''
    # neetcode version
    hashset = set()
        
    for n in nums:
        if n in hashset:
            return True
        hashset.add(n)
    return False
    '''
        
containsDuplicate([2,14,18,22, 22])