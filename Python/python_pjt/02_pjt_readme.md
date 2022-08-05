# PJT 02

### 이번 pjt 를 통해 배운 내용

* api에 get요청을 보내는 방법 재미있었습니다!



## A. 인기 영화 조회 (problem_a)

### 1. 요구 사항 

* requests 라이브러리를 사용하여 TMDB에서 현재 인기있는 영화 목록 (Get Popular) 데이터를 요청합니다

* 응답 받은 데이터의 영화 개수를 반환하는 함수 popular_count를 작성합니다.




### 2. 풀이 코드

``` python 
import requests

def popular_count():
    URL = 'https://api.themoviedb.org/3/movie/popular?api_key=8d8e9b9672f4d1a183be6806ad451223&language=ko-KR'  # 발급받은 key로 인기 영화 순위 URL 주소 저장
    response = requests.get(URL).json()         # requests한 response.body를 파이썬에서 알아볼 형태로 변환
    poplular_movies = response.get('results')   # 영화 리스트가 들어있는 results만 변수에 저장

    return len(poplular_movies) # 영화 리스트 길이 반환



# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
```



### 3. 결과 화면

```python
# 20
```



### 4. 내가 생각하는 이 문제의 포인트

* 파이썬에서 api 응답을 받는 방식을 알게되었습니다.
* 데이터를 요청할 기관에 키 발급 요청을 하는 게 중요할 것 같습니다.

-----

## B. 특정 조건에 맞는 인기 영화 조회 1  (problem_b)

#### 1. 요구 사항 

* TMDB에서 현재 인기있는 영화 목록(Get Popular) 데이터를 요청합니다

* 응답 받은 데이터 중 평점(vote_average)이 8점 이상인 영화 목록을 반환하는 함수 vote_average_movies를 작성합니다.



### 2. 풀이 코드

``` python 
import requests
from pprint import pprint


def vote_average_movies():
    # problem_a에서 설명한 requests 읽기
    URL = 'https://api.themoviedb.org/3/movie/popular?api_key=8d8e9b9672f4d1a183be6806ad451223&language=ko-KR'
    response = requests.get(URL).json()
    poplular_movies = response.get('results')

    # 인기 영화 리스트의 요소들로 반복문을 동작하여 평점이 8.0 이상일 때 반환 리스트에 추가
    over_vote_average_movies = []
    for movie in poplular_movies:
      if movie.get('vote_average') >= 8.0:
        over_vote_average_movies.append(movie)

    # 반환리스트 반환
    return over_vote_average_movies


if __name__ == '__main__':
    pprint(vote_average_movies())
   
```



### 3. 결과 화면

