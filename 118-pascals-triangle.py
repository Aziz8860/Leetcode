def generate(numRows: int) -> List[List[int]]:
    res = [[1]]

    for i in range(1, numRows): # mulai dari 1 karena baris pertama sudah ada, bisa juga (numRows - 1)
        temp = [0] + res[-1] + [0]
        row = []
        for j in range(len(res[-1]) + 1): # bisa juga range(len(temp) - 1)
            row.append(temp[j] + temp[j + 1])
        res.append(row)
    return res
        