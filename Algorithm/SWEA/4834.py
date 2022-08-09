import sys
sys.stdin = open("input4834.txt")

tc = int(input())
for T in range(1, tc+1):
    n = int(input())
    card = list(input())

    index_count = [0] * 10          # 0 ~ 9의 count 를 담을 리스트 길이 할당
    for num in card:                # 카드의 갯수만큼 반복문 동작
        index_count[int(num)] += 1  # 숫자 카드가 나오면 그 숫자를 index로 하는 value에 +1을 함

    enum_count_list = []
    for num, count in enumerate(index_count):   # number, count 를 가지는 list[enum]을 생성
        enum_count_list.append((count, num))

    enum_count_list.sort(reverse=True)          # enum 을 내림차순으로 2차원 정렬을 함.
    print(f'#{T} {enum_count_list[0][1]} {enum_count_list[0][0]}')  # 가장 앞에 있는 튜플을 출력