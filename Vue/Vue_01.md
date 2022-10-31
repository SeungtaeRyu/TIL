# Vue

<br>

## 목차

- [Vue instance](#Vue-instance)
- [Basic of Syntax](#Basic-of-Syntax)
- [Vue advanced](#Vue-advanced)

<br><br>

## Vue instance

- #### MVVM Pattern

  - Model, View, ViewModel 로 구성
  - View : 우리 눈에 보이는 부분 = DOM
  - Model : 실제 데이터 = JSON
  - View Model
    - View를 위한 Model
    - View 와 연결되어 Action을 주고 받음

<br>

- #### Vue instance

  1. Vue CDN 가져오기
  2. `new` 연산자를 사용한 생성자 함수 호출
  3. 인스턴스 출력 및 확인

<br>

- #### el (element)

  - Vue instance와 DOM을 mount(연결) 하는 옵션
    - HTML id 혹은 class와 mount 가능
  - Vue instance와 **연결되지 않은 DOM 외부는 Vue의 영향을 받지 않음**
    - Vue 속성 및 메서드 사용 불가

<br>

- #### data

  - 데이터 객체는 반드시 기본 객체 `{} (Object)` 여야 함
  - 객체 내부의 아이템들은 value로 모든 타입의 객체를 가질 수 있다
  - 정의된 속성은 `interpolation {{ }}` 을 통해 view에 렌더링 가능하다

<br>

- #### methods

  - Vue instance의 method들을 정의하는 곳
  - method 내에서 this를 사용하면 `app.data` 까지 참조해준다!
  - 메서드를 정의 할 때 Arrow Function을 사용하면 안됨, 콜백함수에서는 써도 됨!
    - Arrow Function을 정의할 때 사용하면 this는 window가 된다

<br>

<br>

## Basic of Syntax

- #### Template Syntax

  - Vue2 guide > template syntax 참고

<br>

- #### Directives 기본 구성

  - v-접두사가 있는 특수 속성에는 값을 할당 할 수 있음

    - 값에는 JS 표현식을 작성 할 수 있음

  - directive의 역할은 **표현식의 값**이 **변경**될 때 **반응적**으로 DOM에 적용하는 것

  - `:` 을 통해 전달인자를 받을 수 있음

  - `.` 으로 표시되는 특수 접미사 - directive를 특별한 방법으로 바인딩 해야 함

  - ```vue
    v-on:submit.prevent="onsubmit"
    ```

<br>

- #### v-접두사

  - v-text
    - {{ }} 와 동일한 역할 (정확히 동일한 역할인 것은 아님)

  - v-html
    - RAW HTML을 표현할 수 있는 방법 (단, 사용자가 입력하거나 제공하는 컨텐츠에는 절대 사용 금지)
  - v-show
    - 표현식의 값에 따라 보여줄 것인지를 결정 (boolean 값이 변경 될 때 마다 반응)
    - display: none이 toggle 되는 형식
  - v-if
    - v-show와 사용 방법은 동일
    - 단, 값이 false인 경우 DOM에서 사라짐
    - `v-if` `v-else-if` `v-else` 형태로 사용
  - v-for
    - `for .. in ..` 형식으로 작성
    - index를 함께 출력하고자 한다면 `(char, index)` 형태로 사용 가능
    - 각 요소가 객체라면 `dot notation`으로 접근 할 수 있음
    - 특수 속성 key
      - **v-for 사용 시 반드시 key 속성을 각 요소에 작성**
      - vue 화면 구성 시 이전과 달라진 점을 확인하는 용도로 활용
      - 각 요소가 고유한 값을 가지고 있지 않다면 생략할 수 있음
  - v-on
    - addEventListener의 첫 번째 인자와 동일한 값들로 구성
    - 대기하고 있던 이벤트가 발생하면 할당된 표현식 실행, 메소드 실행도 가능
    - shortcut 제공 `v-on:click` :arrow_right: `@click`
  - v-bind
    - HTML 기본 속성에 Vue data를 연결
    - class의 경우 다양한 형태로 연결 가능
      - 조건부 바인딩
        - {'class Name': '조건 표현식'}
        - 삼항 연산자도 가능
      - 다중 바인딩
        - ['JS 표현식', 'JS표현식', ...]
    - shortcut 제공 `v-bind:class` :arrow_right: `@class`
  - v-model
    - Vue instance와 DOM의 양방향 바인딩
    - Vue data 변경 시 v-model로 연결된 사용자 입력 element에도 적용
    - 영어 빼고는 실시간 반영 어려움!

<br>

<br>

## Vue advanced

- #### computed

  - Vue instance가 가진 options 중 하나
  - 계산 결과가 변하기 전까지 함수를 재호출하는 것이 아닌 계산된 **값**을 반환
  - 함수에 종속된 변수의 값이 변경되었을 때 **재계산**을 함

<br>

- #### watch

  - 특정 데이터의 변화를 감지하는 기능
    1. watch 객체를 정의
    2. 감시할 대상 data를 지정
    3. data가 변할 시 실행 할 함수를 정의
       - 첫 번째 인자는 변동 전 data
       - 두 번째 인자는 변동 후 data
  - 배열이나 객체는 한 겹 감싸져 있기 때문에 `deep: true` 속성을 사용하면 감시 가능해진다
  - 디버깅의 용도로 자주 사용

<br>

- #### filters

  - 텍스트 형식화를 적용할 수 있는 필터
  - interpolation 혹은 v-bind를 이용할 때 사용 가능
  - 필터는 자바스크립트 표현식 마지막에 `|` (파이프)와 함께 추가되어야 함
  - 이어서 사용(chaining) 가능























