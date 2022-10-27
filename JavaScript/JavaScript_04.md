# JavaScript 04 

## 목차

- [동기와 비동기](#동기와-비동기)
- [JavaScript의 비동기 처리](#JavaScript-의-비동기-처리)
- [Axios 라이브러리](#Axios)
- [Callback과 Promise](#Callback-과-Promise)
- [AJAX](#AJAX)

<br>

<br>

## 동기와 비동기

- #### 동기(Synchronous)

  - 모든 일을 **순서대로** 하나씩 처리하는 것
  - 요청과 응답을 동기식으로 처리한다면?
    - 요청을 보내고 응답이 올때까지 기다렸다가 다음 로직을 처리

<br>

- #### 비동기(Asynchronous)

  - 작업을 시작한 후 **결과를 기다리지 않고** 다음 작업을 처리하는 것 (병렬적 수행)

  - 시간이 필요한 작업들은 요청을 보낸 뒤 응답이 빨리 오는 작업부터 처리

    ```Javascript
    function slowRequest(callBack) {
        console.log('1. 오래 걸리는 작업 시작 ...')
        setTimeout(function () {
            callBack()
        }, 3000)
    }
    
    function myCallBack () {
        console.log('2. 콜백함수 실행됨')
    }
    
    slowRequest(myCallBack)
    console.log('3. 다른 작업 실행')
    
    // 1. 오래 걸리는 작업 시작 ...
    // 2. 콜백함수 실행됨
    // 3. 다른 작업 실행
    ```

<br>

- #### 비동기를 사용하는 이유

  - 사용자 경험
    - **비동기로 처리한다면 먼저 처리되는 부분부터 보여줄 수 있으므로, **  <br>
      사용자 경험에 긍정적인 효과를 볼 수 있음

<br>

<br>

## JavaScript 의 비동기 처리

- #### JavaScript는 Single Thread 언어

  - JavaScript 자체는 Single Thread 이므로 비동기 처리를 할 수 있도록 도와주는 환경이 필요함

  - **비동기와 관련한 작업은 브라우저 또는 Node 환경에서 처리**

  - 이중에서 브라우저 환경에서의 비동기 동작은 크게 아래의 요소들로 구성됨
    1. JavaScript Engine 의 **Call Stack**
    2. **Web API**
    3. **Task Queue**
    4. **Event Loop**

<br>

- #### 비동기 처리 동작 방식

  - 브라우저 환경에서의 JavaScript 의 비동기는 아래와 같이 처리된다.
    1. 모든 작업은 Call Stack(LIFO)으로 들어간 후 처리된다.
    2. 오래 걸리는 작업이 Call Stack으로 들어오면 Web API로 보내서 처리하도록 한다.
    3. Web API에서 처리가 끝난 작업들은 TASK Queue(FIFO)에 순서대로 들어간다.
    4. Event Loop가 Call Stack이 비어 있는 것을 체크하고, <br>
       Task Queue 에서 가장 오래된 작업을 Call Stack으로 보낸다.

<br>

<br>

## Axios

- #### 개요

  - JavaScript의 HTTP 웹 통신을 위한 라이브러리
  - 확장 가능하나 인터페이스와 쉽게 사용할 수 있는 비동기 통신 기능을 제공
  - node 환경은 npm을 이용해서 설치 후 사용할 수 있고, <br>
    browser 환경을 CDN을 이용해서 사용할 수 있음
  - Axios 공식문서 및 github
    - https://axios-http.com/kr/docs/intro
    - https://github.com/axios/axios

<br>

- #### Axios 기본 구조

  - get, post 등 여러 method 사용가능

  - **then**을 이용해서 성공하면 수행할 로직을 작성

  - **catch**를 이용해서 실패하면 수행할 로직을 작성

    ```javascript
    axios.get(catImageSearchURL)
      .then((request) => {
        console.log(response.data)
      })
      .catch((error) => {
        console.log('실패했다옹')
      })
      console.log('야옹야옹')
    ```

  - 정리
    - axios는 비동기로 데이터 통신을 가능하게 하는 라이브러리
    - 같은 방식으로 우리가 배운 Django REST API 로 요청을 보내서 데이터를 받아온 후 처리할 수 있음

<br>

<br>

## Callback 과 Promise

- #### 콜백 함수 (Callback Function)

  - **다른 함수의 인자로 전달되는 함수**를 콜백 함수라고 한다
  - 비동기에만 사용되는 함수가 아니며 동기, 비동기 상관없이 사용 가능
  - 시간이 걸리는 **비동기 작업이 완료된 후 실행할 작업을 명시하는 데 사용**되는<br>
    콜백 함수를 **비동기 콜백(asynchronous callback)** 이라 부름

<br>

- #### 콜백 함수를 사용하는 이유

  - 명시적인 호출이 아닌 **특정한 조건 혹은 행동에 의해 호출**되도록 작성할 수 있음
  - **비동기 처리를 순차적으로 동작할 수 있게 함**
  - 비동기 처리를 위해서는 콜백 함수의 형태가 반드시 필요함

<br>

- #### 콜백 지옥

  - 비동기 코드를 작성하다 보면 콜백 함수로 인한 콜백 지옥은 반드시 나타나는 문제
    - 코드의 가독성을 해치고
    - 유지 보수가 어려워짐

<br>

<br>

- #### 프로미스(Promise)

  - "작업이 끝나면 실행 시켜줄게" 라는 약속
  - **비동기 작업의 완료 또는 실패를 나타내는 객체**
  - Promise 기반의 클라이언트가 바로 이전에 사용한 **Axios** 라이브러리!
    - **axios로 처리한 비동기 로직이 항상 promise 객체를 반환**
    - 그래서 then을 계속 이어 나가면서 작성할 수 있었던 것

<br>

- #### then (callback)

  - 요청한 작업이 성공하면 callback 실행
  - callback은 **이전 작업의 성공 결과를 인자로 전달 받음**

- #### catch (callback)

  - then()이 하나라도 실패하면 callback 실행
  - callback은 **이전 작업의 실패 객체를 인자로 전달 받음**

<br>

- #### Promise가 보장하는 것 (vs 비동기 콜백)

  1. 현재 실행 중인 Call Stack을 완료하기 이전에는 절대 호출되지 않음
  2. 비동기 작업이 성공 or 실패한 뒤 .then() 메서드를 이용하여 추가한 경우에도 1번과 똑같이 동작
  3. then()을 여러 번 사용하여 여러 개의 callback 함수를 추가할 수 있음 (Chaining)

<br>

<br>

## AJAX

- #### AJAX 의 특징

  - 비동기 통신 웹 개발 기술을 Asynchronous Javascript And XML (AJAX)라 함
  - 페이지 새로고침 없이 서버에 요청
  - 서버로부터 응답(데이터)을 받아 작업을 수행

<br>

