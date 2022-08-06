n, r, c = map(int, input().split())

def z_func(n, r, c):
    a = 4**(n-1)
    addnumber = [[0, a],[a*2, a*3]]

    quadrant = [0, 0]
    b = 2 ** (n-1)

    if r >= b :
        r -= b
        quadrant[0] += 1

    if c >= b :
        c -= b
        quadrant[1] += 1

    if n == 1:
        return addnumber[quadrant[0]][quadrant[1]]
    else:
        n -= 1
        return z_func(n,r,c) + addnumber[quadrant[0]][quadrant[1]]

print(z_func(n,r,c))