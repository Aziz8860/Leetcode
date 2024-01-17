class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = 0

        index = 0
        for char in a[::-1]:
            res += int(char)*(2**index)
            index += 1

        index = 0
        for char in b[::-1]:
            res += int(char)*(2**index)
            index += 1
        
        # Convert the sum to binary
        binary_res = ""
        while res > 0:
            binary_res = binary_res + str(res % 2)
            res //= 2

        return binary_res[::-1] if binary_res != "" else "0"
            
