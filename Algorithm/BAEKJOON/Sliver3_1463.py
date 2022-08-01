max = 1000000

count = [0]*(max + 1)

count[1] = 0
count[2] = 1
count[3] = 1

for i in range(4, max+1):
    case = [max, max, max]

    # case 1
    if i % 2 == 0:
        case[0] = count[i//2] + 1
    
    # case 2
    if i % 3 == 0:
        case[1] = count[i//3] + 1
    
    # case 3
    case[2] = count[i-1] + 1

    # min(case1, case2, case3)
    count[i] = min(case)

number = int(input())
print(count[number])
