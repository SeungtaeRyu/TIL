max = 1000000

count = [0]*(max + 1)
answer_route = c = [[0]]

count[1] = 0
answer_route.append([1])
count[2] = 1
answer_route.append([1])
answer_route[2].append(2)
count[3] = 1
answer_route.append([1])
answer_route[3].append(3)

for i in range(4, max+1):
    case = [max, max, max]

    if i % 2 == 0:
        case[0] = count[i//2] + 1
    if i % 3 == 0:
        case[1] = count[i//3] + 1
    case[2] = count[i-1] + 1

    if case[0] <= case[1] and case[0] <= case[2]:
        count[i] = case[0]
        answer_route.append(answer_route[i//2][:])
        answer_route[i].append(i)
    elif case[1] <= case[0] and case[1] <= case[2]:
        count[i] = case[1]
        answer_route.append(answer_route[i//3][:])
        answer_route[i].append(i)
    else: 
        count[i] = case[2]
        answer_route.append(answer_route[i-1][:])
        answer_route[i].append(i)

number = int(input())
answer_route[number].sort(reverse=True)
route_to_string = ' '.join(map(str, answer_route[number]))

print(count[number])
print(route_to_string)
