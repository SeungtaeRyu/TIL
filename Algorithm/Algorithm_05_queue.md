## ✨큐

### 특성

- 스택과 마찬가지로 삽입과 삭제의 위치가 제한적인 자료구조
- 큐의 뒤에서 삽입만 하고, 큐의 앞에서는 삭제만 이루어 지는 구조
- 선입선출구조(FIFO, *first in fist out*)

### 연산

- createQueue() : 공백 상태의 큐를 생성하는 연산

  ```python
  Q = [] or Q = [0]*1000
  ```

- enQueue(item) : 큐의 뒤쪽에 원소를 삽입하는 연산

  ```python
  rear += 1
  Q[rear] = A
  rear += 1
  Q[rear] = B
  
  def enQueue(item):
  		global rear
  		if isFull() : print("Queue_Full")     # 디버깅
  		else:
  				rear <- rear + 1;
  				Q[rear] <- item;
  ```

- deQueue() : 큐의 앞쪽에서 원소를 삭제하고 반환하는 연산

  - front 값을 하나 증가시켜 큐에 남아있게 될 첫 번째 원소 이동
  - 새로운 첫 번째 원소를 리턴 함으로써 삭제와 동일한 기능함

  ```python
  deQueue()
  		global front
  		if(isEmpty()) then Queue_Empty(); # 디버깅 용
  		else{
  				front <- fron + 1;
  				return Q[front]
  		}
  ```

- isEmpty() : 큐가 공백상태인지를 확인하는 연산

  ```python
  def isEmpty():
  		return front == rear
  ```

- isFull() : 큐가 포화상태인지를 확인하는 연산

  ```python
  def Full():
  		return rear == len(Q) -1
  ```

- Queek() : 큐의 앞쪽에서 삭제없이 반환하는 연산

  ```python
  def Qpeek():
  		if isEmpty() : print("Queue_Empty")
  		else: return Q[front+1]
  ```

### ✨선형큐

```python
N = 3
q = [0] * N
front = -1
rear = -1
q[rear] = 10
rear += 1
q[rear] = 20
rear += 1
q[rear] = 30

front += 1
print(q[front])
front += 1
print(q[front])
front += 1
print(q[front]) # 10 20 30 rear == front
```

- 1차원 배열을 이용한 큐

  - 큐의 크기 = 배열의 크기
  - front = 저장된 첫 번째 원소의 인덱스
  - rear = 저장된 마지막 원소의 인덱스

- 상태

  - 초기 상태  : fron = rear = -1
  - 공백 상태 : front == rear
  - 포화 상태 : rear == n-1

- 문제점

  - 잘못된 포화상태 인식

    :앞에 공간이 있는 경우에도 꽉찼다고 인식

    - 해결 : 매 연산이 이루어 질 때 마다 저장된 원소들을 배열의 앞으로 이동 → 효율성 급감
    - 해결 : 원형 큐의 논리적 구조

- 큐를 클래스로 만든경우

```python
class Queue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * (size)
        self.front = 0
        self.rear = 0

    def isfull(self):
        return (self.rear + 1) % self.size == self.front

    def isempty(self):
        return self.rear == self.front

    def enqueue(self, item):
        if self.isfull():
            print("Queue is full")                     # 이거 없으면 que 사이즈 지정개수만큼 가능
        else:
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = item

    def dequeue(self):
        if self.isempty():
            print("Queue is empty")
        else:
            self.front = (self.front + 1) % self.size
            return self.queue[self.front]
```

### ✨원형큐

```python
N = 3
q = [0] * N
front = 0
rear = 0
rear = (rear + 1) % N
q[rear] = 10
rear = (rear + 1) % N
q[rear] = 20
rear = (rear + 1) % N
q[rear] = 30

front = (front + 1) % N
print(q[front])
front = (front + 1) % N
print(q[front])
front = (front + 1) % N
print(q[front]) # 10 20 30 rear == front
front = (front + 1) % N
print(q[front]) # 40 20 30 삭제된다.
# pop append 사용하면 크기가 클때 속도가 느려진다.
from collections import deque
q = deque()
q.append(10)
q.append(20)
q.append(3)
print(q.popleft())
print(q.popleft())
print(q.popleft()) # 10 20 30
```

: 일정 크기 이상 지난 경우 과거 데이터가 필요 없을 때 사용한다.

- 초기 공백 상태

  - front = rear = 0

- index의 순환

  - front와 rear의 위치가 배열의 마지막 인덱스인 n-1를 가르킨 후, 그 다음에는 논리적 순환을 이루어 배열의 처음 인덱스인 0으로 이동해야 함

  - 이를 위해 나머지 연산자 mod를 사용함

    |        | 삽입 위치               | 삭제 위치                 |
    | ------ | ----------------------- | ------------------------- |
    | 선형큐 | rear = rear + 1         | front = front + 1         |
    | 원형큐 | rear = (raer + 1) mod n | front = (front + 1) mod n |

