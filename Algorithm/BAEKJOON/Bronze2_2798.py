n, m = map(int, input().split())

numbers = list(map(int, input().split()))

answer = 0
for i in range(n): 
    for j in range(i+1, n):
        for k in range(j+1, n):
            sum = numbers[i] + numbers[j] + numbers[k]
            if sum > m:
                continue
            else:
                answer = max(answer, sum)

print(answer)