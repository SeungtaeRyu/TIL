import sys
sys.stdin = open("input1210.txt")

for tc in range(1, 11):
    _ = input()
    arr = [list(map(int, input().split())) for _ in range(100)]

    d_index = 2         # 0이 상, 1이 좌, 2가 우

    cx = 99

    for i in range(100):
        if arr[99][i] == 2:
            cy = i
            break

    while True:
        if d_index == 0:                    # 올라가는중에
            if cy == 99:                        # 가로 인덱스가 오른쪽 끝이면
                if arr[cx][cy-1] == 1:              # 왼쪽이 1일때 왼쪽으로 감
                    d_index = 1
                    cy -= 1
                else:                               # 왼쪽이 1이 아니면 위로 올라감
                    cx -= 1
            elif cy == 0:                       # 가로 인덱스가 왼쪽 끝이면
                if arr[cx][cy+1] == 1:              # 오른쪽이 1일때 오른쪽으로 감
                    d_index = 2
                    cy += 1
                else:                               # 오른쪽이 1이 아니면 위로 올라감
                    cx -= 1
            else:                               # 가로 인덱스가 오른쪽, 왼쪽 끝도 아닐 때
                if arr[cx][cy-1] == 1:              # 왼쪽이 1이면 왼쪽으로 감
                    d_index = 1
                    cy -= 1
                elif arr[cx][cy+1] == 1:            # 오른쪽이 1이면 오른쪽으로 감
                    d_index = 2
                    cy += 1
                else:                               # 왼쪽, 오른쪽 둘다 1이 아니면 아니면 위로 올라감
                    cx -= 1

        elif d_index == 1:                  # 왼쪽으로 가는 중에
            if cy == 0:                         # 맵에 막히면 위로 올라감
                d_index = 0
                cx -= 1
            elif arr[cx][cy-1] == 1:            # 왼쪽이 계속 1이면 왼쪽으로 감
                cy -= 1
            else:                               # 벽에 막히면 위로 올라감
                d_index = 0
                cx -= 1

        elif d_index == 2:                  # 오른쪽으로 가는 중에
            if cy == 99:                        # 맵에 막히면 위로 올라감
                d_index = 0
                cx -= 1
            elif arr[cx][cy+1] == 1:            # 오른쪽이 계속 1이면 오른쪽으로 감
                cy += 1
            else:
                d_index = 0                     # 벽에 막히면 위로 올라감
                cx -= 1

        if cx == 0:
            print(f'#{tc} {cy}')
            break