def climbStairs(n: int) -> int:
    # gambar tree, leaf kiri menggambarkan 1 step, leaf kanan menggambarkan 2 steps
    
    one, two = 1, 1

    for i in range(n - 1):
        temp = one
        one = one + two
        two = temp

    print(one)
    return one
