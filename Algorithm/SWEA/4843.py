import sys
sys.stdin = open("input4843.txt")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    answer = []
    for i in range(1, N+1):
        if i % 2:                               # 홀수 항이면
            answer.append(max(numbers))         # 결과 리스트에 최대값을 저장하고
            numbers.remove(max(numbers))        # 숫자 리스트에서 최대값을 삭제
        else:                                   # 짝수 항이면
            answer.append(min(numbers))         # 결과 리스트에 최소값을 저장하고
            numbers.remove(min(numbers))        # 숫자 리스트에서 최소값을 삭제
        if i == 10:
            break
    print(f"#{tc} {' '.join(list(map(str, answer)))}")