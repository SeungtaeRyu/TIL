# PJT 01

### 목차

* [Problem_a](#A.-제공되는-영화-데이터의-주요내용-수집)

* [Problem_b](#B.-제공되는-영화-데이터의-주요내용-수정)

* [Problem_c](#C.-다중-데이터-분석-및-수정)

* [Problem_d](#D.-알고리즘을-사용한-데이터-출력)

* [Problem_e](#E.-알고리즘을-사용한-데이터-출력)

  

# A. 제공되는 영화 데이터의 주요내용 수집

* 요구 사항 : 

  * 제공되는 movie.json을 활용합니다.

  * movie.json은 영화 ‘쇼생크 탈출’ 정보를 담고 있습니다.

  * movie.json에서 id, title, poster_path, vote_average, overview, genre_ids 키에 해당하는 값을 추출합니다. 

  * 추출한 값을 새로운 dictionary로 반환하는 함수 movie_info를 완성합니다.

* 결과 : 

  * 문제 접근 방법 및 코드 설명

  ```python
  import json
  from pprint import pprint
  
  
  def movie_info(movie):
      
      # new_data 라는 dictionary 타입을 만들고 movie에서 get한 value를 할당합니다
      result_dict = {
          'id': movie.get('id'),                  
          'title': movie.get('title'),               
          'poster_path': movie.get('poster_path'), 
          'vote_average': movie.get('vote_average'),  
          'overview': movie.get('overview'),        
          'genre_ids': movie.get('genre_ids')     
      }
      return result_dict
  
  
  # 아래의 코드는 수정하지 않습니다.
  if __name__ == '__main__':
      movie_json = open('data/movie.json', encoding='utf-8')
      movie_dict = json.load(movie_json)
      
      pprint(movie_info(movie_dict))
  
  ```

## 배운 것

* `json` 파일을 `path`로 접근하고 `인코딩`하는 문법.
* `json.load`를 사용해 json string을 python 객체로 변환할 수 있다.
* `dictionary.get('key')` 함수를 통해 value를 가져올 수 있다.

---



# B. 제공되는 영화 데이터의 주요내용 수정

* 요구 사항 : 

  * 제공되는 movie.json, genres.json을 활용합니다.

  * genres.json은 모든 장르의 id, name 정보를 담고 있습니다.

  * movie.json에서 id, title, poster_path, vote_average, overview, genre_ids 키에 해당하는 값을 추출합니다. 

  * genres.json을 이용하여 genre_ids를 각 장르 번호에 맞는 name 값으로 대체한 genre_names 키를 생성합니다. 

  * 위 요구사항을 반영한 새로운 dictionary를 반환하는 함수 movie_info를 완성합니다.

* 결과 : 

  * 문제 접근 방법 및 코드 설명

  ```python
  import json
  from pprint import pprint
  
  
  def movie_info(movie, genres):
      
      # return 될 데이터 생성
      result_dict = {
          'id': movie.get('id'),
          'title': movie.get('title'),
          'poster_path': movie.get('poster_path'),
          'vote_average': movie.get('vote_average'),
          'overview': movie.get('overview'),
          'genre_names': [] # genre_names라는 key를 리스트로 초기화합니다.
      }
      
      # movie의 genre_ids 값으로 반복문을 실행
      for ids in movie.get('genre_ids'):  
          # genres.json 파일에 있는 list의 length만큼 반복문을 실행
          for i in range(len(genres)):    
              # movie.genre_ids값(ids) = genres[i].id값이 같으면
              if ids == genres[i].get('id'):  
                  # genres[i]에 해당하는 name를 genre_names에 추가합니다 
                  result_dict['genre_names'].append(genres[i].get('name'))   
  
      return result_dict
          
  
  # 아래의 코드는 수정하지 않습니다.
  if __name__ == '__main__':
      movie_json = open('data/movie.json', encoding='utf-8')
      movie = json.load(movie_json)
  
      genres_json = open('data/genres.json', encoding='utf-8')
      genres_list = json.load(genres_json)
  
      pprint(movie_info(movie, genres_list))
  
  ```

  * 이 문제에서 어려웠던점
  * 내가 생각하는 이 문제의 포인트

## 배운 것

* 일치하는 id를 찾는 로직을 구현하며 제어문을 잘 이해하게 되었다!
* 복잡한 json 파일에 원하는 값까지 접근하기 위한 원리를 깨우침!

## 후기

- 개인적으로 가장 시간이 오래 걸렸지만, type에 대해 잘 알게 되었다.

---



# C. 다중 데이터 분석 및 수정 

* 요구 사항 : 

  * 이전 단계의 함수 구조를 재사용합니다.

  * 개별 영화 데이터는 id, title, poster_path, vote_average, overview, genre_names 키와 이에 해당하는 값을 가집니다.

  * 위 요구사항을 반영한 새로운 list를 반환하는 함수 movie_info를 완성합니다.

* 결과 : 

  * 문제 접근 방법 및 코드 설명

  ```python
  import json
  from pprint import pprint
  
  
  def movie_info(movies, genres):
  
      # return 될 list 초기화
      result_list = []
  
      # movies의 길이만큼 반복문을 동작
      for index in range(len(movies)):
  
          # 새로운 movie 생성
          movie = {
              'id': movies[index].get('id'),
              'title': movies[index].get('title'),
              'poster_path': movies[index].get('poster_path'),
              'vote_average': movies[index].get('vote_average'),
              'overview': movies[index].get('overview'),
              'genre_names': []
          }
  
          # problem_b 에서 풀었던 id를 name으로 변환하는 코드
          for ids in movies[index].get('genre_ids'):
              for i in range(len(genres)):
                  if ids == genres[i].get('id'):
                      movie['genre_names'].append(genres[i].get('name'))
  
          # return 될 list에 movie를 추가!
          result_list.append(movie)
  
      return result_list
          
  # 아래의 코드는 수정하지 않습니다.
  if __name__ == '__main__':
      movies_json = open('data/movies.json', encoding='utf-8')
      movies_list = json.load(movies_json)
  
      genres_json = open('data/genres.json', encoding='utf-8')
      genres_list = json.load(genres_json)
  
      pprint(movie_info(movies_list, genres_list))
  
  ```

## 후기

- 이번에는 movies.json 폴더에서 data를 받아왔는데 python객체로 변환하였을 때 list 형태인 문제였다.
- problem_b의 코드가 단일 딕셔너리에서, 리스트 딕셔너리로 바뀐 것 말고는 똑같다!



---



# D. 알고리즘을 사용한 데이터 출력

* 요구 사항 : 

  * 반복문을 통해 movies 폴더 내부의 파일들을 오픈해야 합니다. 

  * 제공된 영화 데이터에서 수익이 같은 영화는 없습니다. 

  * 수익이 가장 높은 영화의 제목을 출력하는 함수 max_revenue를 완성합니다.

* 결과 : 

  * 문제 접근 방법 및 코드 설명

  ```python
  import json
  
  
  def max_revenue(movies):
  
      # max 수익과 max 수익일 때의 index를 기억할 변수 생성
      result_index = 0
      result_revenue = 0
      
      # movies.json 파일의 리스트 길이만큼 반복문을 동작!
      for i in range(len(movies)):
  
          # movies[i]의 id를 추출하고 movies 폴더에서 같은 id를 가진 json파일 경로 설정 
          file_path = 'data/movies/' + str(movies[i].get('id')) + '.json'
  
          # movies[i]의 id에 해당하는 movies/id.json 파일 오픈! 
          movie_json = open(file_path, encoding='utf-8')
          movie_dict = json.load(movie_json)
          
          # id.json 파일에서 revenue를 찾아, max_revenue인 movie의 인덱스를 찾는다!
          if result_revenue < movie_dict.get('revenue'):
              result_revenue = movie_dict.get('revenue')
              result_index = i
      
      # 찾은 인덱스의 json파일을 다시 오픈하고 
      file_path = 'data/movies/' + str(movies[result_index].get('id')) + '.json'
      movie_json = open(file_path, encoding='utf-8')
      movie_dict = json.load(movie_json)
  
      # 다시 오픈한 파일에서 title을 리턴한다!
      return movie_dict['title']
      
          
  # 아래의 코드는 수정하지 않습니다.
  if __name__ == '__main__':
      movies_json = open('data/movies.json', encoding='utf-8')
      movies_list = json.load(movies_json)
      
      print(max_revenue(movies_list))
  
  ```

## 배운 것

* python을 동작시키는 file을 기준으로 열어야 하는 file까지의 상대경로 설정법을 공부했다!

## 후기

- max_revenue를 찾을 때마다 해당 movie의 인덱스를 같이 찾았어야 하는데 변수 두개를 지정해서 사용했다.
- 다음에는 enumerage를 사용해보면 어떨까 생각한다.



---



# E. 알고리즘을 사용한 데이터 출력

* 요구 사항 : 

  * 반복문을 통해 movies 폴더 내부의 파일들을 오픈해야 합니다. 

  * 개봉일이 12월인 영화들의 제목을 리스트로 출력하는 함수 dec_movies를 완성합니다.

* 결과 : 

  * 문제 접근 방법 및 코드 설명

  ```python
  import json
  
  
  def dec_movies(movies):
  
      # return 될 list 초기화
      result_list = []
  
      # movies.json 파일의 리스트 길이만큼 반복문을 동작!
      for i in range(len(movies)):
  
          # problem_d에서 작성했던 {id}.json 폴더를 오픈하는 코드!
          file_path = 'data/movies/' + str(movies[i].get('id')) + '.json'
          movie_json = open(file_path, encoding='utf-8')
          movie_dict = json.load(movie_json)
  
          # {id}.json 파일에서 release_date를 추출하고 year, month, day 를 split하여 저장합니다
          release_date = list(map(int, movie_dict['release_date'].split('-')))
          # month 만 따로 저장합니다!
          release_month = release_date[1]
          
          # 영화 개봉 month가 12일 때 리턴될 list에 영화 제목 추가! 
          if release_month == 12:
              result_list.append(movies[i].get('title'))
  
      return result_list         
  
  # 아래의 코드는 수정하지 않습니다.
  if __name__ == '__main__':
      movies_json = open('data/movies.json', encoding='utf-8')
      movies_list = json.load(movies_json)
      
      print(dec_movies(movies_list))
  
  ```

## 배운 것

* problem_d의 과정을 거친 후 `release_date` 를 추출하고 데이터를 가공하여 month를 뽑아내는 기능을 구현해 보았다!

## 후기 

- problem_d를 구현한 후에는 별로 어렵지 않은 문제인 것 같다!

---

