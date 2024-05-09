def fib(self, n: int) -> int:
    # # Recursive backtracking
    # if n == 1:
    #     return 1
    # if n == 0:
    #     return 0
    # return self.fib(n - 1) + self.fib(n - 2)

    # ADVANCE
    ans = [0, 1]
    
    for i in range(2, n + 1):
        ans.append(ans[i - 1] + ans[i - 2])

    return ans[n]