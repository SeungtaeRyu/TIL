# JavaScript 03 심화

<br>

## 목차

- [DOM](#DOM)
- [Event](#Event)
- [this](#this)

<br>

## DOM

<br>

- #### DOM 주요 객체

  - **window**
  - **document**
  - navigator, location, history, screen 등등

<br>

- #### window object

  - 가장 최상위 객체 (작성 시 생략 가능)
  - 탭 기능이 있는 브라우저에서는 각각의 탭을 각각의 window 객체로 나타냄
  - window 메서드 예시
    - window.open() : 새 탭 열기
    - window.print() : 경고 대화 상자 표시
    - window. alert() : 인쇄 대화 상자 표시

<br>

- #### document object

  - 브라우저가 불러온 웹 페이지
  - 페이지 컨텐츠의 진입점 역할을 하며, <body> 등과 같은 수많은 다른 요소들을 포함
  - documentdml 속성 예시
    - document.title : 문서 제목
  - document는 window의 속성이다

<br>

- #### DOM 조작 순서

  1. 선택 (Select)
  2. 조작 (Manipulation)
     - 생성, 추가, 삭제 등

<br>

- #### 선택 관력 메서드

  - document.querySelecor(selector) :  CSS 셀렉터와 처음 일치하는 요소 한 개 선택
  - document.querySelectorAll(selector) : CSS 셀렉터와 일치하는 여러 요소를 선택
    - 하나 이상의 셀렉터를 포함하는 유효한 CSS selector를 인자(문자열)로 받음
    - 제공한 CSS selector를 만족하는 **NodeList (index접근, forEach 메서드 등 사용 가능)**를 반환
    - 예시
      - `document.querySelectorAll('body > ul > li')`

<br>

- #### 조작 관련 메서드 (생성)

  - document.createElement (tagName) 
    - 작성한 tagName의 HTML 요소를 생성하여 반환

<br>

- #### 조작 관련 메서드 (입력)

  - Node.innerText
    - Node 객체와 그 자손의 텍스트 컨텐츠(DOMString)를 표현 (해당 요소 내부의 raw text)
    - 사람이 읽을 수 있는 요소만 남김
    - 즉, 줄 바꿈을 인식하고 숨겨진 내용을 무시하는 등 최종적으로 스타일링이 적용된 모습으로 표현

<br>

- #### 조작 관련 메서드 (추가)

  - Node.appendChild()
    - 한 Node를 특정 부모 Node의 자식 NodeList 중 마지막 자식으로 삽입
    - 한번에 오직 하나의 Node만 추가할 수 있음
    - 추가된 Node 객체를 반환
    - 만약 주어진 Node가 이미 문서에 존재하는 다른 Node를 참조한다면 현재 위치에서 새로운 위치로 이동

<br>

- #### 조작 관련 메서드 (삭제)

  - Node.removeChild()
    - DOM에서  자식 Node를 제거
    - 제거된 Node를 반환

<br>

- #### 조작 관련 메서드 (속성 조회 및 설정)

  - Element.getAttribute(attributeName)
    - 해당 요소의 지정된 값(문자열)을 반환
    - 인자는 값을 얻고자 하는 속성의 이름
  - Element.setAttribute(name, value)
    - 지정된 요소의 값을 설정
    - 속성이 이미 존재하면 값을 갱신, 존재하지 않으면 지정된 이름과 값으로  새 속성을 추가
  - Element.classList.toggle('blue')
    - 존재하는 클래스면 제거하고 false 반환, 존재하지 않는 클래스면 추가하고 true 반환

<br>

<br>

## Event

<br>

- #### Event object

  - 네트워크 활동이나 사용자와의 상호작용 같은 사건의 발생을 알리기 위한 객체
  - DOM 요소는 Evene를 받고 (**"수신"**)
  - 받은 Event를 **"처리"**할 수 있음
    - Event 처리는 주로 **addEventListener()** 라는 Event 처리기를 다양한 html 요소에 **"부착"**해서 처리함

<br>

- #### Event handler - addEventListener()

  - 대상에 특정 Event가 발생하면, 할 일을 등록하자
    - `EventTartget.addEventListener(type, listener)`
    - type
      - 반응 할 Event 유형을 나타내는 대소문자 구분 문자열
      - input, click, submit, ..
      - 이벤트 확인(https://developer.mozilla.org/en-US/docs/Web/Events)
    - Listener
      - 지정된 타입의 Event를 수신할 객체
      - JavaScript function 객체여야 함
      - 콜백 함수를 발생한 Event의 데이터를 가진 Event 기반 객체를 유일한 매개변수로 받음

<br>

- #### Event 등록 실습

  - 버튼을 클릭하면 특정 변수 값 변경하기

    ```javascript
    const btn = document.querySelector('#btn')
    btn.addEventListener('click', function (event) {
        const pTag = document.querySelector('#counter')
        countNum += 1
        pTag.innerText = countNum
    })
    ```

    <br>

  - input에 입력하면 입력 값을 실시간으로 출력하기

    ```javascript
    const textInput = document.querySelector('#text-input')
    textInput.addEventListener('input', function (event) {
        const pTag = document.querySelector('p')
        pTag.innerText = event.target.value
    })
    ```

    <br>

  - input에 입력하면 입력 값을 실시간으로 출력하고 버튼을 클릭하면 출력된 값을 클래스를 토글하기

    ```javascript
    const textInput = document.querySelector('input')
    textInput.addEventListener('input', function (event) {
        const h1Tag = document.querySelector('h1')
        h1Tag.innerText = event.target.value
    })
      
    const btn = document.querySelector('#btn')
    btn.addEventListener('click', function (event) {
        const h1Tag = document.querySelector('h1')
        h1Tag.classList.toggle('blue')
    })
    ```

    

<br>

- #### Event 취소

  - event.preventDefault()
    - 현재 Event의 기본 동작을 중단
    - HTML 요소의 기본 동작은 작동하지 않게 막음
    - HTML 요소의 기본 동작 예시
      - a 태그 : 클릭 시 특정 주소로 이동
      - form 태그 : form 데이터 전송

<br>

- #### Event 취소 실습

  - 웹 페이지 내용을 복사하지 못하도록 하기

    ```javascript
    const h1Tag = document.querySelector('h1')
    h1Tag.addEventListener('copy', function(event) {
        event.preventDefault()
        alert('복사 할 수 없습니다.')
    })
    ```

<br>

- #### Event 종합 실습

  - 버튼을 클릭하면 랜덤 로또 번호를 6개 출력하기

    ```javascript
    const btn = document.querySelector('#lotto-btn')
    btn.addEventListener('click', function (event) {
        
        // 공이 들어갈 컨테이너 생성
        const ballContainer = document.createElement('div')
        ballContainer.classList.add('ball-container') // css 이미 작성 되어 있음!
        
        // 랜덤한 숫자 6개를 만들기
        const numbers = _.sampleSize(_.range(1, 46), 6)
        
        // 공 만들기
        numbers.forEach((number) => {
            const ball = document.createElement('div')
            ball.innerText = number
            ball.classList.add('ball')
            ball.style.backgroundColor = 'crimson'
            ballContainer.appendChild(ball)
        })
        
        // 공 컨테이너는 결과 영역의 자식으로 넣기
    	const resultDiv = document.querySelector('#result')
    	resultDiv.appendChild(ballContainer)
    })
    ```

  <br>

  - CREATE, READ 기능을 충족하는 today app 만들기

    ```javascript
    const formTag = document.querySelector('form')
    
    const addTodo = function (event) {
        event.preventDefault()
        
        // 입력값 가져오기
        const inputTag = document.querySelector('.inputData')
        const data = inputTag.value
    	
        if (data.trim()) {
        	// li 태그 생성
        	const liTag = document.createElement('li')
        	liTag.innerText = data
        
        	// ul 태그 선택 후 li 를 자식으로 등록
        	const ulTag = document.querySelector('ul')
        	ulTag.appendChild(liTag)
        
        	// 폼 리셋하기
        	event.target.reset()
        } else {
            alert('내용을 입력하세요!')
        }
    }
    formTag.addEventListener('submit', addTodo)
    ```

<br>

<br>

## this

<br>

- #### this

  - 어떠한 object를 가리키는 키워드
    - (java 에서의 this 와 python 에서의 self 는 인스턴스 자기자신을 가리킴)
  - JavaScript 의 함수는 호출될 때 this 를 암묵적으로 전달 받음
  - JavaScript 에서의 this 는 일반적인 프로그래밍 언어에서의 this 와 조금 다르게 동작
  - JavaScript 는 해당 **함수 호출 방식** 에 따라 this 에 바인딩 되는 객체가 달라짐
  - 즉, 함수를 선언할 때 this 에 객체가 결정되는 것이 아니고,
    함수를 호출할 때 **함수가 어떻게 호출 되었는지에 따라 동적으로 결정**됨

<br>

- #### this INDEX

  - 전역 문맥에서의 this
    - 브라우저의 전역 객체인 window를 가리킴
    - `console.log(this) // window`
  - 함수 문맥에서의 this
    - 단순 호출
      - 전역 객체를 가리킴
      - 전역은 브라우저에서는 window, Node.js 는 global을 의미함
    - Method (객체의 메서드로서)
    - Nested (Function 키워드)
      - forEach의 콜백 함수에서의 this가 메서드의 객체를 가리키지 못하고 전역 객체 window를 가리킴
      - 단순 호출 방식으로 사용되었기 때문
      - 이를 해결하기 위해 등장한 함수 표현식이 바로 **"화살표 함수"**
        - 화살표 함수는 자동으로 한 단계 상위의 scope context를 바인딩

<br>

- #### 화살표 함수

  - 화살표 함수는 호출의 위치와 상관없이 상위 스코프를 가리킴 (Lexical scope this)
  - **Lexical scope**
    - 함수를 어디서 호출하는지가 아니라 어디에 선언하였는지에 따라 결정
    - Static scope 라고도 하며 대부분의 프로그래밍 언어에서 따르는 방식
  - 따라서 함수 내의 함수 상황에서 **화살표 함수를 쓰는 것을 권장**

<br>

- #### this 와 addEventListener

  - 하지만...
    addEventListener 에서의 콜백 함수는 특별하게 function 키워드의 경우
    addEventListener 를 호출한 대상을 (event.target) 뜻함

  - 반면 화살표 함수의 경우 상위 스코프를 지칭하기 때문에 window 객체가 바인딩 됨

  - 결론

    - "addEventListener 의 콜백 함수는 function 키워드를 사용하기" 

      ```javascript
      // function
      console.log(this) // <button id="function">function</button>
      
      // 화살표 함수
      console.log(this) // window
      ```

      