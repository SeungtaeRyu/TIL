# 객체지향 프로그래밍 및 에러처리

---

### 개요

- 객체지향 프로그래밍(OOP)
  - 객체 지향 프로그래밍이란?
  - OOP기초
    - 객체 / 인스턴스 / 클래스
    - 클래스
    - 메서드
- 객체지향 핵심 개념
  - 추상화
  - 상속
  - 다형성
  - 캡슐화
- 에러와 예외

<br>

### 객체지향 프로그래밍

- 객체지향 프로그래밍 정의
  - 객체지향 프로그래밍(OOP)은 컴퓨터 프로그래밍의 패러다임 중 하나이다
  - 객체 지향 프로그래밍은 컴퓨터 프로그램을 명령어의 목록으로 보는 시각에서 벗어나 여러 개의 독린된 단위, 즉 "객체"들의 모임으로 파악하고자 하는 것이다. 각각의 객체는 메세지를 주고받고, 데이터를 처리할 수 있다.



- 객체지향의 장점 / 단점
  - 장점
    - 클래스 단위로 모듈화시켜 개발할 수 있으므로 많은 인원이 참여하는 대규모 소프트웨어 개발에 적합
    - 필요한 부분만 수정하기 쉽기 때문에 프로그램의 유지보수가 쉬움
  - 단점
    - 설계 시 많은 노력과 시간이 필요함
    - 실행 속도가 상대적으로 느림



### 객체와 인스턴스

- 클래스로 만든 객체를 인스턴스 라고도 함
  - 객체와 인스턴스의 차이점?
    - 이찬혁은 객체다(O)
    - 이찬혁은 인스턴스다(X)
    - 이찬혁은 가수의 인스턴스다(O)



### 기본 문법

- 클래스 정의 class MyClass:
- 인스턴스 생성 my_instance = MyClass()
- 메서드 호출 my_instance.my_method()
- 속성 my_instance.my_attribute





### 객체 비교하기

- ==
  - 동등한(equal)
  - 변수가 참조하는 객체가 동등한(내용이 같은) 경우 True
  - 두 객체가 같아 보이지만 실제로 동일한 대상을 가리키고 있다고 확인해 준 것은 아님
- is
  - 동일한(identical)
  - 두 변수가 동일한 객체를 가리키는 경우 True



## 변수

### 1. 인스턴스 변수

- 인스턴스 변수란?

  - 인스턴스가 개인적으로 가지고 있는 속성(attribute)
  - 각 인스턴스들의 고유한 변수

- 생성자 메서드`(__init__)`에서 `self.<name>`으로 정의

- 인스턴스가 생성된 이후 `<instance>.<name>`으로 접근 및 할당

  ``` python
  john = Person('john')
  print(john.name) # john
  john.name = 'John Kim'
  print(john.name) # John Kim
  ```

  

### 2. 클래스 변수

- 클래스 변수

  - 한 클래스의 모든 인스턴스가 공유하는 값을 의미
  - 같은 클래스의 인스턴스들은 같은 값을 갖게 됨
  - 예) 특정 사이트의 User 수 등은 클래스 변수를 사용해야 함

- `<classname>.<name>`으로 접근 및 할당

  ``` python
  class Circle():
      pi = 3.14 # 클래스 변수 정의
      
      def __init__(self, r):
          self.r = r # 인스턴스 변수
          
  c1 = Circle(5)
  c2 = Circle(10)
  
  print(Circle.pi) # 3.14
  print(c1.pi) # 3.14
  print(c2.pi) # 3.14
  
  Circle.pi = 5
  print(Circle.pi) # 5
  print(c1.pi) # 5
  print(c2.pi) # 5
  ```



### 3. 클래스 변수와 인스턴스 변수

- 클래스 변수를 변경할 때는 항상 `클래스.클래스변수` 형식으로 변경



### 4. 인스턴스와 클래스 간의 이름 공간(namespace)

