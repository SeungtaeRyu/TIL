import sys
sys.stdin = open("input4828.txt")

tc = int(input())
for T in range(1, tc + 1):
    _ = int(input())                            # 쓰지 않는 입력
    numbers = list(map(int, input().split()))
    max_ = 0
    min_ = 1000000
    for num in numbers:                         # numbers 의 value 들로 for 문을 동작
        if max_ < num:                          # max 갱신
            max_ = num
        if min_ > num:                          # min 갱신
            min_ = num
    print(f'#{T} {max_ - min_}')