# Django 03 Form

<br>

## Form Class

#### Form Class 선언

- 앱 폴더에 forms.py 생성 후 선언
  
  ```python
  from django import forms
  
  class ArticleForm(forms.Form):
      title = forms.CharField(max_length=10)  # max_length 필수 아님
      content = forms.CharField()                # TextField는 없음!
  ```

- 앱 폴더에 views.py 파일에서 form 파일 import하고 context로 넘겨주기

- html 파일에서 `{{ form }}` 로 사용

- {{ form.as_p }} 를 사용하면 p tag로 감싸짐. (줄바꿈이 됨)

- {{ form.as_ul }}, {{ form.as_table }} 도 사용가능

- 유효성 검증 가능함

<br>

## Widgets

- 선언하기
  
  - input 요소의 단순히 렌더링만 할 뿐 유효성 검증 못함
  
  - Widgets은 반드시 form fields에 할당됨
    
    ```python
    content = forms.CharField(widget=forms.Textarea)
    ```

#### widgets 응용하기

- 드롭다운 만들기
  
  ```python
  # articles/forms.py
  from django import forms
  
  class ArticleForm(forms.Form):
      NATION_A = 'kr'                        # value를 변수에 저장하는 이유는
      NATION_B = 'ch'                        # 이게 장고의 권장 스타일 가이드이기 때문!
      NATION_C = 'jp'
      NATIONS_CHOICES = [
          (NATION_A, '한국'),               # 튜플의 첫번째 인자가 value가 됨!
          (NATION_B, '중국'),
          (NATION_C, '일본'),
      ]
      title = forms.CharField(max_length=10) 
      content = forms.CharField()    
      nation = forms.ChoiceField(choices=NATIONS_CHOICES, widget=forms.RadioSelect)
      # widget=forms.RadioSelect 체크박스로 바꾸기!
  ```

```
- Form fields 공식문서와 Widgets 공식문서를 참고하여 사용하기



<br>

## Django Model Form



#### ModelForm Class

- model을 통해 Form Class를 만들 수 있는 helper class
- form과 똑같은 방식으로 view 함수에서 사용



#### ModelForm 선언

- forms 라이브러리에서 파생된 ModelForm 클래스를 상속받음

- 정의한 ModelForm 클래스 안에 Meta 클래스를 선언

- 어떤 모델을 기반으로 form을 작성할 것인지에 대한 정보를 Meta 클래스에 지정

```python
# articles/forms.py

from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article            # 어떤 모델을 기반으로 할 지
        fields = '__all__'      # 모델필드 중 어떤것을 출력할 지
```

#### ModelForm 에서의 Meta Class

- ModelForm의 정보를 작성하는 곳

- ModelForm을 사용할 경우 참조 할 모델이 있어야 하는데 Meta class의 model 속성이 이를 구성함
  
  - 참조하는 모델에 정의된 field 정보를 Form에 적용함

- fields 속성에 `'__all__'`  를 사용하여 모델의 모든 필드를 포함할 수 있음

- 또는 exclude 속성을 사용하여 모델에서 포함하지 않을 필드를 정할 수 있음
  
  ```python
      class Meta:
          model = Article            
          exclude = ('title',)
  ```

#### ModelForm with view functions

1. CREATE
   
   - 유효성 검사를 통과하면 데이터 저장 후 상세 페이지로 리다이렉트
   
   - 통과하지 못하면 작성 페이지로 리다이렉트
     
     ```python
     # views.py
     def create(request):
         form = ArticleForm(request.POST)
         if form.is_valid():                    # 드디어 나온 유효성 검사
             article = form.save()            # save()는 저장된 객체를 반환까지도 해준대!
             return redirect('articles:detail', article.pk)
         return redirect('articles:new')
     ```

2. UPDATE
   
   - ModelForm의 하위 클래스는 키워드 인자 instance 여부를 통해 생성할 지, 수정할 지를 결정함
   
   - 제공되지 않은 경우 save()는 CREATE
   
   - 제공된 경우 save()는 UPDATE
     
     ```python
     # views.py
     def edit(request, pk):
        article = Article.objects.get(pk=pk)
        form = ArticleForm(instance=article)    # 여기 인스턴스 주면 form에 기존값 초기설정!
        context = {
            'article': article,
            'form': form,
        }
        return render(request, 'articles/edit.html', context)
     ```

     def update(request, pk):
         article = Article.objects.get(pk=pk)
         form = ArticleForm(request.POST, instance=article)    # 여기 instance가 수정부분!
         if form.is_valid():                    
             article = form.save()            
             return redirect('articles:detail', article.pk)
         context = {
             'article': article,
             'form': form,
         }
         return render(request, 'articles/edit.html', context)
     ```

3. ERROR
   
   - 유효성 검사 실패하면 error 도 같이 반환받아짐
   
   - html로 반환되는 게 신기하네요
     
     ```python
     # views.py
     def create(request):
         form = ArticleForm(request.POST)
         if form.is_valid():                    
             article = form.save()            
             return redirect('articles:detail', article.pk)
         # print(f'에러: {form.error})           # 에러도 반환해줌~ html 형식으로!
         context = {
             'form': form,
         }
         return render(request, 'articles/new.html', context) # 에러 메세지 돌려주기
     ```

#### Form과 ModelForm의 차이

- 역할이 다르니까 굳이 비교할 필요는 없음!
  - Form : DB와 연관되어 있지 않는 경우에 사용
  - ModelForm : 사용자로부터 받는 데이터가 DB와 연관되어 있는 경우에 사용

<br>

## ModelForm을 사용한  views.py 구조 수정

#### 1. new - create => create

```python
@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)
```

#### 2. edit - update => update

```python
@require_http_methods(['GET', 'POST'])
def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        # form = ArticleForm(data=request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm(instance=article)
    context = {
        'article': article,
        'form': form,
    }
    return render(request, 'articles/update.html', context)
```

<br>

## Decorator

#### Allowed HTTP methods

1. @require_http_methods()
   - View 함수가 특정한 요청 method만 허용하도록 하는 데코레이터
   - 예시) `@require_http_methods(['GET', 'POST'])`
2. @require_POST()
   - 포스트만 쓰는 Delete같은 곳에 사용
   - 데코레이터 쓰면 POST처리 안해도 됨
3. @require_safe()
   - GET 요청에 대한 Decorator
   - @require_GET이 있지만 @require_safe()를 권장
   - 요청 방법이 다를 경우 405 Method Not Allowed

<br>

## 마무리

- Django Form Class
  - Django 프로젝트의 주요 유효성 검사 도구
  - 공격 및 데이터 손상에 대한 중요한 방어 수단
  - 유효성 검사에 대해 개발자에게 강력한 편의를 제공

- View 함수 구조 변화
  - HTTP requests 처리에 따른 구조 변화
