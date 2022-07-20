# 제어문 (Control Statement) & 함수(function)

---

- 파이썬은 기본적으로 `위에서부터 아래로 차례대로 명령을 수행`
- 특정 상황에 따라 코드를 선택적으로 실행(분기/조건) 하거나 계속하여 실행(반복)하는 제어가 필요함



## 목차

- [내부 해더 이동](#내부-해더-이동)
- [제어문](#제어문)
- [제어문](##제어문)
- [조건문](#조건문)
- [조건문](###조건문)
- 



## 제어문

- ### 조건문

  - 조건문은 `참/거짓`을 판단할 수 있는 `조건식`과 함께 사용

    - 기본형식

      - 조건이 `참인 경우` 이후 들여쓰기 되어있는 코드 블록을 실행

      - 이외의 경우 `else` 이후 들여쓰기 되어있는 코드 블록을 실행

      - `else`는 선택적으로 활용할 수 있음

        ``` python
        if 조건:
            # Run this Code block
        else:
            # Run this Code block
        ```

  - 복수 조건문

    ``` python 
    if 조건:
        # Run this Code block
    elif 조건:
        # Run this Code block
    elif 조건:
        # Run this Code block
    else:
        # Run this Code block
    ```

- 중첩 조건문

  - 조건문은 다른 조건문에 중첩되어 사용될 수 있음

  - `들여쓰기에 유의`하여 작성할 것

    ``` python
    if 조건:
        # Run this Code block
        if 조건:
            # Run this Code block
    else:
        # Run this Code block
    ```

  - 중촉 조건문 실습 

    ``` python
    dust = 500
    if dust > 150:
        print('매우 나쁨')
        if dust > 300:
            print('실외 활동을 자제하세요.')
    elif dust > 80:
        print('나쁨')
    elif dust > 30:
        print('보통')
    elif dust > 0:
        print('좋음')
    else:
        print('값이 잘못 되었습니다')
        
    '''
    매우나쁨
    실외 활동을 자제하세요.
    '''
    ```



- ### 조건 표현식

  - 조건 표현식이란?

    - 조건 표현식을 일반적으로 조건에 따라 값을 정할 때 활용

    - `삼항 연산자`로 부르기도 함

    - 예시

      ` true인 경우 값 if 조건 else false인 경우 값`

      ``` python
      # 절대값을 저장하기 위한 코드
      value = num if num >= 0 else value = -num
      ```

- ### 반복문

- 특정 조건을 만족할 때까지 같은 동작을 게속 반복하고 싶을 때 사용

- 반복문의 종류

  - `while` 문 : 조건식이 참인 경우 반복적으로 코드를 실행

    - 조건이 참인 경우 들여쓰기 되어 있는 코드 블록이 실행됨

    - 코드 블록이 모두 실행되고, 다시 조건식을 검사하며 반복적으로 실행됨

    - `while`문은 무한 루프를 하지 않도록 `종료 조건이 반드시 필요`

      ``` python
      while 조건:
          # Code block
      ```

  - `for` 문 : 반복가능한 객체를 모두 순회하면 종료 (별도의 종료 조건이 필요 없음)

    - `for`문은 시퀀스(`string`, `tuple`, `list`, `range`)를 포함한 순회 가능한 객체(iterable_)의 요소륾 ㅗ두 순회
    - 처음부터 끝까지 모두 순회하므로 별도의 종료 조건이 필요하지 않음
    - Iterable
      - 순회할 수 있는 자료형(`string`, `list`, `dict`, `tuple`, `range`, `set` 등)
      - 순회형 함수(`range`, `enumerate`)

    - 사용 예시

      ``` python
      for fruit in ['apple', 'mango', 'banana']:
          print(fruit)
      print('끝')
      
      '''
      apple
      mango
      banana
      '''
      ```

    - for문을 이용한 문자열(`String`) 순회

      ``` python
      chars = input()
      # happy
      
      for idx in range(len(chars)):
          print(chars[idx])
          
      '''
      h
      a
      p
      p
      y
      '''
      ```

    - 딕셔너리(`Dictionary`) 순회

      - 딕셔너리는 기본적으로 `key`를 순회하며, `key`를 통해 값을 활용

        ``` python
        grades = {'john': 80, 'eric': 90}
        for student, grade in grades.items():
            print(student, grade)
            
        '''
        john 80
        eruc 90
        '''
        ```

    - `enumerate` 순회

      - 인덱스와 객체를 쌍으로 담은 열거형(`enumerate`) 객체 반환

      - (`index`, `value`) 형태의 `tuple`로 구성된 열거 객체를 반환

        ``` python
        members = ['민수', '영희', '철수']
        
        for idx, number in enumerate(member):
            print(idx, number)
            
        '''
        0 민수
        1 영희
        2 철수
        '''
        ```

      - 파이썬 문서에서 확인하기

        ``` python
        members = ['민수', '영희', '철수']
        
        print(list(enumerate(members))) # 
        print(list(enumerate(members, start = 1))) # 
        ```

    -  `List Comprehension` 

      - 표현식과 제어문을 통해 특정한 값을 가진 리스트를 간결하게 생성하는 방법

      - `[code for 변수 in iterable]`

      - `[code for 변수 in iterable if 조건식]`

        ``` python
        # 1~3의 세제곱 리스트 만들기
        cubic_list = []
        for number in range(1, 4):
            cubic_list.append(number ** 3)
        print(cubic_list)
        
        # [1, 8, 27]
        
        cubic_list = [number ** 3 for number in range(1, 4)]
        print(cubic_list)
        
        # [1, 8, 27]
        ```

    - `Dictionary Comprehension`

      - `{key: balue for 변수 in iterable}`

      - `{key: balue for 변수 in iterable if 조건식}`

        ``` python
        # 1~3의 세제곱 딕셔너리 만들기
        cubic_dict = {}
        for number in range(1, 4):
            cubic_dict[number] = number ** 3
        print(cubic_dict)
        
        # [1: 1, 2: 8, 3: 27]
        
        cubic_dict = {number ** 3 for number in range(1, 4)}
        print(cubic_dict)
        
        # [1: 1, 2: 8, 3: 27]
        ```

        

- ### 반복문 제어

  - `break`

    - 반복문을 종료

      ``` python 
      n = 0
      while True:
          if n == 3:
              break
          print(n)
          n += 1
      '''
      0
      1
      2
      '''
      
      for i in range(10):
          if i > 1:
              print('0과 1만 필요해!')
              break
          print(i)
      '''
      0
      1
      0과 1만 필요해!
      '''
      ```

      

  - `continue`

    - continue 이후의 코드 블록은 수행하지 않고, 다음 반복을 수행

      ``` python
      for i in range(6):
          if i % 2 == 0:
              continue
          print(i)
      '''
      1
      3
      5
      '''
      ```

      

  - `pass`

    - 아무것도 하지 않음(문법적으로 필요하지만, 할 일이 없을 때 사용)

    - 반복문 아니어도 사용 가능

      ``` python
      # i가 2일 때 pass
      for i in range(4):
          if i == 2:
              pass
        	print(i)
      '''
      0
      1
      2
      3
      '''
      ```

      

  - `for-else`

    - 끝까지 반복문을 싱행한 이후에 `else`문 실행

      - `break`를 통해 중간에 종료되는 경우 `else`문은 실행되지 않음

        ``` python
        for char in 'apple':
            if char == 'b':
                print('b!')
                break
        else:
            print('b'가 없습니다.)   
        # b가 없습니다.
        
        for char in 'banana':
            if char == 'b':
                print('b!')
                break
        else:
            print('b'가 없습니다.)   
        # b!
        ```

  



## 함수

- ### 함수를 왜 사용할까요?

  - `Decompositon`(분해)
  - `Abstraction`(추상화)

- ### Decompositon

  - 기능을 분해하고, 재사용 가능하게 만들고

    ``` python
    # 함수를 사용하지 않을 때
    numbers = [1, 2, 3]
    count = 0
    for i in numbers:
        conut += 1
    print(count) # 3
    
    # 함수 사용
    print(len([numbers])) # 3
    ```

    ``` python
    # 내장 함수만 사용
    numbers = [1, 2, 3]
    print(sum(numbers) / len(numbers)) # 2.0
    
    
    # 사용자 정의 함수 사용
    numbers = [1, 2, 3]
    
    def average(numbers):
        return sum(numbers) / len(numbers)
    
    print(average(numbers)) # 2.0
    ```

  

- ### Abstraction

  - 복잡한 내용을 모르더라도 사용할 수 있도록 재사용성과 가독성, 생산성

  - 사실 내부 구조를 변경할게 아니라면 몰라도 무방

    - 그것이 함수의 장점이자 프로그래밍의 매력
    - 복잡한 걸 숨기고 알고 싶은것만 드러내어 이해하기 쉬움

    

- ### 함수의 기초

  - 함수의 종류

    - 내장 함수 : 파이썬에 기본적으로 포함된 함수
    - 외장 함수 : `import`문을 통해 사용하며, 외부 라이브러리에서 제공하는 함수
    - 사용자 정의 함수 : 직접 사용자가 만드는 함수

  - 함수의 정의

    - 특정한 기능을 하는 코드의 조각(묶음)

    - 특정 코드를 매번 다시 작성하지 안혹, 필요시에만 호출하여 간편히 사용

      ``` python
      def function_name(parameter):
          return returning_value
      ```

      

  - 함수의 기본 구조

    - 선언과 호출(`define` & `call`)

      ``` python
      # 선언
      def foo():
          return True
      
      def add(x, y):
          return x + y
      
      # 호출
      foo()
      add(2, 3)
      ```

    - 입력(`Input`)

    - 문서화(`Docsting`)

    - 범위(`Scope`)

    - 결과값(`Output`)

  - 함수의 실행 순서 예시

    ``` python
    num = 0
    num = 1
    
    def func1(a, b):
        return a + b
    
    def func2(a, b):
        return a - b
    
    def func2(a, b):
        return func1(a, 5) + func2(5, b)
    
    reslut func3(num1, num2)
    print(result) # 9
    ```









# 내부 해더 이동

