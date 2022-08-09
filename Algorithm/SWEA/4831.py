import sys
sys.stdin = open("input4831.txt")

tc = int(input())
for T in range(1, tc+1):
    k, n, m = map(int, input().split())
    charger = list(map(int, input().split()))

    ischarger = [False] * (n+1)     # 정류장의 갯수만큼 리스트 길이 할당하고 False를 저장
    for i in charger:               # 충전기가 있는 정류장에
        ischarger[i] = True         # True 를 할당

    current = 0
    next_ = 0
    stop_count = 0
    while True:
        current = next_             # 현재 위치 = 다음 위치로 이동
        if current + k >= n:                # 현재 위치 + 최대 이동 거리가 도착지보다 크면
            print(f'#{T} {stop_count}')     # 정답 출력 후 break!
            break
                                                # 현재 위치 + 최대 이동 거리가 도착지보다 작을 때 아래 코드 실행
        for i in range(current+k, current, -1): # 최대 이동거리에서부터 한 정류장씩 뒤로 오면서
            if ischarger[i]:                    # 충전기가 있는지를 확인
                next_ = i                       # 충전기가 있으면 다음 정류장으로 확정하고
                stop_count += 1                 # 충전 횟수를 +1 하고
                break                           # break

        if next_ == current:                # 위의 for 문을 돌고난 후 다음 정류장이 현재 정류장과 같으면 충전기가 없다는 소리
            print(f'#{T} 0')                # 노답을 출력하고 break!
            break