- 클래스를 정의하면, 클래스와 해당하는 이름 공간 생성

- 인스턴스를 만들면, 인스턴스 객체가 생성되고 이름 공간 생성

- 인스턴스에서 특정 속성에 접근하면, 인스턴스-클래스 순으로 탐색

  ``` python
  class Person:
      name = 'unknown'
      
  p1 = Person()
  p2 = Person()
  p2.name = 'Kim'
  
  print(Person.name) # unknown
  print(p1.name) # unknown
  print(p2.name) # Kim
  ```

  



---

## 메서드



### 1. 인스턴스 메서드

- 정의

  - 인스턴스 변수를 사용하거나, 인스턴스 변수에 값을 전달하는 메서드

  - 클래스 내부에 정의되는 메서드의 기본

  - 호출 시, 첫번째 인자로 인스턴스 자기자신(self)이 전달됨

    ``` python
    class MyClass:
        
        def instance_method(self, arg1, ...):
            
    my_instance = MyClass()
    my_instance.instance_method()
    ```

    

- 생성자 메서드

  - 인스턴스 객체가 생성될 때 자동으로 호출되는 메서드

  - `__init__` 메서드 자동 호출

    ``` python
    class Person:
        
        def __init__(self, name):
            print(f'인스턴스가 생성되었습니다. {name}')
            
    person1 = Person('지민') # 인스턴스가 생성되었습니다. 지민
    ```

    

- 매직 메서드

  - Double underscore(__)가 있는 메서드는 특수한 동작을 위해 만들어진 메서드로,

    스페셜 메서드 혹은 매직 메서드라고 불림

  - 특정 상황에 자동으로 불리는 메서드

  - 예시

    - `__str__(self)` : 해당 객체의 출력 형태를 지정

    - `__len__(self)`   

    - `__repr__(self)`

    - `__it__(self, other)`

    - `__le__(self, other)`

    - `__eq__(self, other)`

    - `__gt__(self, other)` : 부등호 연산자(>, greater than)

    -  `__ge__(self, other)`

    - `__ne__(self, other)`

      

- 소멸자 메서드

  - 인스턴스 객체가 소멸되기 직전에 호출되는 메서드

    ``` python 
    class Person:
        def __del__(self):
            print('인스턴스가 사라졌습니다.')
            
    person1 = Person()
    del person1 # 인스턴스가 사라졌습니다
    ```



### 2.클래스 메서드

- 클래스가 사용할 메서드

- `@classmethod` 데코레이터를 사용하여 정의

  - 함수를 어떤 함수로 꾸며서 새로운 기능을 부여
  - @데코레이터(함수명) 형태로 함수 위에 작성
  - 순서대로 적용 되기 때문에 작성 순서가 중요

- 호출 시 첫번째 인자로 (cls)가 전달됨

  ``` python
  class Person:
      count = 0 # 클래스 변수
      def __init__(self, name): # 인스턴스 변수 설정
          self.name = name
          Person.count += 1
      
      @classmethod
      def number_of_population(cls):
          print(f'인구수는 {cls.count}입니다.')
          
  person1 = Person('류승태')
  person2 = Person('문소희')
  print(Person.count)
  ```



### 3. 클래스 메서드와 인스턴스 메서드

- 클래스 메서드 → 클래스 변수 사용

- 인스턴스 메서드 → 인스턴스 변수 사용

- 둘 다 사용하고 싶다면?

  - 클래스는 인스턴스 변수 사용이 불가능

  - 인스턴스 메서드는 클래스 변수, 인스턴스 변수 둘 다 사용이 가능

    

### 4. 스태틱 메서드

- 인스턴스 변수, 클래스 변수 아무것도 사용하지 않을 경우

- 즉, 객체 상태나 클래스 상태를 수정할 수 없음

