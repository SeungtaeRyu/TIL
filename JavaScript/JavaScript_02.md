# JavaScript_02

<br>

## 목차

- 함수
- Array와 Object

<br>

<br>

## 함수

<br>

- #### 함수 선언식

  - ```javascript
    function add(num1, num2) {
      return num1 + num2
    }
      
    console.log(add(2, 7))
    ```

<br>

- #### 함수 표현식

  - 표현식 내에서 함수를 정의하는 방식

  - 함수 표현식은 함수의 이름을 생략한 익명 함수로 정의 가능

  - ```javascript
    const sub = function (num1, num2) {
      return num1 - num2
    }
    
    console.log(sub(2, 7))
    ```

  - 표현식에도 함수 이름을 정의할 수 있지만 그렇게는 쓸 일 없을거임!

<br>

- #### 기본 인자

  - 인자 작성 시 '=' 문자 뒤 기본 인자 선언 가능

  - ```javascript
    const greeting = function (name = 'Anonymous') {
      return `Hi ${name}`
    }
    
    greeting()
    ```

<br>

- #### 매개변수와 인자의 개수 불일치 허용

  - 매개변수보다 인자의 개수가 많을 경우 허용 (버림?)
  - 매개변수보다 인자의 개수가 적을 경우 허용 (undefined)

<br>

- #### Spread syntax (...)

  - 전개 구문

  - 배열에서 썼을때와 함수에서 썼을 때 기능이 다름

    - 배열에서 쓸 때

    - ```javascript
      let parts = ['shoulders', 'knees']
      let lyrics = ['head', ...parts, 'and', 'toes']
      ```

    - 함수에서 쓸 때

    - ```javascript
      const rest0pr = function (arg1, arg2, ...restArgs) {
        return [arg1, arg2, restArgs]
      }
      ```

<br>

- #### 함수의 타입

  - 선언식과 표현식 둘 다 `function` type 임!
  - 함수 선언식으로 정의한 함수는 var로 정의한 변수처럼 호이스팅이 발생
  - 함수 표현식으로 정의된 함수는 변수로 평가되어 변수의 scope 규칙을 따름 => 이거를 잘 써야 함!

<br>

- #### 화살표 함수

  - **함수를 비교적 간결하게 정의할 수 있는 문법**

    - function 키워드 생략 가능

    - 함수의 매개변수가 하나뿐이라면 `()` 도 생략 가능 => Airbnb 가이드에서는 생략 안하는걸 권장!

    - 함수의 내용이 한 줄이라면 `{}` 와 `return`도 생략 가능

    - ```javascript
      const greeting = (name) => `Hi ${name}`
      ```

  - 화살표 함수의 응용

    - 인자가 없다면 `()` or `_` 를 사용해야 함!
    - object 를 return 한다면 명시적으로 return을 적어준다!
    - return 을 적지 않으려면 괄호를 붙여야 한다! `({ key: 'value' })`

  - 즉시 실행 함수

    - 함수 전체를 `()`로 감싸고 의 선언 끝에 `()`를 추가하여 선언되자 마자 실행하는 형태

<br>

<br>

## Array와 Object

<br>

- #### Array

  - 키와 속성을 담고 있는 참조 타입의 객체

  - 순서를 보장

  - 주로 대괄호를 이용하여 생성하고 양의 인덱스로 접근가능

  - 음의 인덱스는 접근 불가능! 대신, `array.length -1` 이런 형태로 접근 가능


<br>

- #### 배열 메서드 기초

  - `reverse` : 반대로 정렬

  - `push & pop` : 가장 뒤에 요소 추가 or 제거

  - `unshift & shift` : 가장 앞에 요소 추가 or 제거

  - `includes` : 존재하는지 참/거짓

  - `indexof` : 첫번째 값의 인덱스 반환, 요소가 없을 경우 -1 반환

  - `join` : 모든 요소를 구분자롤 이용하여 연결, 생략 시 쉼표 기준

