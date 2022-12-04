# Web : 그리드 시스템/반응협 웹

---

## 목차

- CSS Layout
  
  - float
  
  - flexbox
  
  - grid

- bootstrap
  
  - bootstrap grid system

- Responsive web

<br><br>CSS layout

### 1. Float

- 정의
  
  - 박스를 왼쪽 혹은 오른쪽으로 이동시켜 텍스트를 포함 인라인요소들이 주변을 wrapping 하도록 함
  
  - 요소가 Normal flow를 벗어나도록 함

- Float 속성
  
  - none : 기본값
  
  - left : 요소를 왼쪽으로 띄움
  
  - right : 요소를 오른쪽으로 띄움
    
    ```html
    <!DOCTYPE html>
    <html lang="en">
      <head>
        <meta charset="UTF-8" />
        <meta http-equiv="X-UA-Compatible" content="IE=edge" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>Document</title>
        <style>
          /* css 작성 */
          .box {
            width: 150px;
            height: 150px;
            border: 1px solid black;
            background-color: crimson;
            margin: 20px;
          }
          .left {
            float: left;
          }
          .right {
            float: right;
          }
        </style>
      </head>
      <body>
        <div class="box left">float left</div>
        <div class="box left">float left</div>
        <div class="box right">float right</div>
        <p>
          lorem
        </p>
      </body>
    </html>
    ```

<br>

### 2. Floxbox

- CSS Flexible Box Layout

  - 행과 열 형태로 아이템들을 배치하는 1차원 레이아웃 모델

  - 축
    
    - main axis (메인 축)
    
    - cross axis (교차 축)

  - 구성 요소
    
    - Flex Container (부모 요소)
    
    - Flex item (자식 요소)

  - 이전까지 Normal Flow를 벗어나는 수단은 Float 혹은 Position

- **Flex 속성**

  - **배치 설정**

    - **flex-direction**
      
      - Main axis : 기준 방향 설정
      
      - 역병향의 경우 HTML 태그 선언 순서와 시각적으로 다르니 유의 (웹 접근성에 영향)
        
        - `row` (default)
        
        - `row-reverse`
        
        - `column`
        
        - `column-reverse`

    - **flex-wrap**
      
      - 아이템이 컨테이너를 벗어나는 경우 해당 영역 내에 배치되도록 설정
        
        - `nowrap` : 한 줄에 배치
        
        - `wrap` : 넘치면 그 다음 줄로 배치
        
        - `wrap-reverse` : 

    - **flex-flow**
      
      - flex-direction 과 flex-wrap의 shorthand
      
      - flex-direction 과 flex-wrap에 대한 설정 값을 차례로 작성
      
      - 예시) flex-flow: row nowrap;

  - **공간 나누기**

    - **jusify-content (main axis)**
      
      - `flex-start` (default) : 123-
      
      - `flex-end` : -123
      
      - `center` : -123-
      
      - `space-between` : 1-2-3
      
      - `space-around` : -1--2--3-
      
      - `space-evenly` : -1-2-3-

    - **align-content (cross axis)**
      
      - `flex-start`
      
      - `flex-end`
      
      - `center`
      
      - `space-between`
      
      - `space-around`
      
      - `space-evenly`
      
      - `stretch`

  - **정렬**

    - **align-items (모든 아이템을 cross axis 기준으로)**
      
      - `flex-start`
      - `flex-end`
      - `center`
      - `baseline`
      - `stretch` (default)

    - **align-self (개별 아이템)**
      
      - 컨테이너 말고 직접적인 요소에 적용하면 됨!

  - Flex에 적용하는 속성

    - 기타 속성

      - `flex-grow` : 남은 영역을 아이템에 분배

      - `order` : 배치 순서


<br><br>

## Bootstrap

[Get started with Bootstrap · Bootstrap v5.2](https://getbootstrap.com/docs/5.2/getting-started/introduction/)

- ### spaceing
  
  - `{property}{sides}-{size}`
    
    - `{property}`
      
      - `m` : margin
      
      - `p` : padding
    
    - `{sides}`
      
      - `t` : top
      
      - `b` : bottom
      
      - `s` : left
      
      - `e` : right
      
      - `x` : 좌, 우
      
      - `y` : 상, 하
      
      - `black` : 전부 다
    
    - `{size}`
      
      - `0`
      
      - `1`
      
      - `2`
      
      - ...
      
      - `auto` : 양옆을 자동으로 채움
    
    - 팁
      
      - 1rem = 16px
      
      - m-1 → 0.25rem → 4px
      
      - m-2 → 0.5rem → 8px

- ### Color
  
  - `bg-primary`
  
  - `bg-secondary`
  
  - `bg-danger`
  
  - `text-success`
  
  - `text-danger`
  
  - `text-dark`

- ### Text
  
  - `fs` : font-size
  
  - `fw-bold` : 글씨 두껍게
  
  - `fw-normal`
  
  - `fw-light`
  
  - `text-start` 
  
  - `text-center` 
  
  - `text-end`
  
  - `text-decoration-none`
  
  - `fst-italic` : 폰트체 이탈릭

- ### Position
  
  - **property**
    
    - `position-static`
    
    - `position-relative`
    
    - `position-absolute` : 부모가 static이 아니어야 함
    
    - `position-fixed`
    
    - `position-sticky`
  
  - **같이 씀!**
    
    - `top`
    
    - `start`
    
    - `end`
    
    - `bottom`

- ### Display
  
  - `d-none`
  
  - `d-inline`
  
  - `d-inline-block`
  
  - `d-grid`
  
  - `d-table`
  
  - `d-table-cell`
  
  - `d-table-row`
  
  - `d-flex`
  
  - `d-inline-flex`
  
  - `d-sm-none` : 반응형
  
  - `d-md-none` : 반응형

- ### Form

- ### Components
  
  - Button
  
  - Dropdown
  
  - Navbar
  
  - Carousel
  
  - Modal : 중첩되어 사용하면 안됨 !! body레벨에서 사용하는 것 권장!!
  
  - Card

- ### Grid system
  
  - **기본 요소**
    
    - Column : 실제 컨텐츠를 포함하는 부분
    
    - Gutter : 칼럼과 칼럼 사이의 공간 (사이 간격)
    
    - Container : Column들을 담고 있는 공간
  
  - **반드시 기억해야 할 2가지!**
    
    - 12개의 column
    
    - 6개의 grid breakpoints
      
      - `xs` : > 576px
      
      - `sm` : ≥ 576px
      
      - `md` : ≥ 768px
      
      - `lg` : ≥ 992px
      
      - `xl` : ≥ 1200px
      
      - `xxl` : ≥ 1400px
  
  - offset - 공간을 비우고 싶을 때 사용!!
