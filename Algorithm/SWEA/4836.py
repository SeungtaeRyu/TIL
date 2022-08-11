import sys
sys.stdin = open("input4836.txt")

T = int(input())
for tc in range(1, T+1):
    arr = [[0 for _ in range(10)] for _ in range(10)]
    n = int(input())

    for _ in range(n):
        start_row, start_col, end_row, end_col, color = map(int, input().split())
        for i in range(start_row, end_row+1):
            for j in range(start_col, end_col+1):
                if arr[i][j] == color:  # 같은 곳에 같은색으로 칠하지 않음
                    continue
                else:                   # 처음 칠하면 ok
                    arr[i][j] += color

    count = 0
    for i in range(10):
        for j in range(10):
            if arr[i][j] >= 3:          # 1이나 2가 둘다 칠해진곳은 배열의 value가 3이상일 것임
                count += 1

    print(f'#{tc} {count}')