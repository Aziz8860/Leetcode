def countBits(n: int) -> list[int]:
    dp = [0] * (n + 1)
    offset = 1

    # idea: 1 + dp(n - offset)

    for i in range(1, n + 1):
        if offset * 2 == i:
            offset = i
        dp[i] = 1 + dp[i - offset]

    return dp


    