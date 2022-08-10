from collections import deque

n, l, r = map(int, input().split())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

move_count = 0
q = deque([])

while True:                 # while문을 한 번 돌 때마다 인구이동을 한 번 한걸로 한다
    visited = [[False for _ in range(n)] for _ in range(n)]         # 방문기록 초기화
    ismoved = False                                                 # 인구 이동을 했을까?
    for i in range(n):                      # 2중 for문을 사용하여
        for j in range(n):                  # 모든 곳을 체크
            if not visited[i][j]:           # 방문하지 않은 곳이 있으면
                visited[i][j] = True        # 방문기록을 하고
                q.append((i, j))            # 큐에 그 곳 위치를 저장
            else:           # 방문 기록이 없는 곳이 있을때까지
                continue    # continue를 반복

            sumV = 0                    # 이동이 가능한 나라들의 인구 합계
            sumV += arr[i][j]

            share_list = []             # 이동이 가능한 나라들의 위치들 저장
            share_list.append((i, j))

            while q:    # 큐가 빌 때 까지 무한루프 돌려봅니다.
                cx = q[0][0]            # 큐의 가장 왼쪽 항목의 x, y 좌표를
                cy = q[0][1]            # 현재 위치로 저장

                directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
                for dx, dy in directions:
                    nx = cx + dx        # 현재 위치 기준 인접 4개의
                    ny = cy + dy        # 다음 위치 저장
                    if nx < 0 or nx >= n or ny < 0 or ny >= n:  # index가 맵을 벗어나면 패스
                        continue
                    if not visited[nx][ny] and l <= abs(arr[cx][cy] - arr[nx][ny]) <= r:    # 현재 위치 기준 인접 4개 중 조건을 만족하면
                        ismoved = True              # 인구이동이 일어났다고 확인
                        visited[nx][ny] = True      # 다음 지역 방문 체크
                        q.append((nx, ny))          # 다음 지역을 큐에 append
                        share_list.append((nx, ny)) # 인구를 공유하는 위치들 저장
                        sumV += arr[nx][ny]         # 인구 공유하는 위치의 인구 수 sum
                q.popleft()     # 큐의 왼쪽 항목의 인접4개 조사가 끝나면 제거

            avg = sumV // len(share_list)   # 큐의 모든 원소가 제거되면
            for x, y in share_list:         # 그동안 저장된 모든 지역에
                arr[x][y] = avg             # 인구수를 분배해줌

    if ismoved:
        move_count += 1
    else:
        print(move_count)
        break







