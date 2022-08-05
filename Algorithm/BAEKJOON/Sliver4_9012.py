T = int(input())

for test_case in range(T):
    ps = list(input())
    vps = []
    for p in ps:
        if p == '(':
            vps.append(p)
        else:
            if len(vps) == 0:
                vps.append(1)
                break
            else:
                vps.pop()
    
    if len(vps):
        print("NO")
    else:
        print("YES")