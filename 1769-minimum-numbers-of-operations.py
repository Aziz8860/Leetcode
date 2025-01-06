def minOperations(boxes: str) -> list[int]:
    res = [0] * len(boxes)

    balls, moves = 0, 0
    for i in range(len(boxes)):
        res[i] = balls + moves
        moves = moves + balls
        balls += int(boxes[i])
    
    balls, moves = 0, 0
    for i in reversed(range(len(boxes))):
        res[i] += balls + moves
        moves = moves + balls
        balls += int(boxes[i])

    return res