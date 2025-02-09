from collections import defaultdict

def countBadPairs(nums: list[int]) -> int:
    count = defaultdict(int)
    good_pairs = 0
    for i in range(len(nums)):
        diff = nums[i] - i
        good_pairs += count[diff]
        count[diff] += 1
    total_pairs = len(nums) * (len(nums) - 1) // 2
    return total_pairs - good_pairs

# Hitung total jumlah pasangan secara langsung.
# Gunakan hashmap (count[diff]) untuk menghitung good pairs.