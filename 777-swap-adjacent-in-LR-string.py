def canTransform(start: str, end: str) -> bool:
    '''
    start  = "RXXLRXRXL"
                      s

              012345678
    end    = "XRLXXRRLX"
                      e
    '''
    l = len(start)
    s, e = 0, 0

    while True:
        while s < l and start[s] == 'X':  # remove 'X' from calculation
            s += 1
        while e < l and end[e] == 'X': # remove 'X' from calculation
            e += 1
        if s == l or e == l:
            # they both have to reach the end at the same time
            return s == l and e == l   
        # they still need to maintain the equality
        if start[s] != end[e]:
            return False
        # R will be on the right 'RX -> XR' 
        # so it should be on the end side and 
        # s should be smaller (to move forward)
        if start[s] == 'R' and s > e:
            return False
        # L will be on the left 'XL -> LX' 
        # so it should be on the start side and 
        # s should be larger (to move it back)
        if start[s] == 'L' and s < e:
            return False
        s += 1
        e += 1
        