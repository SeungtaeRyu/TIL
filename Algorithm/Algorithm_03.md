# 4. 스택1

## 목차 

- 스택

- 재귀호출

- memoization

- DP

- DFS

<br>

## 1. 스택

### 스택의 특성

- 물건을 쌓아 올리듯 자료를 쌓아 올린 형태의 자료구조
- 스택에 저장된 자료는 선형 구조를 갖는다
  - 선형구조 : 자료 간의 관계가 1:1의 관계를 갖는다
  - 비선형구조 : 자료 간의 관계가 1:N의 관계를 갖는다 (예 : 트리)
- 스택에 자료를 삽입하거나 스택에서 자료를 꺼낼 수 있다
- 마지막에 삽입한 자료를 가장 먼저 꺼냈다. 후입선출이라고 한다
  - 예를 들어 스택에 1,2,3 순으로 자료를 삽입한 후 꺼내면 3,2,1 순으로 꺼낼 수 있다



### 스택을 프로그램에서 구현하기 위해 필요한 자료구조와 연산

- 자료구조 : 자료를 선형으로 저장할 저장소
  - 배열을 사용할 수 있다
  - 저장소 자체를 스택이라 부르기도 한다
  - 스택에서 마지막 삽인된 원소의 위치를 top`(stack pointer : sp)`이라 부른다
- 연산
  - 삽입 : 저장소에 자료를 저장한다. 보통 push라고 부른다
  - 삭제 : 저장소에서 자료를 꺼낸다. 보통 pop이라고 부른다
  - 스택이 공백인지 아닌지를 확인하는 연산 .isEmpty
  - 스택의 top에 있는 item(원소)을 반환하는 연산. peek

- 스택 구현 고려 사항
  - 1차원 배열을 사용하여 구현할 경우 구현이 용이하다는 장점이 있지만 스택의 크기를 변경하기가 어렵다는 단점이 있다.
  - 이를 해결하기 위한 방법으로 저장소를 동적으로 할당하여 스택을 구현하는 방법이 있다. 동적 연결리스트를 이용하여 구현하는 방법을 의미한다. 구현이 복잡하다는 단점이 있지만 메모리를 효율적으로 사용한다는 장점을 가진다. 스택의 동적 구현은 생략



## 2. 재귀호출

### 재귀호출이란?

- 자기 자신을 호출하여 순환 수행되는 것
- 함수에서 실행해야 하는 작업의 특성에 따라 일반적인 호출방식보다 재귀호출방식을 사용하여 함수를 만들면 프로그램의 크기를 줄이고 간단하게 작성가능



## 3. Memoization

### 메모이제이션이란?

- 재귀 함수로 구현한 알고리즘은 엄청난 중복 호출이 존재할 때 문제점이 있다.

- 메모이제이션은 컴퓨터 프로그램을 실행할 때 이전에 계산한 값을 메모리에 저장해서 매번 다시 계산하지 않도록 하여 전체적인 실행속도를 빠르게 하는 기술, 동적 계획법의 핵심이 되는 기술이다.

- 'memoization'은 글자 그대로 해석하면 메모리에 넣기(to put in memory) 라는 의미이며 기억되어야 할 것 이라는 뜻의 라틴어 memorandum에서 파생되었다. 흔히 기억하기, 암기하기 등의 memorization과 혼동하지만 정확한 단어는 memoization이다. 동사형은 memoize이다.

- Memoization 방법을 적용한 알고리즘

  ``` python
  # memo를 위한 배열을 할당하과, 모두 0으로 초기화한다
  # memo[0]을 0으로 memo[1]을 1로 초기화한다
  
  def fibo1(n):
      global memo
      if n >= 2 and len(memo) <= n:
          memo.append(fibo(n-1)) + fibo1(n-2))
      return memo[n]
  
  memo = [0, 1]
  ```

  

## 4. DP

### DP(Dynamic Programming)이란?

- 동적 계획 알고리즘은 그리디 알고리즘과 같이 최적화 문제를 해결하는 알고리즘이다.
- 동적 계획 알고리즘은 먼저 입력 크기가 작은 부분 문제들을 모두 해결한 후에 그 해들을 이용하여 보다 큰 크기의 부분 문제들을 해결하여, 최종적으로 원래 주어진 입력의 문제를 해결하는 알고리즘이다



## 5. DFS

### DFS(깊이우선탐색) 이란?

- 비선형구조인 그래프 구조는 그래프로 표현된 모든 자료를 빠짐없이 검색하는 것이 중요함

- 두 가지 방법

  - 깊이 우선 탐색(Depth First Search, DFS)
  - 너비 우선 탐색(Breadth First Search, BFS)

- 시작 정점의 한 방향으로 갈 수 있는 경로가 있는 곳까지 깊이 탐색해 가다가 더 이상 갈 곳이 없게 되면, 가장 마지막에 만났던 갈림길 간선이 있는 정점으로 되돌아와서 다른 방향의 정점으로 탐색을 계속 반복하여 결국 모든 정점을 방문하는 순회방법

- 가장 마지막에 만났던 갈림길의 정점으로 되돌아가서 다시 깊이 우선 탐색을 반복해야 하므로 후입선출 구조의 스택 사용

  ``` python
  visited = []
  stack = []
  def DFS(v):
      visited[v] = True
      while True:
          if (v의 인접 정점 중 방문 안한 정점 w가 있으면):
              stack.append(w)
              visited[v] = True;
          else:
              if stack: #(스택이 비어있지 않으면)
                  v = stack.pop()
              else:
                  break
  
  DFS(v)   
  ```

  