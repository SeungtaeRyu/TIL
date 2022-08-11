import sys
sys.stdin = open("input4839.txt")

T = int(input())
for tc in range(1, T+1):
    P, A, B = map(int, input().split())

    A_l = 1
    B_l = 1
    A_r = P
    B_r = P
    while True:
        A_c = int((A_l+A_r)/2)
        B_c = int((B_l+B_r)/2)

        if A == A_c and B == B_c:       # 동시에 값을 찾으면 0 출력
            print(f'#{tc} 0')
            break

        if A == A_c:                    # A가 값을 찾으면 브레이크
            print(f'#{tc} A')
            break
        elif A > A_c:                   # A가 찾는값이 중간값보다 크면 시작점을 중간값으로
            A_l = A_c
        else:                           # A가 찾는 값이 중간값보다 작으면 끝점을 중간값으로
            A_r = A_c

        if B == B_c:                    # B가 값을 찾으면 브레이크
            print(f'#{tc} B')
            break
        elif B > B_c:                   # B가 찾는값이 중간값보다 크면 시작점을 중간값으로
            B_l = B_c
        else:                           # B가 찾는 값이 중간값보다 작으면 끝점을 중간값으로
            B_r = B_c

