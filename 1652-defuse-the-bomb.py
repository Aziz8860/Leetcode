def decrypt(code: list[int], k: int) -> list[int]:
    # modding method
        N = len(code)
        res = [0] * N

        for i in range(N):
            if k > 0:
                for j in range(i + 1, i + 1 + k):
                    res[i] += code[j % N]
            elif k < 0:
                for j in range(i - 1, i - 1 - abs(k), -1):
                    res[i] += code[j % N]
        
        return res

        # another way
        # N = len(code)
        # res = [0] * N
        
        # l = 0
        # cur_sum = 0
        # for r in range(N + abs(k)):
        #     cur_sum += code[r % N]

        #     if r - l + 1 > abs(k):
        #         cur_sum -= code[l % N]
        #         l = (l + 1) % N

        #     if r - l + 1 == abs(k):
        #         if k > 0:
        #             res[(l - 1) % N] = cur_sum
        #         else k < 0:
        #             res[(r + 1) % N] = cur_sum
        # return res 
