# :sparkles:Django

#### 목차

1. [Django Intro](#1-Intro)

2. [Django 구조 이해하기 (MTV Design Pattern)](#2-Django-구조-이해하기)

3. Django Quick start

4. Django Template

5. Sending and Retrieving form data

6. Django URLs

7. 마무리



## 1. Intro

#### Django를 배워야하는 이유

1. Python으로 작성된 프레임워크

2. 수많은 여러 유용한 기능들

3. 검증된 웹 프레임워크
   
   - 화해, Toss, 두나무, 당근 마켓, 요기요 등



## 2. Django 구조 이해하기

#### Django에서의 디자인 패턴

- Django에 적용된 디자인 패턴은 **MTV 패턴**이다.

- MTV패턴은 **MVC 디자인 패턴**을 기반으로 조금 변형된 패턴이다.
  
  

#### MVC 소프트웨어 디자인 패턴

- MVC는 Model - View - Controller의 준말

- 데이터 및 논리 제어를 구현하는데 널리 사용되는 소프트웨어 디자인 패턴

- 하나의 큰 프로그램을 세가지 역할로 구분한 개발 방법론



1. Model : 데이터와 관련된 로직을 관리

2. View : 레이아웃과 화면을 처리

3. Controller : 명령을 model과 view 부분으로 연결

    

| MVC        | MTV      |
|:----------:|:--------:|
| Model      | Model    |
| View       | Template |
| Controller | View     |



#### MTV 디자인 패턴

- Model
  
  - MVC 패턴에서 Model의 역할에 해당
  
  - 데이터와 관련된 로직을 관리
  
  - 응용프로그램의 데이터 구조를 정의하고 데이터베이스의 기록을 관리

- Template
  
  - 레이아웃과 화면을 처리
  
  - 화면상의 사용자 인터페이스 구조와 레이아웃을 정의
  
  - MVC 패턴에서 View의 역할에 해당

- View
  
  - Model & Template과 관련한 로직을 처리해서 응답을 반환
  
  - 클라이언트의 요청에 대해 처리를 분기하는 역할
  
  - 동작 예시
    
    - 데이터가 필요하다면 mode에 접근해서 데이터를 가져오고 가져온 데이터를 template로 보내 화면을 구성하고 구성된 화면을 응답으로 만들어 클라이언트에 반환
  
  - MVC패턴에서 Controller의 역할에 해당

<img src="Django_01_assets/2022-08-30-09-49-38-image.png" title="" alt="" data-align="center">



#### 정리

- Django는 MTV 디자인 패턴을 가지고 있음
  
  - Model : 데이터 관련
  
  - Template : 화면 관련
  
  - View : Model & Template 중간 처리 및 응답 반환
