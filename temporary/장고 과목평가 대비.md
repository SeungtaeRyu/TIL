# 장고 과목평가 대비

<br>

## 홈워크 정리

#### 0830_1

- MTV 의 역할

  <details markdown="1">
      <summary>정답</summary><br>
      Model(데이터베이스 관리) - Model <br>
      Template(인터페이스, 화면) - View <br>
      View(중심 컨트롤러) - Controller <br>
      <br>
  Model<br>
  - 응용프로그램의 데이터 구조를 정의하고 데이터베이스의 기록을 관리(추가, 수정, 삭제)
  <br><br>
  Template<br>
  - 파일의 구조나 레이아웃을 정의<br>
  - 실제 내용을 보여주는 데 사용(presentation)<br><br>
  View<br>
  - HTTP 요청을 수신하고 HTTP 응답을 반환<br>
  - Model을 통해 요청을 충족시키는데 필요한 데이터에 접근<br>
  - 그리고 탬플릿에게 응답의 서식 설정을 맡김

<br>

- __(a)__는 Django에서 URL 자체를 변수처럼 사용해서 동적으로 주소를 만드는 것을 의미한다. __(a)__는 무엇인지 작성하시오.

  <details markdown="1">
      <summary>정답</summary><br>
      Variable Routing



 <br>

- Django 프로젝트는 render할 template 파일들을 찾을 때, 기본적으로 settings.py에 등록된 각 앱 폴더 안의 __(a)__ 폴더 내부를 탐색한다. __(a)__에 들어갈 폴더 이름을 작성하시오.

  <details markdown="1">
      <summary>정답</summary><br>
      templates


 <br>

#### 0830_2

- 한국어로 번역하기 위해 setting.py에 어떤 변수를 어떤 값으로 할당해야 하는지 ?

  <details markdown="1">
      <summary>정답</summary><br>
      LANGUAGE_CODE = 'ko-kr'



 <br>

- 추가로 settings.py에 ‘이 변수‘가 활성화인 상태여야 1-1번 변수를 설정할 수 있다고 한 다. ‘이 변수’는 ?

  <details markdown="1">
      <summary>정답</summary><br>
      USE_I18N



 <br>

- 주소 ’/ssafy’로 요청이 들어왔을 때 실 행되는 함수가 pages 앱의 views.py 파일 안 ssafy 함수라면 path는?

  <details markdown="1">
      <summary>정답</summary><br>
      path('ssafy/', views.ssafy),



 <br>

- Django Template Language (DTL)

  1) menus 리스트를 반복문으로 출력하시오

     ```
     {% for __(a)__ in munus %}
     <p>{{ menu }}</p>
     {% endfor %}
     ```

     <details markdown="1">
         <summary>정답</summary><br>
         a : menu

  2) posts 리스트를 반목문을 활용하여 0번 글부터 출력하시오.

     ```
     {% for post in posts %}
     <p>{{ __(a)__}}번 글 : {{ post }}</p>
     {% endfor %}
     ```

     <details markdown="1">
         <summary>정답</summary><br>
         a : forloop.counter0

  3) users 리스트가 비어있다면 현재 가입한 유저가 없습니다. 텍스트를 출력하시오.

     ```
     {% for user in users %}
     <p>{{ user }}</p>
     {% __(a)__ %}
     <p>현재 가입한 유저가 없습니다.</p>
     {% endfor %}
     ```

     <details markdown="1">
         <summary>정답</summary><br>
         a : empty

  4) 첫 번째 반복문일 때와 아닐 때를 조건문으로 분기처리 하시오.

     ```
     {% __(a)__ forloop.first %}
     <p>첫 번째 반복문 입니다.</p>
     {% __(b)__ %}
     <p>첫 번째 반복문이 아닙니다.</p>
     {% __(c)__ %}
     ```

     <details markdown="1">
         <summary>정답</summary><br>
         a : if<br>
         b : else<br>
         c: endif

  5) 출력된 결과가 주석과 같아지도록 하시오.

     ```
     <!-- 글자 길이 : 5 -->
     <p>글자 길이 : {{ 'hello'| __(a)__ }}</p>
     <!-- My Name Is Tom -->
     <p>{{ 'my name is tom'| __(b)__ }}</p>
     ```

     <details markdown="1">
         <summary>정답</summary><br>
         a : length<br>
         b : title

  6) 변수 today에 datetime 객체가 들어있을 때 출력된 결과가 주석과 같아지도록 작성하시오.

     ```
     <!-- 2022년 08월 8일 (Mon) AM 10:02 -->
     <p>{{ today | date:"__(a)__" }}</p>
     ```

     <details markdown="1">
         <summary>정답</summary><br>
         a : Y년 m월 d일 (D) A h:i

 <br>

