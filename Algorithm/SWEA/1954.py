import sys
sys.stdin = open("input1954.txt")

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = [[0 for _ in range(n)] for _ in range(n)]     # n * n 행렬만큼 배열 초기화

    move_count = []                                     # 움직여야할 횟수 저장
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    m = n
    for i in range(1, 2*n):                         # move_count = [n, n-1, n-1, n-2, n-2, ... , 1, 1] 이 들어감
        if not i % 2:
            m -= 1
        move_count.append(m)

    direction_index = 0
    x, y = 0, -1
    num = 0
    for i in range(len(move_count)):                # move_count 리스트의 길이만큼 반복문 동작
        for j in range(move_count[i]):              # move_count[i] value 만큼 현재 direction_index 방향으로 이동
            x += directions[direction_index][0]
            y += directions[direction_index][1]
            num += 1                                # 두번째 포문이 한 번 돌때마다 num += 1
            arr[x][y] = num                         # 다음 위치에 num 을 할당
        direction_index = (direction_index + 1) % 4     # move_count[i]의 value 만큼 이동 하면 direction 방향 이동

    print(f'#{tc}')
    for i in range(n):
        for j in range(n):
            print(arr[i][j], end=" ")
        print("")