- `@staticmethod` 데코레이터를 사용하여 정의

  ``` python
  class Person:
      count = 0 # 클래스 변수
      def __init__(self, name): # 인스턴스 변수 설정
          self.name = name
          Person.count += 1
          
      @staticmethod
      def check_rich(money): # 스태틱은 cls, self 사용 x
          return money > 10000
      
  person1 = Person('류승태')
  person2 = Person('문소희')
  print(Person.check_rich(100000)) # True 스태틱은 클래스로 접근 가능
  print(person1.check_rich(100000)) # True 스태틱은 인스턴스로 접근 가능
  ```



### 5. 메서드 정리

- 인스턴스 메서드

  - 호출한 인스턴스를 의미하는 self 매개 변수를 통해 인스턴스를 조작

- 클래스 메서드

  - 클래스를 의미하는 cls 매개 변수를 통해 클래스를 조작

- 스태틱 메서드

  - 클래스 변수나 인스턴스 변수를 사용하지 않는 경우에 사용
    - 객체 상태나 클래스 상태를 수정할 수 없음

  ``` python
  class MyClass:
      
      def method(self):
          return 'instance method', self
      
      @classmethod
      def classmethod(cls):
          return 'class method', cls
      
      @staticmethod
      def staticmethod():
          return 'static method'
  ```

  

---



## 객체 지향의 핵심 개념

### 객체지향의 핵심 4가지

- 추상화
- 상속
- 다형성
- 캡슐화



### 1. 추상화

- 현실 세계를 프로그램 설계에 반영

- 복잡한 것은 숨기고 필요한 것만 들어내기

  ex) 변수, 함수, 클래스



### 2. 상속

#### 상속의 정의

- 상속이란

  - 두 클래스 사이 `부모 - 자식 관계`를 정립하는 것

  - 클래스는 상속이 가능함
    - 모든 파이썬 클래스는 `object`를 상속 받음

- 하위 클래스는 상위 클래스에 정의된 속성, 행동, 관계 및 제약 조건을 모두 상속 받ㄴ음

- 부모 클래스의 속성, 메서드가 자식 클래스에게 상속되므로, 코드 재사용성이 높아짐

  ``` python
  class Person:
      def __init__(self, name, age):
          self.name = name
          self.age = age
          
      def talk(self): # 메서드 재사용
          print(f'반갑습니다 {self.name}입니다.')
          
  class Professor(Person):
      def __init__(self, name, age, department):
          self.name = name
          self.age = age
          self.department = department
          
  class Student(Person):
      def __init__(self, name, age, gpa):
          self.name = name
          self.age = age
          self.gpa = gpa
          
  p1 = Professor('박교수', 49, '컴공')
  s1 = Student('류승태', 30, 4.5)
  ```



#### 상속 관련 함수와 메서드

- isinstance(object, classinfo)

  - classinfo의 instance거나 subclass*인 경우 True

    ``` python
    print(isinstance(p1, Person)) # True
    print(isinstance(s1, Person)) # True
    ```

- issubclass(class, classinfo)

  - class가 classinfo의 subclass면 True

- super()

  - 자식클래스에서 부모클래스를 사용하고 싶은 경우

- mro 메서드 (Method Resolution Order)

  - 해당 인스턴스의 클래스가 어떤 부모 클래스를 가지는지 확인하는 메서드

  - 기존의 인스턴스 → 클래스 순으로 이름 공간을 탐색하는 과정에서 상속 관계에 있으면

    인스턴스 → 자식 클래스 → 부모 클래스로 확장



#### 상속 정리

- 파이썬의 모든 클래스는 object로부터 상속됨
- 부모 클래스의 모든 요소(속성, 메서드)가 상속됨
- super()를 통해 부모 클래스의 요소를 호출할 수 있음
- 메서드 오버라이딩을 통해 자식 클래스에서 재정의 가능함
- 상속관계에서의 이름 공간은 인스턴스, 자식 클래스, 부모 클래스 순으로 탐색



#### 다중 상속

- 두 개 이상의 클래스를 상속 받는 경우
- 상속받은 모든 클래스의 요소를 활용 가능함
- 중복된 속성이나 메서드가 있는 경우 **상속 순서에 의해 결정됨**



