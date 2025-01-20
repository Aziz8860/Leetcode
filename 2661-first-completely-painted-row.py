def firstCompleteIndex(arr: list[int], mat: list[list[int]]) -> int:
    '''
    [
        [1,3,4,2],
        [2,4,5,6],
        [6,3,5,6],
    ]
    '''

    ROWS, COLS = len(mat), len(mat[0])

    mat_to_position = {} # n : (r, c)
    for r in range(ROWS):
        for c in range(COLS):
            mat_to_position[mat[r][c]] = (r, c)
    
    row_count = [0] * ROWS
    col_count = [0] * COLS
    for i in range(len(arr)):
        r, c = mat_to_position[arr[i]]
        row_count[r] += 1
        col_count[c] += 1

        if col_count[c] == ROWS or row_count[r] == COLS:
            return i
    