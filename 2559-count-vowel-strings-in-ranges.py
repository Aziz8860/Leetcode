def vowelStrings(words: list[str], queries: list[list[int]]) -> list[int]:
        vowels = ['a', 'e', 'i', 'o', 'u']
        transformed = []
        res = []

        # make words to array of 0's and 1's
        for word in words:
            if len(word) == 1 and word in vowels:
                transformed.append(1)
            elif word[0] in vowels and word[-1] in vowels:
                transformed.append(1)
            else:
                transformed.append(0)
        
        # build prefix sum array
        prefix_sum = [0] * (len(transformed) + 1)
        for i in range(len(transformed)):
            prefix_sum[i + 1] = prefix_sum[i] + transformed[i]

        # Prefix sum array building step by step:
        # i=0: prefix_sum[1] = prefix_sum[0] + transformed[0] = 0 + 1 = 1
        # i=1: prefix_sum[2] = prefix_sum[1] + transformed[1] = 1 + 0 = 1
        # i=2: prefix_sum[3] = prefix_sum[2] + transformed[2] = 1 + 1 = 2
        # i=3: prefix_sum[4] = prefix_sum[3] + transformed[3] = 2 + 1 = 3
        # i=4: prefix_sum[5] = prefix_sum[4] + transformed[4] = 3 + 1 = 4

        # final transform  array:   [1,0,1,1,1]
        # Final prefix_sum array: [0,1,1,2,3,4]

        # Query processing:
        # Query [0,2]: prefix_sum[3] - prefix_sum[0] = 2 - 0 = 2
        # Query [1,4]: prefix_sum[5] - prefix_sum[1] = 4 - 1 = 3
        # Query [1,1]: prefix_sum[2] - prefix_sum[1] = 1 - 1 = 0

        # checking
        for query in queries:
            start = query[0]
            end = query[1] + 1 # add 1 to include the end index
            range_sum = prefix_sum[end] - prefix_sum[start]
            res.append(range_sum)

        return res