### 3. 다형성

#### 다형성의 정의

- 다형성 이란?
  - 여러 모양을 뜻하는 그리스어
  - 동일한 메서드가 클래스에 따라 다르게 행동할 수 있음을 의미
  - 즉, 서로 다른 클래스에 속해있는 객체들이 동일한 메세지에 대해 다른 방식으로 응답할 수 있음



#### 메서드 오버라이딩

- 상속받은 메서드를 재정의
  - 클래스 상속 시, 부모 클래스에서 정의한 메서드를 자식 클래스에서 변경
  - 부모 클래스의 메서드 이름과 기본 기능은 그대로 사용하지만, 특정 기능을 바꾸고 싶을 때 사용
  - 부모 클래스의 메서드를 실행시키고 싶은 경우 `super()`를 활용



### 4. 캡슐화

#### 캡슐화의 정의

- 객체의 일부 구현 내용에 대해 외부로부터 직접적인 액세스를 차단
  - 예시 : 주민등록번호
- 파이썬에서 암묵적으로 존재하지만, 언어적으로는 존재하지 않음



#### 접근제어자 종류

- Public Access Modifier
  - 언더바 없이 시작하는 메서드나 속성
  - 어디서나 호출이 가능, 하위 클래스 override 허용
  - 일반적으로 작성되는 메서드와 속성의 대다수를 차지
- Protected Access Modifier
  - **언더바 1개**로 시작하는 메서드나 속성
  - **암묵적 규칙**에 의해 부모 클래스 내부와 자식 클래스에서만 호출 가능
  - 하위 클래스 override 허용
- Private Access Modifier
  - **언더바 2개**로 시작하는 메서드나 속성
  - 본 클래스 내부에서만 사용이 가능
  - 하위클래스 상속 및 호출 불가능 (오류)
  - 외부 호출 불가능(오류)



#### getter 메서드와 setter 메서드

- 변수에 접근할 수 있는 메서드를 별도로 생성

  - getter 메서드 : 변수의 값을 읽는 메서드
    - @property 데코레이터 사용
  - setter 메서드 : 변수의 값을 설정하는 성격의 메서드
    - @변수.setter 사용

  ``` python
  class Person:
      def __init__(self, age):
          self._age = age
          
      @property
      def age(self):
          return self._age
      
      @age.setter
      def age(self, new_age):
          if new_age <= 19:
              raise ValueError('Too Young For SSAFY')
              return
          
          self._age = new_age
          
  p1 = Person(20)
  print(p1.age) # 20
  
  p1.age = 33
  print(p1.age) # 33
  
  p1.age = 19
  print(p1.age) # ValueError: Too Young For SSAFY
  ```

  

---



## 에러와 예외처리

### 개요

- 디버깅
- 에러와 예외
- 예외 처리
- 예외 발생 시키기



### 1. 디버깅

- 버그란?
  - 최초의 버그는 1945년 프로그래밍 언어의 일종인 코볼 발명자 그레이스 호퍼가 발견
  - 역사상 최초의 컴퓨터 버그는 Mark ll 라는 컴퓨터 회로에 벌레인 나방이 들어가 합선을 일으켜 비정상적으로 동작
  - 이때부터 소프트웨어에서 발생하는 문제를 버그라고 부름
- 디버깅의 정의
  - 잘못된 프로그램을 수정하는 것을 디버깅이라함 de(없앤다) + bugging(버그)
  - 에러 메세지가 발생하는 경우
    - 해당하는 위치를 찾아 메세지를 해결
  - 로직에 에러가 발생하는 경우
    - 명시적인 에러 메세지 없이 예상과 다른 결과가 나온 경우
      - 정상적으로 동작하였던 코드 이후 작성된 코드를 생각해봄
      - 전체 코드를 살펴봄
      - 휴식을 가져봄
      - 누군가에게 설명해봄
      - ...



