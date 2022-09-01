# Django 02

## Model

#### 1. 테이블 작성법

- models.py 폴더 수정

- python manage.py makemigrations

- python manage.py migrate

- pip install ipython djnago-extentions

- settings.py에 앱 등록 'django_extensions',

- pip freeze > requirements.txt

- python manage.py shell_plus   

#### 2. 데이터 생성

- article = Article()

- article = Article(title = '제목', content = '내용')

#### 3. 데이터 조회

- Article.objects.all()

- Article.objects.filter(content='django')

- Article.objectsfilter(content__contains='dj')

#### 4. 데이터 수정

- article = Article.objects.get(pk=1)

- article.title = 'byebye'

- article.save()

#### 5. 데이터 삭제

- article = Article.objects.get(pk=1)

- article.delete()

## 데이터 전송

- #### form method
  
  - form tag의 method 디폴트값은 GET 요청이다. 하지만 GET 요청을 url에 정보가 노출되기 떄문에 POST 방식을 쓴다. (CRUD 중 CUD를 POST 방식으로 씀)
  
  - POST 방식은 권한이 필요하기 때문에 `{% csrf_token %}` 태그가 없으면 Django 서버는 요청에 대해 403 forbidden error로 응답한다.

## admin 계정 생성

- python manage.py createsuperuser
  
  - username 입력
  
  - email 입력 - 선택사항이므로 입력하지 않고 enter도 가능
  
  - password 입력
  
  - admin.py 파일 작성   
    
    ```python
    from django.contrib import admin
    from .models import Article
    
    admin.site.register(Article)
    ```
