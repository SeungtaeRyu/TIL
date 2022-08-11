T = int(input())
for tc in range(1, T+1):
    n, k = map(int, input().split())

    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    answer = []

    for i in range(1, 1 << 12):
        total = 0                           # 합계 변수
        count = 0                           # 더한 원소 횟수 변수
        for j in range(12):
            if i & (1 << j):
                count += 1                  # 더한 원소 갯수 ++
                total += numbers[j]         # 합계 ++
        if total == k and count == n:       # 합계가 k 이면서 더한 원소가 n개 이면 결과 리스트에 +를 추가
            answer.append('+')
    print(f'#{tc} {len(answer)}')           # 결과 출력으로 +의 갯수를 출력한다.