- Form tag with Django

  1. form 태그의 속성인 action의 역할에 대해 설명하시오.

     <details markdown="1">
         <summary>정답</summary><br>
         form 이 제출될 때 데이터를 보낼 경로를 지정한다.

  2. method가 가질 수 있는 속성 값을 작성하시오.

     <details markdown="1">
         <summary>정답</summary><br>
         GET <br>
         POST

  3. input 태그에 각각 `안녕하세요`, `반갑습니다`, `파이팅` 문자열을 넣고, submit 버튼을 눌렀을 때 이동하는 url 경로를 작성하시오.

     - action="/create/"
     - name 속성은 각각 title, content, my-site이다

     <details markdown="1">
         <summary>정답</summary><br>
         HOST:PORT/create/?title=안녕하세요&content=반갑습니다&my-site=파이팅

 <br> <br>

#### 0901

- models.py를 작성한 후 마이그레이션 작업을 위해 터미널에 작성해야 하는 두 개의 핵심 명령어는 ??

  <details markdown="1">
      <summary>정답</summary><br>
      $ python manage.py makemigrations<br>
  	$ python manage.py migrate


<br>

- 다음 중 새로운 Post를 저장하기 위하여 작성한 코드 중 옳지 않은 것을 고르시오.

  ```python
  # 1
  post = Post()
  post.title ='a'
  post.content = 'b'
  post.save()
  # 2
  post = Post(title='가', content='나')
  post.save()
  # 3
  post = Post('제목', '내용')
  post.save()
  # 4
  Post.objects.create(title='1', content='2')
  ```

  <details markdown="1">
      <summary>정답</summary><br>
      3번 => 인스턴트 생성 시, 필드 명을 함께 적어야 한다.


<br>

- Post가 10개 저장되어 있고 id의 값이 1부터 10까지라고 가정할 때 가장 첫 번째 Post를 가져오려고 한다. 다음 중 옳지 않은 코드를 고르시오

  ```
  # 1
  post1 = Post.objects.all()[0]
  # 2
  post1 = Post.objects.all()[-10]
  # 3
  post1 = Post.objects.all().first()
  # 4
  post1 = Post.objects.all().get(id=1)
  ```

  <details markdown="1">
      <summary>정답</summary><br>
      2번 => Negative indexing(음수 인덱싱) 지원하지 않음


<br>

- my_post 변수에 Post 객체 하나가 저장되어 있다. title을 “안녕하세요” content를 “반갑습니다” 로 수정하기 위한 코드를 작성하시오.

  <details markdown="1">
      <summary>정답</summary><br>
      my_post.title = '안녕하세요'<br>
  	my_post.content = '반갑습니다'<br>
  	my_post.save()


<br>

- 만들어진 모든 Post 데이터를 QuerySet형태로 반환하는 코드는?

  <details markdown="1">
      <summary>정답</summary><br>
      posts = Post.objects.all()

<br>

<br>

#### 0906

- 각 문항을 읽고 맞으면 T, 틀리면 F를 작성하시오.

  1. ModelForm을 사용할 때 Meta 클래스의 model 변수는 반드시 작성해야 한다.

  2. ModelForm을 사용할 때 사용자의 입력을 위해 페이지에 렌더링 되는 input element 의 속성은 Django에서 제공 해주는 대로만 사용해야 한다.

  3. 화면에 나타나는 각 element 위치는 html에서 form.as_p()를 사용하지 않고, 직접 위치시킬 수 있다.

     <details markdown="1">
         <summary>정답</summary><br>
         1. (T) ModelForm을 사용할 때 Meta 클래스의 model 변수는 반드시 작성해야 한다.<br>
         2. (F) ModelForm을 사용할 때 사용자의 입력을 위해 페이지에 렌더링 되는 input element의 속성은 Django에서 제공 해주는 대로만 사용해야 한다.<br>
         3. (T) Rendering fields manually 혹은 Looping over the form’s fields ({% for %})를 사용하면 각각의 element 위치를 수동으로 변경할 수 있다.

