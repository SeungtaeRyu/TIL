# [입력]
# 첫째 줄에 N과 K가 빈 칸을 사이에 두고 순서대로 주어진다. (1 ≤ K ≤ N ≤ 5,000)
# 7 3

# [출력]
# 예제와 같이 요세푸스 순열을 출력한다.
# <3, 6, 2, 7, 5, 1, 4>

# 방법 1. 내 생각대로 풀기

# 인덱스로 접근하기 위해 오름차순 수열에 M-1번째 인덱스를 항상 추출해야 한다. ex) 수열 = 1234567, M=3일때 뽑아야 하는 수 3 = 수열[2]
# for 문이 한 번 동작할 때마다 오름차순 수열이 pop 되기 때문에 길이가 1씩 줄어든다.
# 길이가 1 줄어들기 때문에 다음에 추출할 숫자는 index = index + M 이 아니라 index = index + (M-1)을 해줘야 한다.
# index = index + (M-1)이 줄어들고 있는 오름차순 수열의 length 보다 크면 길이로 나눈 나머지로 저장한다.

N, M = map(int, input().split())

ase = list(range(1, N+1))
yp = []

index = M-1
for i in range(1, N+1):

    yp.append(ase[index])
    if i == N:
        break
    ase.pop(index)
    index = (index+M-1) % len(ase)

print('<' + ', '.join(list(map(str, yp))) + '>')


# 방법 2. 자료구조 큐를 사용하여 풀기 - First-In First-Out 선입선출

# 자료구조 큐를 의미하는 [1,2,3,4,5,6,7] 을 저장한다.
# M이 3일때 2번 앞에 있는 숫자를 뒤로 보낸다. [3,4,5,6,7,1,2]
# popleft()를 통해 3을 추출한다. [4,5,6,7,1,2]

# 다시 2번 앞에 있는 숫자를 뒤로 보낸다. [6,7,1,2,4,5]
# popleft()를 통해 6을 추출한다. [7,1,2,4,5]

# ...계속 반복한다. 
# 큐의 length가 M보다 작아지더라도 숫자를 한개씩 뒤로 보낸 후 결국 추출하는 숫자는 제일 왼쪽이기 때문에 문제가 되지 않음!


# from collections import deque

# N, M = map(int, input().split())

# d = deque(list(range(1,N+1)))
# yp = []

# for i in range(1, N+1):
#     for count in range(1, M+1):
#         if count == M:
#             yp.append(d.popleft())
#         else:
#             d.append(d.popleft())

# print('<' + ', '.join(list(map(str, yp))) + '>')
