def maxArea(height: list[int]) -> int:
    l, r = 0, len(height) - 1
    max_val = 0

    while l < r:
        current_val = min(height[l], height[r]) * abs(l - r)
        max_val = max(current_val, max_val)
        
        if min(height[l], height[r]) == height[l]:
            l += 1
        else:
            r -= 1

    print(max_val)
    return max_val