<br>

- 다음 빈칸 (a) ~ (d) 에 적합한 코드를 작성하시오.

  ```python
  from django import __(a)__
  from .models import Article
  
  class ArticleForm(__(b)__):
      
      class Meta:
          model = __(c)__
          __(d)__ = '__all__'
  ```

  <details markdown="1">
      <summary>정답</summary><br>
      (a) : forms<br>
  	(b) : forms.ModelForm<br>
  	(c) : Article<br>
  	(d) : fields

<br>

<br>

#### 0907

- Django 공식 github에서 User 모델이 정의된 코드를 찾아본 후 우리가 User 모델을 대체 시 AbstractUser를 상속 받는 부모 클래스로 설정한 이유를 작성해보시오.

  <details markdown="1">
      <summary>정답</summary><br>
      AbstractUser 가 User 를 정의하기 위한 코드를 가지고 있는 클래스 이기 때문


<br>

- 새 유저를 생성하기 위해서 Django 내부에 정의된 ModelForm을 사용하려 한다. 이 때 유저 생성 form을 사용하기 위해 작성하는 import 구문을 적으시오.

  <details markdown="1">
      <summary>정답</summary><br>
      from django.contrib.auth.forms import UserCreationForm


<br>

- Django는 사용자가 로그인에 성공할 경우 (a) 테이블에 세션 데이터를 저장한다. 그리고 브라우저의 쿠키에 세션 값이 발급되는데 이 세션 값의 key 이름은 (b)다. (a)와 (b)에 알맞은 값을 작성하시오.

  <details markdown="1">
      <summary>정답</summary><br>
      (a) : django_session<br>
  	(b) : sessionid

<br><br>

### 0908

- 단순히 사용자가 ‘로그인 된 사용자인지’만을 확인하기 위하여 사용하는 속성의 이름을 작성 하시오. (User 모델 내부에 정의되어 있음)

  <details markdown="1">
      <summary>정답</summary><br>
      is_authenticated


<br>

- 다음은 로그인 기능을 구현한 코드이다. 빈 칸에 들어갈 코드를 작성하시오.

  ```python
  from django.contfib.auth.forms import __(a)__
  from django.contrib.auth import __(b)__ as auth_login
  
  def login(request):
      if request.method == 'POST':
          form = __(a)__(request, request.POST)
          if form.is_vaild():
              auth_login(request, __(c)__)
              return redirect('accounts:index')
      else:
          form = __(a)__()
      context = {
          'form': form,
      }
      return render(request, 'accounts/login.html', context)
  ```

  <details markdown="1">
      <summary>정답</summary><br>
      (a) : AuthenticationForm<br>
      (b) : login<br>
      (c) :  form.get_user()


<br>

- 로그인을 하지 않았을 경우 template에서 user 변수를 출력했을 때 나오는 클래스의 이름을 작성하시오.

  <details markdown="1">
      <summary>정답</summary><br>
      AnonymousUser


<br>

- Django에서 기본적으로 User 객체의 password 저장에 사용하는 알고리즘, 그리고 함께 사용된 해시 함수를 찾아서 작성하시오.

  <details markdown="1">
      <summary>정답</summary><br>
      알고리즘: PBKDF2<br>
      해시함수: SHA256


<br>

- 로그아웃 기능을 구현하기 위하여 다음과 같이 코드를 작성하였다. 로그아웃 기능을 실행 시 문제가 발생한다고 할 때 그 이유와 해결 방법을 작성하시오

  ```python
  def logout(request):
      logout(request)
      return redirect('accounts:login')
  ```

  <details markdown="1">
      <summary>정답</summary><br>
      이유: views 파일의 함수 이름이 logout 함수의 이름과 같아서 충돌이 일어난다.<br><br>
  	해결방법: import의 이름을 바꿔준다 <br>
      from django.contrib.auth import logout as auth_logout

<br>

<br>

## 나올만한거 정리

