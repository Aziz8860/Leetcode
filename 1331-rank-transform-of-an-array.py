def arrayRankTransform(arr: list[int]) -> list[int]:
    sortedArr = sorted(arr)
    rank_map = {} # hashmap

    rank = 1
    for num in sortedArr:
        if num not in rank_map:
            rank_map[num] = rank
            rank += 1
    
    rank = [rank_map[num] for num in arr]
    return rank

    # versi short: rank_map = {val: idx + 1 for idx, val in enumerate(sortedArr)}

# arrayRankTransform([40,10,20,30])
# arrayRankTransform([100,100,100])