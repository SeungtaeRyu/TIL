n = int(input())
a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))

a_list.sort()

total = 0
for i in range(n):
    total += a_list[i] * b_list.pop(b_list.index(max(b_list)))
print(total)