- 프로젝트 시작할 때 명령어들은 ?

  <details markdown="1">
      <summary>정답</summary><br>
  $ mkdir 00_django_intro : 폴더 생성 <br>
  $ cd 00_django_intro : 폴더로 이동 <br>
  $ python -m venv [venv] : 가상환경 생성<br>
  $ source [venv]/scripts/activate : 가상환경 접속<br>
  $ pip install django==3.2.13 : 가상환경 접속 후 장고 설치<br>
  $ pip freeze > requirements.txt : pip 설치 목록 반영<br>
  $ pip install -r requirements.txt : 적혀있는 pip 설치<br>
  $ django-admin startproject [firstpjt] . : 프로젝트 생성<br>
  $ python manage.py startapp articles : 앱 생성<br>
  settings.py -> INSTALLED_APPS 안에 'articles', : 앱 등록<br>
  $ python manage.py runserver : 프로젝트 서버 실행<br>

<br>

- base.html 설정하려면 settings.py 에서 바꿔야 할 것은 ?

  <details markdown="1">
      <summary>정답</summary><br>
  	'DIRS': [BASE_DIR / 'templates',],


<br>

- 프로젝트 urls.py 에서 app의 urls.py로 넘겨주기 위한 path 등록방법은 ?

  <details markdown="1">
      <summary>정답</summary><br>
      from django.contrib import admin<br>
      from django.urls import path, include<br>
      <pre>
  urlpatterns = [
  	path('admin/', admin.site.urls),
      path('articles/', include('articles.urls')),
      path('pages/', include('pages.urls')),
  ]
  </pre>


<br>

- url 자체를 변수로 사용하기 위해 설정해야 하는 것은 ?

  <details markdown="1">
      <summary>정답</summary><br>
      app_name 등록 후 path에 name 속성 지정<br>
  	<pre>
  app_name = 'articles'
  urlpatterns = [
  	path('index/', views.index, name='index'),
  	path('greeting/', views.greeting, name='greeting'),
  	path('dinner/', views.dinner, name='dinner'),
  	path('throw/', views.throw, name='throw'),
  	path('catch/', views.catch, name='catch'),
  	path('hello/<str:name>/', views.hello, name='hello'),
  ]
  </pre>


<br>

- render 함수의 인자는 ?

  <details markdown="1">
      <summary>정답</summary><br>
  	첫번째 : request<br>
      두번째 : template_name<br>
      세번째 : context<br><br>
      [참고]<br>
      context 는 dictionary 형태로 저장 후 인자에 넘겨줌<br>
      ex) 'name' : name, 


<br>

- redirect 함수의 인자는 ?

  <details markdown="1">
      <summary>정답</summary><br>
  	첫번째 : URL 주소<br><br>
      [참고]<br>
      URL 변수 이름 사용 가능<br>
      데이터가 필요한 URL에는 데이터 변수도 함께 넘겨주기 가능

<br>

- url 태그에 인자 보내는 법은 ?

  <details markdown="1">
      <summary>정답</summary><br>
  	"{% url 'articles:detail' article.pk %}"

<br>

- url 주소에 인자 받는 법은 ?

  ```
  ex) path('<pk>/', views.detail, name='detail'),<br>
  ex) path('<int:pk>/', views.detail, name='detail'),<br>
  ex) path('<int:pk>/<int:id>/', views.detail, name='detail'),
  ```

  접기/펼치기가 html 파일이라 <> 안쪽 내용이 사라짐 ,,,

<br>

- POST 요청에 발급받아야 하는 토큰은?

  <details markdown="1">
      <summary>정답</summary><br>
  	form 태그 안에 {% csrf_token %} 을 받급받는다.<br><br>
      [참고]<br>
  	토큰을 받급받지 않으면 403 forbidden 에러가 발생한다.

<br>