``` python
"""
[{'adult': False,
  'backdrop_path': '/odJ4hx6g6vBt4lBWKFD1tI8WS4x.jpg',
  'genre_ids': [28, 18],
  'id': 361743,
  'original_language': 'en',
  'original_title': 'Top Gun: Maverick',
  'overview': '최고의 파일럿이자 전설적인 인물 매버릭은 자신이 졸업한 훈련학교 교관으로 발탁된다. 그의 명성을 모르던 팀원들은 '
              '매버릭의 지시를 무시하지만 실전을 방불케 하는 상공 훈련에서 눈으로 봐도 믿기 힘든 전설적인 조종 실력에 모두가 '
              '압도된다. 매버릭의 지휘 아래 견고한 팀워크를 쌓아가던 팀원들에게 국경을 뛰어넘는 위험한 임무가 주어지자 매버릭은 '
              '자신이 가르친 동료들과 함께 마지막이 될지 모를 하늘 위 비행에 나서는데…',
  'popularity': 6087.102,
  'poster_path': '/jMLiTgCo0vXJuwMzZGoNOUPfuj7.jpg',
  'release_date': '2022-05-24',
  'title': '탑건: 매버릭',
  'video': False,
  'vote_average': 8.3,
  'vote_count': 1714},
 {'adult': False,
  'backdrop_path': '/AfvIjhDu9p64jKcmohS4hsPG95Q.jpg',
  'genre_ids': [27, 53],
  'id': 756999,
  'original_language': 'en',
  'original_title': 'The Black Phone',
  'overview': '1978년 덴버 작은 마을, 아동연쇄납치살인범에게 납치된 소년이 초자연적인 현상을 겪으며 탈출을 위한 사투를 '
              '벌인다는 내용의 영화',
  'popularity': 3929.773,
  'poster_path': '/p9ZUzCyy9wRTDuuQexkQ78R2BgF.jpg',
  'release_date': '2022-06-22',
  'title': '블랙폰',
  'video': False,
  'vote_average': 8,
  'vote_count': 1207},
 {'adult': False,
  'backdrop_path': '/ocUp7DJBIc8VJgLEw1prcyK1dYv.jpg',
  'genre_ids': [28, 12, 878],
  'id': 634649,
  'original_language': 'en',
  'original_title': 'Spider-Man: No Way Home',
  'overview': '미스테리오의 계략으로 세상에 정체가 탄로난 스파이더맨 피터 파커는 하루 아침에 평범한 일상을 잃게 된다. 문제를 '
              '해결하기 위해 닥터 스트레인지를 찾아가 도움을 청하지만 뜻하지 않게 멀티버스가 열리면서 각기 다른 차원의 '
              '불청객들이 나타난다. 닥터 옥토퍼스를 비롯해 스파이더맨에게 깊은 원한을 가진 숙적들의 강력한 공격에 피터 파커는 '
              '사상 최악의 위기를 맞게 되는데…',
  'popularity': 1587.421,
  'poster_path': '/voddFVdjUoAtfoZZp2RUmuZILDI.jpg',
  'release_date': '2021-12-15',
  'title': '스파이더맨: 노 웨이 홈',
  'video': False,
  'vote_average': 8.1,
  'vote_count': 14355}]
"""
```



### 4. 내가 생각하는 이 문제의 포인트

* 요청받은 json 데이터를 파이썬 형식으로 가공하여 원하는 데이터에 접근하는 방법!

-----

## C. 특정 조건에 맞는 인기 영화 조회 2 (problem_c)

### 1. 요구 사항 

* TMDB에서 현재 인기있는 영화 목록(Get Popular) 데이터를 요청합니다.

* 응답 받은 데이터 중 평점(vote_average)을 기준으로 평점이 높은 영화 5개릐 정보를 리스트로 반환하는 함수 ranking을 작성합니다.

* sort 메서드 혹은 sorted 함수의 특정 파라미터를 이용합니다.



### 2. 풀이 코드

``` python 
import requests
from pprint import pprint


def ranking():
    # problem_a에서 설명한 requests 읽기
    URL = 'https://api.themoviedb.org/3/movie/popular?api_key=8d8e9b9672f4d1a183be6806ad451223&language=ko-KR'
    response = requests.get(URL).json()
    poplular_movies = response.get('results')

    
    score_index_list = []                               # 점수와 인덱스를 같이 저장할 리스트
    for i in range(len(poplular_movies)):               # 인기 영화 리스트 길이만큼 반복문 동작
      score = poplular_movies[i].get('vote_average')    # 인기영화[인덱스]의 평점을 scroe에 저장
      score_index_list.append((score, i))               # 점수와 인덱스를 튜플로 리스트에 append!

    score_index_list.sort(reverse=True)                 # 저장된 리스트를 평점순으로 정렬! (인덱스도 따라서 정렬 됨)

    top_5_movies = []   # 평점 TOP 5 영화를 저장할 리스트
    for i in range(5):  # 5번 만큼 반복
      top_5_movies.append(poplular_movies[score_index_list[i][1]]) # 정렬된 평점순 리스트의 인덱스를 꺼내어 인기영화[인덱스]로 반환리스트에 append!

    return top_5_movies
    # 여기에 코드를 작성합니다.  


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    pprint(ranking())
```



### 3. 풀이 코드

