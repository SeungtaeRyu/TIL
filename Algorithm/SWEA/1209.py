import sys
sys.stdin = open("input1209.txt")

for _ in range(10):
    T = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    sum_max = 0
    for i in range(100):                            # 행, 열의 합 구할 2중 for 문
        sum_row = 0
        sum_col = 0
        for j in range(100):
            sum_row += arr[i][j]
            sum_col += arr[j][i]
        sum_max = max(sum_max, sum_row, sum_col)

    sum_diagonal1 = 0
    sum_diagonal2 = 0
    for i in range(100):                            # 대각선을 구할 1중 for 문
        sum_diagonal1 += arr[i][i]
        sum_diagonal2 += arr[99-i][99-i]
    sum_max = max(sum_max, sum_diagonal1, sum_diagonal2)
    print(f'#{T} {sum_max}')