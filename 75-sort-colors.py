def sortColors(nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        maps = {0: 0, 1: 0, 2: 0}
        for x in nums:
            maps[x] = maps.get(x, 0) + 1
       
        index = 0
        for color in range(3):
            for _ in range(maps[color]):
                nums[index] = color
                index += 1