<br>

- #### 배열 메서드 심화

  - **배열을 순회하며 특정 로직을 수행하는 메서드**

  - **메서드 호출 시 인자로 `callback 함수`를 받는 것이 특징**

  - **종류**

    - `forEach` : 콜백 함수를 한 번씩 실행, **반환값 없음**

      - ```javascript
        colors.forEach((color) => consoloe.log(color)
        ```

    - `map` : **콜백 함수의 반환 값**을 요소로 하는 **새로운 배열 반환**

      - ```javascript
        const newArray = numbers.map((number) => number * 2)
        ```

    - `filter` : **콜백 함수의 반환 값이 참인 요소들만** 모아서 **새로운 배열을 반환**

      - ```javascript
        const newArray = products.filter((product) => {
          return projuct.type === 'fruit'
        })
        ```

    - `reduce` : **콜백 함수의 반환 값들을 하나의 값(acc)에 누적 후 반환**

      - 두번째 인자는 선택인자이고 초기값을 의미!

      - ```javascript
        const sumNum = numbers.reduce((result, number) => {
          return result + number
        }, 0)
        ```

    - `find` : 콜백 함수의 **반환 값이 참이면 해당 요소를 반환**

      - ```javascript
        const avanger = avengers.find((avenger) => {
            return avenger.name === 'Tony Stark'
        })
        ```

    - `some` : 배열의 **요소 중 하나라도 판별 함수를 통과**하면 참을 반환

      - ```javascript
        const result = arr.some((e) => e % 2 === 0) // true
        ```

    - `every` : 배열의 **모든 요소가 판별 함수를 통과**하면 참을 반환

      - ```javascript
        const result = arr.every((e) => e % 2 === 0) // false
        ```


<br>

<br>

- #### Object

  - key 는 문자열 타입만 가능
  - value 는 모든 타입(함수포함) 가능
  - 객체 요소 접근은 점`.` 또는 대괄호`['']` 로 가능
    - key 이름에 띄워쓰기 같은 구분자가 있으면 대괄호 접근만 가능!

<br>

- #### 객체 관련 문법

  - **속성명 축약**

    - 객체를 정의할 때 key 와 value의 이름이 값으면  축약 가능!

  - **메서드명 축약**

    - 메서드 선언 시 function 키워드 생략 가능!

    - ```javascript
      const obj = {
        name: 'jack',
        greeting() {
          console.log('hi!')
        },
      }
      ```

  - **계산된 속성명 사용하기**

    - 객체를 정의할 때 key 의 이름을 표현식으로 이용하여 동적으로 생성 가능

    - ```javascript
      const key = 'country'
      
      const obj = {
        [key]: value,
      }
      
      console.log(obj.country) // value
      ```

  - **구조 분해 할당** :sparkles:

    - 배열 또는 객체를 분해하여 속성을 변수에 쉽게 할당할 수 있는 문법

    - ```javascript
      const userInformation = {
        name: 'ssafy kim',
        userId: 'ssafyStudent1234',
        phoneNumber: '010-1234-1234',
        email: 'ssafy@ssafy.com'
      }
      
      const { name, userId } = userInfomation
      ```

  - **Spread syntax (...)**

    - 배열과 마찬가지로 전개구문을 사용해 객체 내부에서 객체 전개 가능
    - 얕은 복사에 활용 가능

  - **JSON**

    - Key-Value 형태로 이루어진 자료 표기법이고 **문자열**의 형태임!

    - JavaScript 에서 JSON을 사용하기 위해서는 Object로 변환이 필요!

    - ```javascript
      // Object -> json
      const objToJson = JSON.stringify(jsonData)
      console.log(typeof objToJson) // string
      
      // json -> Object
      const jsonToObj = JSON.parse(objtoJson) 
      console.log(typeof jsonToObj) // object
      ```

<br>











