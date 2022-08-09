import sys
sys.stdin = open("input4835.txt")

tc = int(input())
for T in range(1, tc+1):
    n, m = map(int, input().split())
    numbers = list(map(int, input().split()))

    sum_list = [0] * (n-m+1)
    sum_list[0] = sum(numbers[:m])  # 슬라이싱을 통해 첫 합계를 구함

    for i in range(1, n-m+1):       # n-m 만큼 반복문을 동작
        sum_list[i] = sum_list[i-1] - numbers[i-1] + numbers[i+m-1]     # 두번째 합계부터는 이전합계 - 이전합계마지막원소 + 다음에 추가할 원소

    print(f'#{T} {max(sum_list) - min(sum_list)}')  # sum_list의 최대 - 최소를 출력
