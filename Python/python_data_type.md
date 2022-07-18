# Python Data Type

---



### 연산자 우선순위

- 기본적으로 수학에서 우선순위와 같음
- 괄호가 가장 먼저 계산되고 *, / 가 +, - 보다 먼저 계산된다



### 자료형 분류

#### 1. Numeric Type

- int (정수, integer)

  - 2진수(0b)
  - 8진수(0o)
  - 16진수(0x)

- Float (부동소수점, 실수, floating point number)

  - 실수 연산 시 주의할 점(부동소수점)

    ``` python
    print(3.2 - 3.1) # 0.1000000000009
    print(1.2 - 1.1) # 0.0999999999987
    
    # 해결책 1. 임의의 작은 수 활용
    print(abs(a - b) <= 1e-10) # True
    
    # 해결책 2. python 3.5이상
    import math
    print(math.inclose(a, b)) # True
    ```

- Complex (복소수, complex number)

  

#### 2. String Type

- 문자열은 작은따옴표(')나 큰따옴표(")를 활용하여 표기

  - 문자열을 묶을 때 동일한 문장부호를 활용
  - PEP8에서는 소스코드 내에서 하나의 문장부호를 선택하여 유지하도록 함

- 중첩 따옴표

  - 작은따옴표가 들어 있는 경우는 큰따옴표로 문자열 생성

  - 큰따옴표가 들어 있는 경우는 작은따옴표로 문자열 생성

    ``` python
    print("문자열 안에 '작은따옴표'를 사용하려면 큰따옴표로 묶는다")
    print('문자열 안에 "큰따옴표"를 사용하려면 큰따옴표로 묶는다')
    ```

  - 삼중따옴표

- Escape sequence

  - `\n` : 줄바꿈
  - `\t` : 탭
  - `\r` : 캐리지 리턴
  - `\0` : 널(Null)
  - `\\`  : \
  - `\'` : 단일인용부호(')
  - `\"` : 이중인용부호(")

- 문자열 연산

  - 덧셈

    ``` python
    print("Hello" + "World") # HelloWorld
    ```

  - 곱셈

    ``` python
    print("Python" * 3) #PythonPythonPython
    ```

- String Interpolation(문자열을 변수를 활용하여 만드는 법)

  - f-strings : python 3.6+

    ``` python
    name = 'Kim'
    score = 4.5
    
    print(f'Hello, {name}! 성적은 {score}')
    # Hello, Kim! 성적은 4.5
    
    import datetime
    today = datetime.datetime.now()
    print(today) # 2202-07-08 16:04:15.200411
    
    print(f'오늘은 {today:%y}년 {today:%m}월 {today:%d}일 ')
    # 오늘은 22년 07년 08일
    
    pi = 3.141592
    print(f'원주율은 {pi:.3}. 반지름이 2일 때 원의 넓이는 {pi*2*2}')
    # 원주율은 3.14. 반지름이 2일때 원의 넓이는 12.566368
    ```

    

#### 3. None

- 파이썬 자료형 중 하나

- 값이 없음을 표현하기 위해 None 타입이 존재

- 일반적으로 반환 값이 없는 함수에서 사용하기도 함

  

#### 4. Boolean Type

- 논리 자료형으로 참과 거짓을 표현하는 자료형

- True 또는 False를 값으로 가짐

- 비교 / 논리 연산에서 활용됨

  - 비교 연산자

    - `<` : 미만
    - `<=` :  이하
    - `>` : 초과
    - `>=` : 이상
    - `==` : 같다
    - `!=` : 다르다
    - `is` : 객체 아이덴티티(OOP)
    - `is not` : 객체 아이덴티티가 아닌 경우

    ``` python
    print(3 > 6) # False
    print(3.0 == 0) # True
    print(3 >= 0) # True
    print('3' != 3) # True
    print('Hi' == 'hi') # False
    ```

  - 논리 연산자

    - `A and B` : A와 B 모두 True시, True
    - `A or B` : A와 B 하나라도 True시, True
      - `Not` : True를 False로, False를 True로

    ``` python
    # 23시가 되었고, 잠이 오는 경우
    hour = 23
    status = 'sleepy'
    print(hour >= 22 and status == 'sleepy') # True
    
    # 23시가 되었지만, 잠이 안 오는 경우
    hour = 23
    stats = 'nice'
    print(hour >= 22 and status == 'sleepy') # False
    ```

    - `Falsy` : `False`는 아니지만 False로 취급 되는 다양한 값
      - `0`, `0.0`, `()`, `{}`, `[]`, `None`, `""`(빈 문자열)
      - `Falsy`가 아닌 모든 값들은 `True`이다
    - 우선순위 `not` > `and` > `or` 순

    ``` python
    print(not True) # False
    print(not 0) # True
    print(not 'hi') # False
    print(not True and False or not False) # True
    # 위와 같음
    print(((not True) and False) or (not False)) # True
    # and 는 1 * 0 = 0이라 곱하기
    # or는 1 + 0 = 1이라 더하기!
    ```

    - 논리 연산자의 단축 평가

      - 결과가 확실한 경우 두번쨰 값은 확인하지 않고 첫번째 값 반환
      - `and` 연산에서 첫번째 값이 `False`인 경우 무조건 `False` => 첫번째 값 반환
      - `or` 연산에서 첫번째 값이 `True`인 경우 무조건 `True` => 첫번째 값 반환
      - `0`은 `False`, `1`은 `True`

      ``` python
      print(3 and 5) # 5 단축 평가 x
      print(3 and 0) # 0 단축 평가 x
      print(0 and 3) # 0 단축 평가 o
      print(0 and 0) # 0 단축 평가 o
      
      print(5 or 3) # 5 단축 평가 o
      print(3 or 0) # 3 단축 평가 o
      print(0 or 3) # 3 단축 평가 x
      print(0 or 0) # 0 단축 평가 x
      ```



#### 5. 컨테이너

- 여러 개의 값(데이터)을 담을 수 있는 것(객체)으로, 서로 다른 자료형을 저장할 수 있음

  - 예시 : `List`

- 컨테이너의 분류

  - 순서가 있는 데이터(Ordered) vs. 순서가 없는 데이터(Unordered)

  - 순서가 있다 `!=` 정렬되어 있다

  - 시퀀스형

    - `List` (가변형) : 여러 개의 값을 `순서가 있는` 구조로 저장하고 싶을 때 사용

      - 리스트는 대괄호(`[]`) 혹은 `list()` 를 통해 생성

        ``` python
        my_list = []
        another_list = list()
        
        print(type(my_list)) # <class 'list'>
        print(type(another_list)) # <class 'list'>
        ```

      - 어떠한 자료형도 저장할 수 있으며, 리스트 안에 리스트도 넣을 수 있음

      - 생성된 이후 내용 변경이 가능 -> 가변 자료형

      - 값에 대한 접근은 `list[index]`

        ``` python
        location = ['서울', '대전', '구미', '광주', '부울경']
        print(location[0]) # 서울
        
        location[0] = '양양'
        print(location) # ['양양', '대전', '구미', '광주', '부울경']
        ```

    - `Tuple` (비가변형) : 여러 개의 값을 순서가 있는 구조로 저장하고 싶을 때

      - 리스트와의 차이점은 생성 후, 담고 있는 값 변경이 불가 => 불변 자료형

      - 항상 소괄호 형태로 사용

      - 소괄호(`()`) 혹은 `tuple()`을 통해 생성

      - 튜플은 수정 불가능한 시퀀스로 인덱스로 접근 가능

      - 값에 대한 접근은 `tuple[index]`

      - 튜플(Tuple) 생성 주의사항

        - 단일 항목의 경우 생성시 값 뒤에 쉼표를 붙여야 함 `tuple_a = (1,)`
        - 복수 항목의 경우 마지막 항목에 붙은 쉼표는 없어도 되지만, **넣는 것을 권장**
        - 튜플 대입(Tuple assignment)

        ``` python
        x, y = 1, 2
        print(x, y) # 1 2
        
        # 실제로 tuple로 처리
        x, y = (1, 2)
        print(x, y) # 1 2
        ```

      - `Range` (비가변형)

      - 숫자의 시퀀스를 나타내기 위해 사용

      - 주로 반복문과 함께 사용됨

        ``` python
        print(range(4)) # range(0, 4)
        
        print(list(range(4))) # [0, 1, 2, 3]
        
        print(type(range(4))) # <class 'range'>
        ```

      - `Range`의 사용 방법 

        - `range(n)` : 0부터 n-1까지의 숫자의 시퀀스
        - `range(n, m)` : n부터 m-1까지의 숫자의 시퀀스
        - `range(n, m, s)` : n부터 m-1까지 s만큼 증가시키는 숫자의 시퀀스

        ``` python
        # 역순
        print(list(range(6, 1, -1))) # [6, 5, 4, 3, 2]
        print(list(range(6, 1, -2))) # [6, 4, 2]
        print(list(range(6, 1, 1))) # []
        ```

    - 슬라이싱 연산자

      - 인덱스와 콜론을 사용하여 문자열의 특정 부분만 잘라낼 수 있음

        ``` python
        # 리스트([1:4]에서 1은 포함 4는 미포함)
        print([1, 2, 3, 5][1:4]) # [2, 3, 5]
        
        # 튜플
        print((1,2,3)[:2]) # (1, 2)
        
        # range
        print(range(10)[5:8]) # range(5,8)
        
        # 문자열
        print('abcd'[2:4]) # cd
        ```

      - 시퀀스를 k간격으로 슬라이싱

        ``` python
        # 리스트
        print([1, 2, 3, 5][0:4:2]) # [1, 3]
        
        # 튜플
        print((1, 2, 3, 5)[0:4:2]) # (1, 3)
        
        # range
        print(range(10)[1:5:3]) # range(1, 5, 3)
        
        # 문자열
        print('abcdefg'[1:3:2]) # b
        ```

      - `s[::]` : 처음부터 끝까지, 전체를 의미 `s[0:len(s):1]`과 동일

      - `s[::-1]` : `s[-1:-(len(s)+1:-1)]`과 동일

  - 비시퀀스형

    - `셋(Set)` (가변형)

      - `Set`이란 중복되는 요소가 없이, 순서에 상관없는 데이터들의 묶음

      - 중복되는 원소가 있다면 하나만 저장

      - 순서가 없기 때문에 인덱스를 이용한 접근 불가능

      - 집합 연산이 가능(합집합, 차집합, 교집합)

      - 담고 있는 요소를 삽입 변경, 삭제 가능 => 가변 자료형

      - 중괄호(`{}`) 혹은 `set()`을 통해 생성

        - 빈 Set을 만들기 위해서는 `set()`을 반드시 활용해야 함

        ``` python 
        # Set는 중복 값 제거
        print({1, 2, 3, 1, 2}) # {1, 2, 3}
        print(type({1, 2, 3})) # <class 'set'>
        ```

      - 셋(Set) 사용하기

        - 다른 컨테이너에서 중복된 값을 쉽게 제거할 수 있음

        ``` python
        my_list = ['서울', '서울', '대전', '광주', '서울', '대전', '부산']
        print(len(set(my_list))) # 4
        
        # 순서 보장 x
        print(set(my_list)) # {'광주', '부산', '서울', '대전'} 
        ```

      - 셋(Set) 연산자

        - `|` : 합집합
        - `&` : 교집합
        - `-` : 차집합
        - `^` : 대칭차집합 `합집합 - 교집합`
        - (여집합은 없음)

        ``` python
        A_set = {1, 2, 3, 4}
        B_set = {1, 2, 3, "Hello", (1,2,3)}
        
        print(A_set | B_set) # {1, 2, 3, 4, (1,2,3), 'Hello'}
        print(A_set & B_set) # {1, 2, 3}
        print(A_set - B_set) # {(1, 2, 3), 'Hello'}
        print(A_set ^ B_set) # {'Hello', 4, (1, 2, 3)}
        ```

        

    - 딕셔너리(`dictionary`) (가변형)

      - 키 - 값(key-value) 쌍으로 이뤄진 자료형(3.7부터는 ordered, 이하 버전은 unordered)\
      - Dictionary의 키(`key`) : 변경이 불가능한 데이터(immutable)만 활용 가능
      - 각 키의 값(`values`) : 어떠한 형태든 관계 없음
      - 중괄호(`{}`) 혹은 `dict()`을 통해 생성
      - `key`를 통해 `value`에 접근

      ``` python 
      dict_a = {}
      print(type(dict_a)) # <class 'dict'>
      
      dict_b = dict()
      print(type(dict_b)) # <class 'dict'>
      
      dict_a = {'a': 'apple', 'b': 'banana', 'list': [1, 2, 3]}
      print(dict_a) # {'a': 'apple', 'b': 'banana', 'list': [1, 2, 3]}
      print(dict_a['list']) # [1, 2, 3]
      
      dict_b = dict(a='apple',b = 'banana', list=[1, 2, 3])
      print(dict_b) # {'a': 'apple', 'b': 'banana', 'list': [1, 2, 3]}
      ```

    

### 형 변환(Typecasting)

- 파이썬에서 데이터 형태는 서로 변환할 수 있음

- 암시적 형 변환(Implicit)

  - 사용자가 의도하지 않고, 파이썬 내부적으로 변환하는 경우

  ``` python 
  # bool
  # Numeric type(int, float)
  print(True + 3) # 4
  print(3 + 5.0) # 8.0
  ```

- 명시적 형 변환(Explicit)

  - 사용자가 특정 함수를 활용하여 의도적으로 자료형을 변환하는 경우
  - 단 형식에 맞는 문자열만 정수로 변환 가능

  ``` python
  # int
  print('3' + 4) # TypeError: can only concatenate str (not "int") to str
  # 명시적 타입 변환이 필요함
  print(int('3') + 4) # 7
  # 정수 형식이 아닌 경우 타입 변환을 할 수 없음
  print(int('3.5') + 5) # ValueError: invalid literal for int() with base 10:
  
  # float
  print('3.5' + 3.5) # TypeError: can only concatenate str (not "int") to str
  # 정수 형식인 경우에도 float로 타입 변환
  print(float('3')) # 3.0
  # float 형식이 아닌 경우 타입 변환할 수 없음
  print(float('3/4') + 5.3) # ValueError: could not convert string to float: '3/4'
  
  # str
  print(str(~~~)) # 모든 결과가 그대로 ~~~
  ```



### 입력

- `input()`은 모든 입력을 `str`로 생각한다

``` python
number = input('아무 숫자나 입력하세요.')
# 터미널에 111 222 입력
print(number) # 111 222
print(type(number)) # <class 'srt'>

# map(int, input().split()) 나중에 배움!
```

