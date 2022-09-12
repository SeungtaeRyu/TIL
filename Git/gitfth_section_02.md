# section02 git의 원리

<br>

## 분석도구 gistory 소개

- python 설치
- windows : pip install gistory
- max : sudo pip or pip3 install gistory
- 실습폴더 git bash에서 gistory 입력 후 포트번호 확인
- 로컬호스트 포트번호에 접속

<br>

## git add

- 새로운 실습폴더 생성 후 git init
- .git이 있는 폴더에서 gistory 실행
- 파일 생성후 add 하면 2개의 파일이 바뀜
  - index
  - objects
  - 파일의 이름은 index에 담겨있고 내용은 objects에 담겨 있다
  - objects 앞의 2자리는 디렉토리 라고 말하는듯???

- f1.txt와 f3.txt의 내용이 같을 때 
  - git은 파일 제목이 달라도 내용이 같으면 같은 objects 주소를 가르킨다


​	<br>

## objects 파일명의 원리

- 구글에서 sha1 onlie 쳐보기 [SHA1 online](#http://www.sha1-online.com/)
- objects의 이름은 내용을 sha1 이라는 해쉬를 통과한 내용에 뭔가를 덧붓여서 정해지는 듯함

​	<br>

## commit의 원리

- commit을 실행하면 여러개의 파일이 바뀜
  - objects 
    - tree : SHA1 으로 만들어진 값 : 스테이지에 올라온 파일들과 내용
    - author
    - message

  - logs/refs/heads/master
  - logs/HEAD
  - COMMIT_EDITMSG
  - refs/heads/master

- 파일을 수정 후 add, commit 을 실행하면 objects 객체에 parent 정보(이전 커밋 정보)가 담김

#### 정리

- commit의 objects에는 중요한 정보 2개가 있다. 
  1. tree
  2. parent
- objects는 3가지 정도로 나뉨
  1. blob : 파일의 내용
  2. tree : blob에 대한 정보를 담고 있음
  3. commit : commit객체 주소를 담고 있음

​	<br>

## status의 원리

- 파일이 변경 되었을 때
  - index라는 파일과 가장 최근 commit의 내용이 같으면 git status에 변경사항이 없다고 보는듯?

- 파일을 add 했을 때 
  - index의 파일과 add된 파일의 내용이 같으면 commit 대기 상태라고 보는듯?
  - 또한, index의 내용과 마지막 commit의  tree에서 가르키는 파일의 내용이 다르다면 commit 대기상태?

- commit을 하면 index, objects의 tree, 디렉토리의 파일 안 내용까지 세가지가 같아짐
- 이 때 git status를 하면 더이상 commit 할 것이 없다고 알려준다
- 복잡한 개념은 구글 이미지 검색으로 찾아보기
  - git working directory vs index vs repository 검색




#### 정리

- [로컬 저장소] working directory - [add] index, staging area, cache - [commit] repository









