- 디버깅 방법
  - print() 함수 활용
  - 개발 환경 등에서 제공하는 기능 활용
    - breakpoint, 변수 조회 등
  - python tutor 활용 (단순 파이썬 코드인 경우)
  - 뇌컴파일, 눈디버깅



### 2. 에러와 예외

- 문법 에러

  - SystaxError가 발생하면, 파이썬 프로그램은 실행이 되지 않음

  - 파일이름, 줄번호, ^문자를 통해 파이썬이 코드를 읽어 나갈 때(parser) 문제가 발생한 위치를 표현

  - 줄에서 에러가 감지된 가장 앞의 위치를 가리키를 캐럿(caret)기호 (^)를 표시

  - 종류

    - Invalid syntax : 문법 오류

    - assign to literal : 잘못된 할당

    - EOL(End of Line) :
    - EOF(End of File) : 

- 예외 (Exception)
  - 실행 도중 예상치 못한 상황을 맞이하면, 프로그램 실행을 멈춤
    - 문장이나 표현식이 문법적으로 올바르더라도 발생하는 에러
  - 실행 중에 감지되는 에러들을 예외(Exception)라고 부름
  - 예외는 여러 타입(type)으로 나타나고, 타입이 메세지의 일부로 출력됨
    - NameError, TypeError 등은 발생한 예외 타입의 종류(이름)
  - 모든 내장 예외는 Exception Class를 상속받아 이뤄짐
  - 사용자 정의 예외를 만들어 관리할 수 있음
  - 종류
    - ZeroDivisionError : 0으로 나눌 때
    - NameError : 정의되지 않은 변수를 쓸 때
    - TypeError : ex) `1+ '1'`, `round(3.5)`
    - ValueError : 타입은 올바르나 값이 적절하지 않거나 없는 경우
    - IndexError : 인덱스 범위 틀렸을 때
    - keyError : 딕셔너리에서 없는 키를 조회할 때
    - ModuleNotFoundError : 모듈을 찾지 못했을 때
    - importError : Module은 있으나 존재하지 않는 클래스/함수를 가져오는 경우
    - KeyboardInterrupt : 임의로 프로그램을 종료하였을 때
    - IndentationError : 들여쓰기가 적절하지 않은 경우



### 3. 예외 처리

#### 예외 처리

- try문(statement) / except절(clause)을 이용하여 예외 처리를 할 수 있음

  ``` python
  try:
      pass
  except 예외그룹1 as 변수1:
      pass
  except 예외그룹2 as 변수2:
      pass
  finally:
      pass
  ```

  

#### 에러 메세지 처리 (as)

- as 키워드를 활용하여 원본 에러 메세지를 사용할 수 있음

  ``` python
  try:
      empty_list = []
      print(empty_list)
  except IndexError as err:
      print(f'{err}, 오류가 발생했습니다.')
  ```

  

#### 복수의 예외 처리 실습

- 100을 사용자가 입력한 값으로 나누고 출력하는 코드를 작성해 보세요

  ``` python
  try:
      num = input('100으로 나눌 값을 입력하시오 : ')
      print(100 / int(num))
  except ValueError:
      print('숫자를 넣어주세요.')
  except ZeroDivisionError:
      print('0으로 나눌 수 없습니다.')
  except:
      print('뭔지는 모르겠지만 에러가 발생하였습니다.')
  ```

  

#### 예외 처리 종합

- try
  - 코드를 실행함
- except
  - try 문에서 예외가 발생 시 실행함
- else
  - try 문에서 예외가 발생하지 않으면 실행함

- finally
  - 예외 발생 여부와 관계없이 항상 실행함

``` python
try:
    f = open('nooofile.txt')
except FileNotFoundError:
    print('해당 파일이 없습니다.')
else:
    print('파일을 읽기 시작합니다.')
    print(f.read())
    print('파일을 모두 읽었습니다.')
    f.close()
finally:
    print('파일 읽기를 종료합니다.')
```