``` python
"""
[{'adult': False,
  'backdrop_path': '/odJ4hx6g6vBt4lBWKFD1tI8WS4x.jpg',
  'genre_ids': [28, 18],
  'id': 361743,
  'original_language': 'en',
  'original_title': 'Top Gun: Maverick',
  'overview': '최고의 파일럿이자 전설적인 인물 매버릭은 자신이 졸업한 훈련학교 교관으로 발탁된다. 그의 명성을 모르던 팀원들은 '
              '매버릭의 지시를 무시하지만 실전을 방불케 하는 상공 훈련에서 눈으로 봐도 믿기 힘든 전설적인 조종 실력에 모두가 '
              '압도된다. 매버릭의 지휘 아래 견고한 팀워크를 쌓아가던 팀원들에게 국경을 뛰어넘는 위험한 임무가 주어지자 매버릭은 '
              '자신이 가르친 동료들과 함께 마지막이 될지 모를 하늘 위 비행에 나서는데…',
  'popularity': 6087.102,
  'poster_path': '/jMLiTgCo0vXJuwMzZGoNOUPfuj7.jpg',
  'release_date': '2022-05-24',
  'title': '탑건: 매버릭',
  'video': False,
  'vote_average': 8.3,
  'vote_count': 1714},
 {'adult': False,
  'backdrop_path': '/ocUp7DJBIc8VJgLEw1prcyK1dYv.jpg',
  'genre_ids': [28, 12, 878],
  'id': 634649,
  'original_language': 'en',
  'original_title': 'Spider-Man: No Way Home',
  'overview': '미스테리오의 계략으로 세상에 정체가 탄로난 스파이더맨 피터 파커는 하루 아침에 평범한 일상을 잃게 된다. 문제를 '
              '해결하기 위해 닥터 스트레인지를 찾아가 도움을 청하지만 뜻하지 않게 멀티버스가 열리면서 각기 다른 차원의 '
              '불청객들이 나타난다. 닥터 옥토퍼스를 비롯해 스파이더맨에게 깊은 원한을 가진 숙적들의 강력한 공격에 피터 파커는 '
              '사상 최악의 위기를 맞게 되는데…',
  'popularity': 1587.421,
  'poster_path': '/voddFVdjUoAtfoZZp2RUmuZILDI.jpg',
  'release_date': '2021-12-15',
  'title': '스파이더맨: 노 웨이 홈',
  'video': False,
  'vote_average': 8.1,
  'vote_count': 14355},
 {'adult': False,
  'backdrop_path': '/AfvIjhDu9p64jKcmohS4hsPG95Q.jpg',
  'genre_ids': [27, 53],
  'id': 756999,
  'original_language': 'en',
  'original_title': 'The Black Phone',
  'overview': '1978년 덴버 작은 마을, 아동연쇄납치살인범에게 납치된 소년이 초자연적인 현상을 겪으며 탈출을 위한 사투를 '
              '벌인다는 내용의 영화',
  'popularity': 3929.773,
  'poster_path': '/p9ZUzCyy9wRTDuuQexkQ78R2BgF.jpg',
  'release_date': '2022-06-22',
  'title': '블랙폰',
  'video': False,
  'vote_average': 8,
  'vote_count': 1207},
 {'adult': False,
  'backdrop_path': '/wUwizGzbTk5CTiKBnE4Pq1MONwD.jpg',
  'genre_ids': [16, 12, 10751, 14],
  'id': 560057,
  'original_language': 'en',
  'original_title': 'The Sea Beast',
  'overview': '전설적인 바다 괴물 사냥꾼의 배에 여자아이가 몰래 숨어든다. 이제 한배에 탄 둘은 미지의 바다를 향해 대장정의 '
              '항해를 떠나는데. 이들은 어떤 역사를 쓰게 될까.',
  'popularity': 1350.484,
  'poster_path': '/axtQ6KM40hpwhcEJy0UNZ9rXOLV.jpg',
  'release_date': '2022-06-24',
  'title': '씨 비스트',
  'video': False,
  'vote_average': 7.7,
  'vote_count': 470},
 {'adult': False,
  'backdrop_path': '/egoyMDLqCxzjnSrWOz50uLlJWmD.jpg',
  'genre_ids': [28, 12, 10751, 35],
  'id': 675353,
  'original_language': 'en',
  'original_title': 'Sonic the Hedgehog 2',
  'overview': '강력한 파워의 ‘너클즈’와 함께 돌아온 천재 과학자 ‘닥터 로보트닉’에 맞서 지구를 구하기 위해 ‘소닉’과 새로운 '
              '파트너 ‘테일즈’가 전 세계를 누비는 스피드 액션 블록버스터.',
  'popularity': 1489.947,
  'poster_path': '/8dzKn3RtPWUJRG9ymSpi423eMNV.jpg',
  'release_date': '2022-03-30',
  'title': '수퍼 소닉 2',
  'video': False,
  'vote_average': 7.7,
  'vote_count': 2605}]
"""
```



