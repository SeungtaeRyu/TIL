# 데이터 구조(Data Structure)



## 목차

- [**순서가 있는 데이터 구조**](#순서가-있는-데이터-구조)
  - 문자열

  - 리스트

  - 튜플

- [**비시퀀스형 데이터 구조**](#비시퀀스형-데이터-구조)
  - 셋

  - 딕셔너리

- [**얕은 복사와 깊은 복사**](#얕은-복사와-깊은-복사)



## 데이터 구조 활용

데이터 구조를 활용하기 위해서는 메서드(method)를 활용

- 메서드는 클래스 내부에 정의한 함수, 사실상 함수 동일
- 쉽게 설명하자만 객체의 기능(추후 객체 지향 프로그래밍에서 학습)
- `데이터구조.메서드()` 형태로 활용!
- 어렵게 느껴진다면, `주어.동사()` 



## 데이터 구조 활용 예시

- List.append(10)

- String.split()



## 파이썬 공식 문서의 표기법

- `str.replace(old, new[, count])`
  - `old`, `new`는 필수 / `[,count]`는 선택적 인자를 의믜함



## 순서가 있는 데이터 구조

### 1. 문자열

- 메모리 주소 확인

  ``` python
  word = 'ssafy'
  print(word) # ssafy
  print(id(word)) # 메모리 주소 확인 24~~
  
  word = 'test'
  print(word) # test
  print(id(word)) # 메모리 주소 확인 24~~
  
  # 새로운 값을 할당하면 기존 주소는 사라지고 새로운 주소가 주어진다!
  ```

  

#### 문자열 조회/탐색 및 검증 메서드

- `s.find(x)`: x의 첫 번째 index를 반환. 없으면, `-1`을 반환

- `s.index(x)`: x의 첫 번째 index를 반환. 없으면, **오류 발생**

- `s.isalpha()`: 알파벳 문자 여부(단순 알파벳이 아닌 유니코드 상 Letter(한국어도 포함))

- `s.isupper()`: 대문자 여부

- `s.islower()`: 소문자 여부

- `s.istitle()`: 타이틀 형식 여부

  ``` python
  # find
  print('apple'.find('p')) # 1
  print('apple'.find('k')) # -1
  
  # index
  print('apple'.index('p')) # 1
  print('apple'.index('k')) # ValueError: substring not found
  
  # isalpha
  print('abc'.isalpha()) # True
  print('ㄱㄴㄷ'.isalpha()) # True
  
  # isupper, islower
  print('Ab'.isupper()) # True
  print('ab'.islower()) # True
  
  # istitle
  print('Title Title!'.istitle()) # True
  
  # 첫 글자가 대문자고 나머지가 소문자인지 ??
  ```



#### 문자열 관련 검증 메서드

- `isdecimal() `: 숫자인지
- `isdigit()` : 소수점까지 보고 싶으면
- `isnumeric()` : 웬만하면 다 숫자



#### 문자열 변경 메서드(S는 문자열)

- `s.replace(old, new[,count])` : 바꿀 대상 글자를 새로운 글자로 바꿔서 반환

- `s.strip([chars])` : 공백이나 특정 문자를 제거

- `s.split(sep=None, maxsplit=-1)`

- `'separator'.join([iterable])` : 구분자로 iterable을 합침

- `s.capitalize()` : 가장 첫 번째 글자를 대문자로 변경

- `s.title()` : 첫 글자가 대문자인지?

- `s.upper()` : 대문자로

- `s.lower()` : 소문자로

- `s.swapcase()` : 대 ↔ 소문자 서로 변경

  ``` python
  # replace - count를 지정하면, 해당 개수만큼만 변환
  print('wooooowoo'.replace('o', '!', 2)) # w!!ooowoo
  
  # strip
  print('    와우!\n'.strip()) # 좌우 공백 제거
  print('    와우!\n'.lstrip()) # 왼쪽 공백 제거
  print('    와우!\n'.rstrip()) # 오른쪽 공백 제거
  print('안녕하세요????'.rstrip('?')) # '안녕하세요'
  
  # split
  print('a,b,c'.split(',')) 	# ['a', 'b', 'c']
  print('a b c'.split()) 		# ['a', 'b', 'c']
  print('서울시 강남구 00동'.split()[0])	# 서울시
  
  # 'separator'.join([iterable])
  print('!'.join('ssafy')) # 's!s!a!f!y'
  print(' '.join(['3', '5'])) # '3 5'
  
  
  msg = 'hI! Everyone, I\'m ssafy'
  print(msg)				# hI! Everyone, I'm ssafy
  print(msg.capitalize())	# Hi! everyone, i'm ssafy
  print(msg.title())		# Hi! Everyone, I'M Ssafy
  print(msg.upper())		# HI! EVERYONE, I'M SSAFY
  print(msg.lower())		# hi! everyone, i'm ssafy
  print(msg.swapcase())	# Hi! eVERYONE, i'M SSAFY
  ```





### 2. 리스트

#### 리스트 메서드

- `L.append(x)` : 리스트 마지막에 항목 x를 추가

- `L.insert(i, x)` : 리스트 인덱스 i에 항목 x를 삽입

- `L.remove(x)` : 리스트 가장 왼쪽에 있는 항목(첫 번째) x를 제거. **없으면 ValueError**

- `L.pop()` : 리스트 가장 오른쪽에 있는 항목(마지막)을 반환 후 제거

- `L.pop(i)` : 리스트 인덱스 i에 있는 항목을 반환 후 제거

- `L.extend(m)` : 순회형 m의 모든 항목들의 리스트 끝에 추가 (+=랑 같은 기능)

- `L.index(x, start, end)` : 리스트에 있는 항목 중 가장 왼쪽에 있는 항목 x의 인덱스를 반환

- `L.count(x)` : 리스트에서 항목 x가 몇 개 존재하는지 갯수를 반환

  ``` python
  # append
  cafe = ['stratbucks', 'tomntoms', 'hollys']
  print(cafe) # ['stratbucks', 'tomntoms', 'hollys']
  print(id(cate)) # 1466672629504
  cafe.append('banapresso')
  print(cafe) # ['stratbucks', 'tomntoms', 'hollys', 'banapresso']
  print(id(cate)) # 1466672629504
  # list에서는 주소가 바뀌지 않는다!
  
  # insert
  cafe. insert(0, 'start')
  print(cafe) # ['start', 'stratbucks', 'tomntoms', 'hollys', 'banapresso'] 
  cafe. insert(2, 'start')
  print(cafe) # ['stratbucks', 'tomntoms', 'start', 'hollys', 'banapresso'] 
  # start 인덱스가 리스트 index보다 크면 마지막에 들어감!
  
  # extend
  cafe.extend(['coffe'])
  print(cafe) # ['stratbucks', 'tomntoms', 'start', 'hollys', 'banapresso', 'coffe']
  cafe.extend('cup')
  print(cafe) # ['stratbucks', 'tomntoms', 'start', 'hollys', 'banapresso', 'coffe', 'c', 'u', 'p']
  
  # remove
  numbers = [1, 2, 3,'hi']
  numbers.remove('hi')
  print(numbers) # [1, 2, 3]
  numbers.remove('hi')
  print(numbers) # list.remove(x): x not in list
  
  # pop
  numbers = [1, 2, 3,'hi']
  word = numbers.pop()
  print(word) # hi
  print(numbers) # [1, 2, 3]
  
  # clear 
  numbers = [1, 2, 3,'hi']
  word = numbers.clear()
  print(numbers) # []
  
  # index
  numbers = [1, 2, 3, 4]
  print(numbers.index(4)) # 없을 시 Error 반환 
  
  # count
  numbers = [1, 2, 3, 1, 1, 1, 2, 2]
  print(numbers.count(1)) # 4
  print(numbers.count(100)) # 0
  ```



#### 정렬 관련 메서드

- `L.reverse()` : 리스트를 거꾸로 정렬

- `L.sort()` : 리스트를 정렬 (매개변수 이용가능)

  ``` python
  # sort()는 원본 리스트를 정렬. None 반환
  # sorted는 원본 리스트 그대로. 정렬된 리스트 반환
  numbers = [3, 2, 5, 8, 7]
  result = numbers.sort() # [2, 3, 5, 7, 8]
  print(numbers, result)  # None
  
  result = sorted(numbers)
  print(numbers, result)  # [3, 2, 5, 8, 7] [ 2, 3, 5, 7, 8]
  
  # reverse 정렬하는 것이 아님
  numbers = [3, 2, 5, 1]
  result = numbers.reverse()
  print(numbers, result) # [1, 5, 2, 3] None
  ```

  



### 3. 튜플

- 여러 개의 값을 순서가 있는 구조로 저장하고 싶을 때 사용

- 값을 변경할 수 없기 때문에 값에 영향을 미치지 않는 메서드만을 지원

- List 메서드 중 항목을 변경하는 메서드들을 제외하고 대부분 동일

  ``` python
  day_name = ('월', '화', '수', '목', '금')
  print(day_name[-3]) # 수
  print(day_name * 2) # ('월', '화', '수', '목', '금', '월', '화', '수', '목', '금')
  print(id(day_name)) # 2616448081328
  day_name += False, True
  print(day_name)		# ('월', '화', '수', '목', '금', False, True)
  print(id(day_name)) # 2616448511904
  
  # 튜플은 변경 전 후 주소가 동일하지 않다!
  ```

  

### 4. 멤버십 연산자(Membership Operator)

- `in`  : 있나요?

  ``` python
  print('apple' in 'a') # False
  print('a' in 'apple') # True
  print('hi' in 'hi I am ssafy') # True
  print('서순' in ['요까일엇무', '기러기']) # False
  ```

- `not in` : 없나요?



---



## 비시퀀스형 데이터 구조

### 1. 셋

- set이란 중복되는 요소가 없이, 순서에 상관없는 데이터들의 묶음
- 수학에서의 집합을 표현한 컨테이너
- 담고 있는 요소를 삽입 변경, 삭제 가능(가변 자료형)



#### 셋 메서드

- `s.copy()` : 셋의 얕은 복사본을 반환

- `s.add(x)` : 항목 x가 셋 s에 없다면 추가

- `s.pop()` : 셋 s에서 랜덤하게 항목을 반환하고 해당 항목을 제거. set이 비어 있을 경우 KeyError

- `s.remove(s)` : 항목 x를 셋 s에서 삭제. 존재하지 않을 경우 KeyError

- `s.discard(x)` : 항목 x가 셋 s에 있는 경우, 항목 x를 셋 s에서 삭제

- `s.update(t)` : 셋 t에 있는 모든 항목 중 셋 s에 없는 항목을 추가

- `s.clear()` : 모든 항목을 제거 

  ``` python
  # set는 순서 보장 x !!
  
  # add - set에 값을 추가
  a = {'사과', '바나나', '수박'}
  print(a)  # {'사과', '바나나', '수박'}
  a.add('딸기')
  print (a) # {'사과', '바나나', '딸기', '수박'}
  
  
  # update(*others) - 여러 값을 추가(겹치는 것 빼고)
  a = {'사과', '바나나', '수박'} 
  a.update(['딸기', '바나나', '참외'])
  print (a) # {'사과', '참외', '바나나', '딸기', '수박'} 
  
  # remove(elem) - set에서 삭제하고, 없으면 KeyError
  a.remove('딸기')
  print(a) # {'사과', '참외', '바나나', '수박'}
  a.remove('딸기') # KeyError
  
  # discard(elem) - remove와 동일하지만 Error가 발생하지 않음!
  
  # pop() - 임의의 원소를 제거해 반환
  
  # clear() - 모든 항목을 제거
  a = {'사과', '바나나', '수박'}
  a.clear()
  print(a) # set()
  ```



#### 집합 관련 함수

- `s.isdisjoint(t)` : 셋 s가 셋 t의 서로 같은 항목을 하나라도 갖고 있지 않은 경우, True 반환

- `s.issubset(t)` : 셋 s가 셋 t의 하위 셋인 경우, True 반환

- `s.issuperset(t)` : 셋 s가 셋 t의 상위 셋인 경우, True 반환 

  ``` python 
  a = {'사과', '바나나', '수박'}
  b = {'포도', '망고'}
  c = {'사과', '포도', '망고', '수박', '바나나'}
  
  print(a.isdisjoint(b))	# True	a와 b는 서로소인가?
  print(b.issubset(c))	# True	b가 c의 하위셋인가?
  print(a.issuperset(c))	# False	a가 c의 상위셋인가?
  ```

  



### 2. 딕셔너리

- 키-값(key-value) 쌍으로 이뤄진 자료형
- Dictionary의 키(key)
  - key는 변경 불가능한 테이터(immutable)만 활용 가능
  - string, integer, float, boolean, tuple, range
- 각 키의 값(values)
  - 어떤한 형태든 관계없음



#### 딕셔너리 메서드

- `d.clear()` : 모든 항목을 제거

- `d.copy()` : 딕셔너리 d의 얕은 복사본을 반환

- `d.keys()` : 딕셔너리 d의 모든 키를 담은 뷰를 반환

- `d.values()` : 딕셔너리 d의 모든 값를 담은 뷰를 반환

- `d.items()` : 딕셔너리 d의 모든 키-값 쌍을 담은 뷰를 반환

- `d.get(k)` : 키 k의 값을 반환하는데, 키 k가 딕셔너리 d에 없을 경우 None을 반환

- `d.get(k, v)` : 키 k의 값을 반환하는데, 키 k가 딕셔너리 d에 없을 경우 v를반환

- `d.pop(k)` : 키 k의 값을 반환하고 키 k인 항목을 딕셔너리 d에서 삭제하는데,

  ​					 키 k가 딕셔너리 d에 없을 경우 KeyError를 발생

- `d.pop(k, v)` : 키 k의 값을 반환하고 키 k인 항목을 딕셔너리 d에서 삭제하는데,

  ​					  	 키 k가 딕셔너리 d에 없을 경우 v를 반환

- `d.update([other])` : 딕셔너리 d의 값을 매핑하여 업데이트

  ``` python
  # pop()
  my_dict = {'apple': '사과', 'banana': '바나나'}
  data = my_dict.pop('apple')
  print(data, my_dict) # 사과, {'banana': '바나나'}
  data = my_dict.pop('apple') # KeyError: 'apple'
  data = my_dict.pop('apple', 0) # 0
  
  # update()
  my_dict = {'apple': '사', 'banana': '바나나'}
  my_dict.update(apple='사과')
  print(my_dict) # {'apple': '사과', 'banana': '바나나'}
  
  # for문 사용
  # keys()랑 같음
  for key in my_dict:	# key를 순회합니다
      print(key)		
  # values()
  for value in my_dict.values():	# values를 순회합니다
      print(value)
      
  # items()
  for key, value in my_dict.items():
      print(f'key: {key}, value: {value}')
  ```

  

---



## 얕은 복사와 깊은 복사

### 복사 방법

- 할당
- 얕은 복사
- 깊은 복사



### 할당

- 할당은 전형적인 얕은 복사!

- 대입 연산자 (`=`)를 통한 복사는 해당 객체에 대한 **객체 참조**를 복사

  ``` python
  list1 = [1, 2, 3]
  list2 = list1
  print(list1, list2) # [1, 2, 3] [1, 2, 3]
  
  list2[0] = 'hello'
  print(list1, list2) # ['hello', 2, 3] ['hello', 2, 3]
  ```



### 얕은 복사 해결법

- Slice 연산자 활용하여 같은 원소를 가진 리스트지만 연산된 결과를 복사

  ``` python
  a = [1, 2, 3]
  b = a[:]
  print(a, b) # [1, 2, 3] [1, 2, 3]
  b[0] = 5
  print(a, b) # [1, 2, 3] [5, 2, 3]
  ```

  

### 얕은 복사 주의사항

- 복사하는 리스트의 원소가 주소를 참조하는 경우 ex) 다중 리스트

  ``` python
  import copy
  a = [1, 2, ['a','b']]
  b = a[:]
  print(a, b)	# [1, 2, ['a', 'b']] [1, 2, ['a', 'b']]
  b[2][0] = 0
  print(a, b) # [1, 2, [0, 'b']] [1, 2, [0, 'b']]
  ```

  

### 모든 문제를 해결하기 위한 deepcopy!

``` python
import copy
a = [1, 2, ['a','b']]
b = copy.deepcopy(a)
print(a, b)	# [1, 2, ['a', 'b']] [1, 2, ['a', 'b']]
b[2][0] = 0
print(a, b) # [1, 2, ['a', 'b']] [1, 2, [0, 'b']]
```

