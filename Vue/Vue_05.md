# Vue 05

<br>

## 목차

- [Vue with DRF](#Vue-with-DRF)
- [CORS](#CORS)
- DRF Auth System
- DRF Auth with Vue
- DRF-spectacular

<br><br>

## Vue with DRF

- #### Server & Client

  - Server
    - DB와 통신하며 데이터를 생성, 조회, 수정, 삭제를 담당
    - 요청을 보낸 Client에게 정상적인 요청이었다면 처리한 결과를 응답
  - Client
    - Server가 정의한 방식대로 정보(데이터)를 요청
    - 응답 받은 정보를 가공하여 화면에 표현

<br><br>

## CORS

- #### Cross-Origin Resource Sharing

  - **What Happened?**
    - 서버는 제대로 응답을 주었지만 브라우저가 막은 것
    - 보안상의 이유로 브라우저는 **동일 출처 정책(SOP)** 에 의해 다른 출처의 리소스와 상호작용 하는 것을 제한함
  - **CORS - 교차 출처 리소스 공유**
    - 추가 **HTTP Header** 를 사용하여, 특정 출처에서 실행 중인 웹 어플리케이션이<br>**다른 출처의 자원에 접근할 수 있는 권한** 을 부여하도록 브라우저에 알려주는 체제

<br>

- #### How to set CORS

  1. 라이브러리 설치

     - `$ pip install django-cors-headers`
     - `$ pip freeze > requirements.txt`

  2. App 추가 및 MIDDLEWARE 추가 주석 해제

     - :warning: 주의) CorsMiddleware 는 가능한 CommonMiddleware 보다 먼저 정의되어야 함

     - ```python
       INSTALLED_APPS = [
       	...
       	# CORS policy
       	'corsheaders',
       	...
       ]
       ```

     - ```python
       MIDDLEWARE = [
           ...    
           "corsheaders.middleware.CorsMiddleware",
           'django.middleware.common.CommonMiddleware',
       	...    
       ]
       ```

  3. **CORS_ALLOWED_ORIGINS** 에 교차 출처 자원 공유를 허용할 Domain 등록

     - ```python
       CORS_ALLOWED_ORIGINS = [
           'http://localhost:8080',
       ]
       ```

     - ```python
       CORS_ALLOWED_ALL_ORIGINS = True # 모든 Origin을 허용하고 싶으면
       ```