- Model field 속성들 ?

  <details markdown="1">
      <summary>정답</summary><br>
      😁 : 썼던거 체크 <br>
  models.BinaryField()<br>
  models.BooleanField()<br>
  models.NullBooleanField()<br>
  models.DateField()😁<br>
  models.TimeField()<br>
  models.DateTimeField()😁<br>
  models.DurationField()<br>
  models.AutoField()<br>
  models.BigIntegerField()<br>
  models.DecimalField(decimal_places=X,max_digits=Y)<br>
  models.FloatField()<br>
  models.IntegerField()<br>
  models.PositiveIntegerField()<br>
  models.PositiveSmallIntegerField()<br>
  options.SmallIntegerField()<br>
  models.CharField(max_length=N)😁<br>
  models.TextField()😁<br>
  models.CommaSeparatedIntegerField(max_length=50)<br>
  models.EmailField()<br>
  models.FileField()<br>
  models.FilePathField()<br>
  models.ImageField()<br>
  models.GenericIPAddressField()<br>
  models.SlugField()<br>
  models.URLField()<br>
  models.UUIDField()<br>

<br>

- create_at / updated_at 필드 속성 차이는 ?

  <details markdown="1">
      <summary>정답</summary><br>
  	created_at = models.DateTimeField(auto_now_add=True)<br>
      updated_at = models.DateTimeField(auto_now=True)<br><br>
      auto_now_add => 최초생성 할때만 => created_at<br>
  	auto_now => 최초생성, 수정 할때마다 => updated_at 

<br>

- HTTP의 특징은 ?

  <details markdown="1">
      <summary>정답</summary><br>
  	1. 비 연결 지향<br>
      서버는 요청에 대한 응답을 보낸 후 연결을 끊음<br><br>
      2. 무상태<br>
      연결을 끊는 순간 클라이언트와 서버 간의 통신이 끝나며 상태 정보가 유지되지 않음  

<br>

- 쿠키 사용 목적은 ?

  <details markdown="1">
      <summary>정답</summary><br>
  	1. 세션 관리<br>
      로그인, 아이디 자동완성, 공지 하루 안 보기, 팝업체크, 장바구니 등의 정보 관리<br><br>
      2. 개인화<br>
      사용자 선호, 테마 등의 설정 <br><br>
      3. 트래킹<br>
      사용자 행동을 기록 및 분석

<br>

- Form class 사용방법 1. forms.py

  <details markdown="1">
      <summary>정답</summary><br>
  	1. 임폴트 선언<br>
      from django import forms<br><br>
      2. 클래스 정의(상속)<br>
      class ArticleForm(forms.Form)<br><br>
      3. fields 정의<br>
      title = forms.CharField(max_length=10)  	# max_length 필수 아님<br>
      content = forms.CharField()                	# TextField는 없음!<br><br>
      [참고]<br>
      1. forms.Form 중요<br>
      2. TextField 없는거 

<br>

- Form class 사용방법 2. views.py

  <details markdown="1">
      <summary>정답</summary><br>
  	1. 임폴트 선언<br>
      from .forms import ArticleForm<br><br>
      2. form 생성 후 context에 등록 <br>
      form = ArticleForm()<br>
      context = {<br>
      &nbsp; 'form': form,<br>
      }<br><br>

<br>

- Form class 사용방법 3. html

  <details markdown="1">
      <summary>정답</summary><br>
  	1. form 태그 안에 {{ form }} 입력<br><br>
      2. input마다 줄바꿈을 하고 싶으면 {{ form.as_p }} 입력<br>

<br>

- Form class 유효성 검사 방법

  <details markdown="1">
      <summary>정답</summary><br>
  	if form.is_valid():

<br>

- ModelForm 사용방법 

  <details markdown="1">
      <summary>정답</summary><br>
  	1. 임폴트 선언<br>
      from django import forms<br><br>
      2. 클래스 정의(상속)<br>
      class ArticleForm(forms.ModelForm)<br><br>
      3. meta 클래스 정의<br>
      class Meta:<br>
      &nbsp;&nbsp;&nbsp;&nbsp;model = Article<br>
      &nbsp;&nbsp;&nbsp;&nbsp;fields = '__all__'<br><br>
      [참고]<br>
      1. forms.ModelForm 중요<br>
      2. Models.py를 참조하기 때문에 TextField 자동으로 됨<br>
      3. fields의 __all__ 속성은 DB Table의 모든 field를 받아옴<br>
      4. 또는 exclude 속성을 사용하여 모델에서 포함하지 않을 필드를 정할 수 있음<br>
      &nbsp;&nbsp;&nbsp;&nbsp;ex) exclude = ('title',)

<br>

