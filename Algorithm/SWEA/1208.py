import sys
sys.stdin = open("input1208.txt")

for T in range(1, 11):
    dump = int(input())
    floor_list = list(map(int, input().split()))

    for _ in range(dump):                                       # dump의 수만큼 반복
        floor_list[floor_list.index(max(floor_list))] -= 1      # max를 찾고, max의 index를 찾고, 그 index value에 -1을 함
        floor_list[floor_list.index(min(floor_list))] += 1      # min을 찾고, min의 index를 찾고, 그 index value에 +1을 함

    print(f'#{T} {max(floor_list)-min(floor_list)}')            # max-min을 함


