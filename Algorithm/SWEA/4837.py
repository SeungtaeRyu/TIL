# import sys
# sys.stdin = open("input4837.txt")
#
# T = int(input())
# for tc in range(1, T+1):
#     n, k = map(int, input().split())
#
#     numbers = []
#     answer = []
#     for i in range(1, n+1):
#         numbers.append(i)
#
#     for i in range(1, 1<<n):
#         total = 0
#         for j in range(n):
#             if i & (1 << j):
#                 total += numbers[j]
#         if total == k:
#             answer.append('+')
#     print(f'#{tc} {len(answer)}')