- 공백상태 → 선형 큐와 일치

- 

- 

- Full상태 →  보통 큐의 크기를 정해 놓고 푼다.

  ```python
  # rear + 1== front
  def isFull():
  		return (rear + 1) % len(cQ) == front
  ```

- 삽입(enQueue(item))

  - 마지막 원소 뒤에 새로운 원소를 삽입하기 위해
    1. rear값을 조정하여 새로운 원소를 삽입할 자리를 마련함
    2. 그 인덱스에 해당하는 배열원소 cQ[rear]에 item을 저장

- 삭제(deQueue(), delete())

  - 가장 앞에 있는 원소를 삭제하기 위해
    1. front 값을 조정하여 삭제할 자리를 준비
    2. 새로운 front 원소를 리턴함으로써 삭제와 동일한 기능한다.

### ✨우선순위 큐

- 특성
  - 우선순위를 가진 항목들을 저장하는 큐
  - FIFO 순서가 아니라 우선순위가 높은 순서대로 먼저 나가게 된다.
- 적용 분야
  - 시뮬레이션 시스템
  - 네트워크 트래픽 제어
  - 운영체제의 테스크 스케줄링

1. 배열을 이용해서 구현

   - 문제점

     삽입이나 삭제 연산이 일어날 때 원소의 재배치가 발생 → 이에 소요되는 시간이나 메모리 낭비가 크다.

2. 리스트를 이용해서 구현

### 🎈큐 응용 (마이쮸)

```python
# 마이쮸 받고 줄서기 새로운 사람 한명이 뒤에 줄서기 반복
p = 1 # 처음 줄 설 사람의 번호
m = 0 # 나눠준 개수
v = 0
N = 1000 # 마이쮸 개수

while m < N :
		q.append((p,1,0)) # 처음 줄 서는 사람
		v, c, my = q.pop(0)
		print(f'큐에 있는 사람 수 {len(q)+1}, 받아갈 사탕 수{c}, 나눠준 사탕 수{m}')
		m += c
		q.append((v,c+1,my+c))
		p += 1
print(f'마지막 받은 사람 : {v}')
```

### ✨버퍼(buffer)

- 의미
  - 데이터를 한곳에서 다른 한 곳으로 전송하는 동안 일시적으로 그 데이터를 보관하는 메모리의 영역
  - 버퍼링 : 버퍼를 활용하는 방식 또는 버퍼를 채우는 동작을 의미한다.
  - 크기의 제약이 있다.
- 자료 구조
  - 일반적으로 입출력 및 네트워크 관련된 기능에서 이용
  - 순서대로 입력/출력/전달 되어야 하므로 FIFO방식의 자료구조인 큐가 활용된다.

## 👓검색

### ✨BFS

------

인접한 정점들에 대해 탐색 한 후, 차례로 다시 너비 우선 탐색을 진행해야하므로, 선입선출 형태의 자료구조 큐 사용

- 초기상태
  1. visited 배열 초기화
  2. Q생성
  3. 시작점 enqueue
- 입력 파라미터

```python
# 찾아간 곳 가지 순서대로 번호 입력
def BFS(G,v,n)                               # 그래프 G ,  탐색 시작점 v
		visited = [0] * (n+1)
		queue = []
		queue.append(v)
		visited[v] = 1
		while queue:
				t = queue.pop(0)
				visit(t)
				for i in G[t]:
						if not visited[i]:
								queue.append(i)
								visited[i] = visited[n] + 1
# 들리는 순서
def bfs(v, N):                                # v 시작정점, N 마지막 정점
		visited = [0] * (N + 1)
		q = []                                    # 큐 생성
		q.append(v)                               # 시작점 인큐
		visited[v] = 1                            # 시작점 처리 표시
		while q:
				v = q.pop(0)
				print(v)                              # visit(v)
				for w in adjList[v]:                  # 인접하고 미방문한 lst가 있으면
						if visited[w] == 0:
								q.append(w)
								visited[w] = visited[v] + 1
V, E = map(int,input().split())
N = V +1
adjList = [[] for _ in range(N)]
for _ in range(E):
		a, b = map(int,input().split())
		adjList[a].append(b)
def bfs(v,N,t) # v 시작, N 마지막 정점번호, t 찾는 정점
		visited = [0] * (N+1)
		q = []
		q = []                                    # 큐 생성
		q.append(v)                               # 시작점 인큐
		visited[v] = 1                            # 시작점 처리 표시
		while q:
				v = q.pop(0)
				if v == t:                            # visit(v)
						return 1                          # 목표 발견 visited[99] 넣으면 99번째 찾음
				for w in adjList[v]:                  # v에 인접하고 방문안한 w 인큐, 표시 w:                     
						if visited[w] == 0:
								q.append(w)
								visited[w] = visitied[v] + 1
		return 0
V, E = map(int,input().split())
N = V +1
adjList = [[] for _ in range(N)]
for _ in range(E):
		a, b = map(int,input().split())
		adjList[a].append(b)
```

