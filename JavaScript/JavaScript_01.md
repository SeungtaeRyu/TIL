# JavaScript 기초 문법

<br>

## 목차

- JavaScript 실행하기
- JavaScript 기초 문법

<br>

<br>

## JavaScript 실행하기

<br>

- #### 사전준비

  - vscode 확장 프로그램 open in browser 설치

<br>

- #### 방법 1

  - `.js` 파일을 open browser 로 열고 Console 에서 확인

<br>

- #### 방법 2

  - `.html` 파일에서 `.js`파일을 불러오기
  - `<script src="hello.js"></script>`

<br>

- #### 방법 3

  - Web browser 의 Console 화면에서 바로 작성하기	

<br>

- #### 방법 4

  - node.js 설치 후 터미널에서 node [파일명].js 로 실행하기

<br>

<br>

## JavaScript 기초 문법

<br>

- #### 코드 작성법

  - 세미콜론 : 써도 되고 안써도 되는데 쓰지 말자는게 추세!

  - 들여쓰기 : 2칸 

  - 블럭 :  JavaScript는 중괄호 `{ } ` 기준으로 코드 블럭을 구분

  - 스타일가이드 : Airbnb, Google, Standart 등이 있는데 Airbnb를 알아봄!

  - 주석 : 한줄 주석 `//`, 여러 줄 주석 `/* */` 

<br>

- #### 변수와 식별자

  - 식별자는 문자, 달러($), 밑줄(_)로 시작
  - **대소문자**를 구분하며, **클래스명 외에는 모두 소문자로 시작**
  - 예약어 사용 불가능 (for, if, function 등)
  - 식별자 정의
    - 카멜 케이스(camelCase) - 변수, 객체, 함수에 사용
    - 파스칼 케이스(PascalCase) - 클래스, 생성자에 사용
    - 대문자 스네이크 케이스(SNAKE_CASE) - 상수에 사용, 변경될 가능성이 없는 값
  - 변수 선언 키워드 (동시에 값 할당 가능)
    - let
      - 블록 스코프 지역 변수를 선언
      - 재할당 가능 & 재선언 불가능
    - const 
      - 블록 스코프 읽기 전용 상수를 선언
      - 재할당 불가능 & 재선언 불가능
      - 반드시 초기값 설정 해야 함
    - var
      - 함수 스코프를 가짐
      - 재할당 가능 & 재선언 가능
      - ES6 이전에 사용되던 키워드 -> 쓸 일 없음!

<br>

- #### 데이터 타입

  - **원시타입**과 **참조타입**으로 분류 됨
  -  Number 
    - 정수 또는 실수형 숫자를 표현하는 자료형
    - `NaN`을 반환하는 경우 : Not-A-Number (숫자로 읽을 수 없음, 허수, 피연산자가 NaN, 등등)
  - String
    - 따옴표 모두 가능
    - 곱셈, 나눗셈, 뺄셈은 안되지만 덧셈 가능
    - `Quote`를 사용하면 선언 시 줄바꿈 안됨. `\n` 사용하면 가능
    - `Template literals`(백틱) 을 사용하면 줄바꿈이 됨, 변수도 삽입 가능해짐
  - Empty Value
    - `null` 과 `undefined`가 존재 - 설계 실수임!
    - `null` : 값이 없음을 **의도적**으로 표현할 때 사용
    - `undefined` : 값이 할당되지 않으면 **자동**으로 할당됨
    - 데이터 타입 확인은 `typeof` 로 확인! 
      - 원시타입임에도 null은 `objects` 로 반환되는데 설계 당시 버그고 아직까지 해결 못함!
  - Boolean
    - true, false 모두 소문자
    - boolean이 아닌 데이터 타입은 **자동 형변환 규칙** 에 따라 true, false로 변환됨
      - undefined : 항상 false
      - null : 항상 false
      - Number : 0, -0, NaN false, 나머지 true
      - String : 빈 문자열 false, 나머지 true
      - Object : 항상 true

<br>

- #### 연산자

  - 할당 연산자
    - 기본적으로 알고 있는 것과 동일
    - `++`, `--` 등이 있지만 Airbnb 스타일 가이드에서 잘 사용하지 않음
  - 비교 연산자
    - 기본적으로 알고 있는 것과 동일
  - 동등 연산자(==)
    - 파이썬과 다름!!
    - 비교할 때 암묵적 타입 변환을 통해 타입을 일치시킨 후 값은 값인지 비교한다
      - 1 == '1' => true가 됨
  - 일치 연산자(===)
    - 값과 타입 모두 비교!
    - 암묵적 타입 변환 이루어지지 않음
  - 논리 연산자
    - 세가지 논리 연산자로 구성
      - and : `&&`
      - or : `||`
      - not : `!`
    - 단축 평가 지원함!
      - false && ~~~~ => false
      - true || ~~~~ => True
  - 삼항 연산자
    - `[조건식] ? [참일때 실행] : [거짓일때 실행]`

 <br>

- #### 조건문

  - `if` statement
    - `if`, `else if`, `else` 문법임!
    - 조건은 **소괄호** 안에 작성
    - 실행할 코드는 **중괄호** 안에 작성
  - `switch` statement
    - 표현식(expression)의 결과값을 이용한 조건문
    - 표현식의 결과값과 `case` 문의 오른쪽 값을 비교
    - `break`, `default` 문을 [선택적]으로 사용 가능
    - `break` 없는 경우 `break`를 만나거나 `default`문을 실행할 때 까지 다음 조건문 전부 실행

<br>

- #### 반복문

  - `while`

    - 참이기만 하면 문장을 계속해서 수행!

  - `for`

    - 특정한 조건이 거짓으로 판별될 때까지 반복!

    - ```javascript
      for ([초기문]; [조건문]; [증감문]) { // 여기는 세미콜론 항상 써야해요!
      	// do something
      }
      ```

  - `for...in` 

    - 객체의 속성을 순회할 때 사용 (js에서 객체 => key, value인 딕셔너리 형태)

    - 배열도 순회 가능하지만 인덱스 순으로 순회한다는 보장이 없으므로 권장하지 않음

    - ```javascript
      const fruits = { a: 'apple', b: 'banana'}
      
      for (const key in fruits) {
          console.log(key) // a, b
          console.log(fruits[key]) // apple, banana
      }
      ```

  - `for...of`

    - 반복 가능한 타입을 순회할 때 사용

    - 반복 가능한(iterable) 객체의 종류 : `Array`, `Set`, `String` 등

    - ```javascript
      const numbers = [0, 1, 2, 3]
      
      for (const number of fruits) {
          console.log(number) // 0, 1, 2, 3
      }
      ```

  - `for...in` , `for...of` 차이점

    - for...in : 속성 **이름**을 통해 반복 (key라고 생각하면 편할듯? 리스트도 key가 있었다?)
    - for...of : 속성 **값**을 통해 반복! 객체를 for of 했을 경우 error 발생~



























