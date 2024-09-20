def plusOne(digits: list[int]) -> list[int]:
    # Here, map(str, my_list) converts each element to a string, join() concatenates them,
    # and int() converts the resulting string to an integer.
    int_result = int(''.join(map(str, digits)))
    int_result += 1
    ans = [int(i) for i in str(int_result)]
    return ans

    # Neetcode
    # digits = digits[::-1]
    # one, i = 1, 0

    # while one:
    #     if i < len(digits):
    #         if digits[i] == 9:
    #             digits[i] = 0
    #         else:
    #             digits[i] += 1
    #             one = 0
    #     else:
    #         digits.append(1)
    #         one = 0
    #     i += 1
    # return digits[::-1]



plusOne([1,2,3]) # [1,2,4]
plusOne([4,3,2,1]) # [4,3,2,2]
plusOne([0]) # [1]