### 큐 응용(미로)

```python
# 미로에서 목표 찾기
def bfs(v,N,t) # v 시작, N 마지막 정점번호, t 찾는 정점
		visited = [0] * (N+1)
		q = []                                    # 큐 생성
		q.append(v)                               # 시작점 인큐
		visited[v] = 1                            # 시작점 처리 표시
		while q:
				v = q.pop(0)
				if v == t:                            # visit(v)
						return 1                          # 목표 발견 visited[99] 넣으면 99번째 찾음
				for w in adjList[v]:                  # v에 인접하고 방문안한 w 인큐, 표시 w:                     
						if visited[w] == 0:
								q.append(w)
								visited[w] = visitied[v] + 1
		return 0
V, E = map(int,input().split())
N = V +1
adjList = [[] for _ in range(N)]
for _ in range(E):
		a, b = map(int,input().split())
		adjList[a].append(b) 
# 미로 경로의 수 세기
def bfs(i,j,N):
		visited = [[0]*N for _ in range(N)]
		q = []
		q.append((i,j))
		visited[i][j] = 1
		while q:
				i, j = q.pop(0)
				if maze[i][j] == 3:    # 3을 만나면 만약 3을 못 만난다면?
						answer += 1        # 경로 수를 측정하기 위해
						return 1
				else:
						visited[i][j] = 1
						for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
								ni, nj = i + di, j + dj
								if maze[ni][nj] !=1 and visited[ni][nj] == 0: # 벽으로 둘러쌓인 미로
										dfs(ni,nj,N)
						visited[i][j] = 0   # 반환할 때 0으로 돌리기 
						return

	
T = int(input())
for tc in range(1,T+1):
		N = int(input())
		maze = [list(map(int,input())) for _ in range(N)]
		sti = -1
		stj = -1
		for i in range(N):
				for j in range(N):
						if maze[i][j] == 2:
								sti, stj = i, j
								break
				if sti != -1:
						break
						
	print(f'#{tc} {bfs(sti,stj,N}')
		# 검사간 순서대로 길에 기록이 남는다.
```

- 최단 경로 / 최단거리
- 문제점 : 다중 경로를 체크할 때 경로가 겹치는 경우 visited때문에 갈수 없어서 체크가 안된다. 그렇다고 visited를 지우면 무한 루프에 빠질 수 있다. → 리턴할 때 방문체크를 없애기!

```python
# 미로 경로 목표치 
def bfs(i,j,N):
		visited = [[0]*N for _ in range(N)]
		q = []
		q.append((i,j))
		visited[i][j] = 1
		while q:
				i, j = q.pop(0)
				if maze[i][j] == 3:    # 3을 만나면 만약 3을 못 만난다면?
						answer += 1        # 경로 수를 측정하기 위해
						return 1
				else:
						visited[i][j] = 1
						for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
								ni, nj = i + di, j + dj
								if maze[ni][nj] !=1 and visited[ni][nj] == 0: # 벽으로 둘러쌓인 미로
										dfs(ni,nj,N)
						visited[i][j] = 0   # 반환할 때 0으로 돌리기 
						return

	
T = int(input())
for tc in range(1,T+1):
		N = int(input())
		maze = [list(map(int,input())) for _ in range(N)]
		sti = -1
		stj = -1
		for i in range(N):
				for j in range(N):
						if maze[i][j] == 2:
								sti, stj = i, j
								break
				if sti != -1:
						break
						
	print(f'#{tc} {bfs(sti,stj,N}')
		# 검사간 순서대로 길에 기록이 남는다.
# 미로 최단거리 찾기
def dfs(i,j,s,N):
		global minV
		if maze[i][j] == 3:
				if minV > s+1:
						minV = s +1
				return
		else:
				visited[i][j] = 1
				for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
						ni,nj = i + di, j + dj
						if maze[ni][nj] != 1 and visited[ni][nj] == 0:
								dfs(ni,nj,s+1,N)
				visited[i][j] = 0
				return
T = int(input())
for tc in range(1,T+1):
		N = int(input())
		maze = [list(map(int,input())) for _ in range(N)]
		dfs(sci,scj,0,N)
		if minV == N*N:
				minV = -1
		print(f'#{tc} {minV}')
```

🎈공부의 흐름 DFS → BFS  → 트리 순회 → 그래프 DFS, BFs → MST → 위상정렬 찾아보기

| 탐색                |          |
| ------------------- | -------- |
| 빠짐없이, 중복 없이 | DFS/ BFS |
| 최단거리            | DFS/BFS  |
| 경로의 수           | DFS      |
| 확산(출발이 여러곳) | BFS      |