### 4. 내가 생각하는 이 문제의 포인트

* dictionary의 특정 key의 value값으로 정렬을 해야하는 문제!
* 이번에 sort함수에 key값에 대해 공부하였습니다!

-----

## D. 특정 추천 영화 조회 (problem_d)

### 1. 요구 사항 

* 제공된 영화 제목으로 TMDB에서 영화를 검색(Search Movies)합니다.

* 응답 받은 결과 중 첫번째 영화의 id 값을 찾아 해당 영화에 대한 추천 영화 목록 (Get Recommendations)을 가져옵니다.

* 추천 영화 목록 중 첫번째 영화만 출력하는 함수 recommendation을 작성합니다.

* 추천 영화가 없을 경우 []를 반환합니다.

* 검색한 영화 정보가 없다면 None을 반환합니다.



### 2. 풀이 코드

``` python 
import requests
from pprint import pprint


def recommendation(title):
    # query를 포함해 db에 get 요청을 보내는 방법!
    URL = f'https://api.themoviedb.org/3/search/movie?api_key=8d8e9b9672f4d1a183be6806ad451223&language=ko-KR&query={title}&include_adult=false'
    response = requests.get(URL).json()
    search_movies = response.get('results')

    # 돌아온 응답에 영화가 없다면 None을 반환
    if search_movies == []:
        return None
    
    # 돌아온 응답에 영화가 있다면
    else: 
        # 응답된 영화의 id로 추천 영화 목록을 db에 get 요청을 보냄!
        recommend_URL = f"https://api.themoviedb.org/3/movie/{search_movies[0].get('id')}/recommendations?api_key=8d8e9b9672f4d1a183be6806ad451223&language=ko-KR"
        response = requests.get(recommend_URL).json()
        recommend_movies = response.get('results')

        # 응답받은 추천 영화 목록들의 title만 반환 리스트에 저장!
        recommend_movies_title = []
        for movie in recommend_movies:
            recommend_movies_title.append(movie.get('title'))

        # title 리스트 반환!
        return recommend_movies_title


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    pprint(recommendation('기생충'))
    # ['조커', '1917', '조조 래빗', ..생략.., '살인의 추억', '펄프 픽션']
    pprint(recommendation('그래비티'))
    # []
    pprint(recommendation('검색할 수 없는 영화'))
    # None

```



### 3. 결과 화면

```PYTHON
"""
['조커',
 '1917',
 '조조 래빗',
 '원스 어폰 어 타임 인… 할리우드',
 '결혼 이야기',
 '나이브스 아웃',
 '아이리시맨',
 '포드 V 페라리',
 '작은 아씨들',
 '라이트하우스',
 '미드소마',
 'Authentik',
 '더 플랫폼',
 '언컷 젬스',
 '센과 치히로의 행방불명',
 '패스트 & 필 러브',
 '암살',
 '그린 북',
 '스타워즈: 라이즈 오브 스카이워커',
 '내 여자친구를 소개합니다',
 '두 교황']
[]
None
"""
```



### 4. 내가 생각하는 이 문제의 포인트

* url 주소에 변수를 포함해서 요청을 보내는 방법!

-----

## E. 출연진, 연출진 데이터 조회 (problem_e)

### 1. 요구 사항 

* 제공된 영화 제목으로 TMDB에서 영화를 검색(Search Movies)합니다.

