def generateParenthesis(n: int) -> list[str]:
    ans, sol = [], []

    def backtrack(openN, closedN):
        # also can be
        # if len(sol) == 2*n:
        if openN == closedN == n:
            ans.append("".join(sol))
            return

        if openN < n:
            sol.append("(")
            backtrack(openN + 1, closedN)
            sol.pop()

        if closedN < openN:
            sol.append(")")
            backtrack(openN, closedN + 1)
            sol.pop()

    backtrack(0, 0)
    return ans

    # Time: O(2^n)
    # Space: O(n)