* 응답 받은 결과 중 첫번째 영화의 id 값을 찾아 해당 영화에 대한 출연진과 스태프 목록(Get Credits)을 가져옵니다.

* 출연진은 cast_id 값이 10 미만인 출연진만 추출하며, 연출진은 스태프 부서가 Directing인 데이터만 추출합니다.

* 위 조건을 만족해서 답을 반환하는 함수 credits를 작성합니다.

* 검색한 영화 정보가 없다면 None을 반환합니다.



### 2. 풀이 코드

``` python 
import requests
from pprint import pprint


def credits(title):
    # query를 포함해 db에 get 요청을 보내는 방법!
    URL = f'https://api.themoviedb.org/3/search/movie?api_key=8d8e9b9672f4d1a183be6806ad451223&language=ko-KR&query={title}&include_adult=false'
    response = requests.get(URL).json()
    search_movies = response.get('results')

    # 돌아온 응답에 영화가 없다면 None을 반환
    if search_movies == []:
        return None

    # 돌아온 응답에 영화가 있다면
    else: 
        # 응답된 영화 id로 출연진, 스태프의 정보를 db에 get요청을 보냄!
        cast_staff_URL = f"https://api.themoviedb.org/3/movie/{search_movies[0].get('id')}/credits?api_key=8d8e9b9672f4d1a183be6806ad451223&language=ko-KR"
        response = requests.get(cast_staff_URL).json()

        # 요청받은 출연진, 스태프의 정보를 각각 분리
        casts = response.get('cast')
        crews = response.get('crew')

        # return해줄 딕셔너리 선언
        result_credits = {
            'cast': [],
            'directing': []
        }

        # 출연진의 id가 10 미만인 사람들만 반환 딕셔너리에 추가
        for cast in casts:
            if cast.get('cast_id') < 10:
                result_credits['cast'].append(cast.get('name'))

        # 스태프의 부서가 Directing인 사람만 반환 딕셔너리에 추가
        for crew in crews:
            if crew.get('department') == "Directing":
                result_credits['directing'].append(crew.get('name'))

        # 딕셔너리 반환
        return result_credits
    # 여기에 코드를 작성합니다.  


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    pprint(credits('기생충'))
    # {'cast': ['Song Kang-ho', 'Lee Sun-kyun', ..., 'Jang Hye-jin'], 'crew': ['Bong Joon-ho', 'Park Hyun-cheol', ..., 'Yoon Young-woo']}
    pprint(credits('검색할 수 없는 영화'))
    # None

```



### 3. 결과 화면

``` python
"""
{'cast': ['Song Kang-ho',
          'Lee Sun-kyun',
          'Cho Yeo-jeong',
          'Choi Woo-shik',
          'Park So-dam',
          'Lee Jung-eun',
          'Jang Hye-jin'],
 'directing': ['Bong Joon-ho',
               'Park Hyun-cheol',
               'Han Jin-won',
               'Kim Seong-sik',
               'Lee Jung-hoon',
               'Yoon Young-woo']}
None
"""
```



### 4. 내가 생각하는 이 문제의 포인트

* 이 문제에서는 특별히 더 배워갈 점은 없었다 .. ?

-----



# 후기

* 오늘 프로젝트는 어려워 보였지만 나의 착각이었다.
* 파이썬에서 api 통신 방법으로 get 요청을 받아봤는데 재미있었다!
* json을 디코드하여 파이썬에서 사용하기 위한 객체로 만들어 보았는데 반대로 인코딩하여 post 요청을 하는 방법도 배웠으면 좋겠다
* 파이썬 문법을 어느 정도 배웠기 때문에 여러 방식으로 원하는 데이터에 접근하는게 가능해졌다. 하지만 계속 한가지 방법으로만 생각이 굳는 것 같게 되어 아쉽다? 메모리를 적게, 효율적으로 코드를 짤 수 있는 방법이나 팁을 배웠으면 좋겠다.
* 파이썬에서 json body를 출력하니까 눈이 어지러웠다. 크롬 확장팩 jsonview를 통해서 직관적으로 데이터를 본 후 쉽게 데이터에 접근할 수 있었다.
