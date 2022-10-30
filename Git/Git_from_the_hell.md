# Git from the hell

<br>

#### 목차

- 01강 - 버전관리의 본질
- 02강 - git의 원리
- 03강 - git의 혁신 - branch
- 04강 - 생활코딩 강의 컨셉
- 05강 - git의 원리
- 06강 - 원격저장소
- 07강 - 태그
- 08강 - Rebase
- 09강 - git을 이용한 프로젝트의 흐름
- 10강 - 수업을 마치며

<br>

<br>

## 01. 버전관리의 본질

- #### git init

  - pwd : 현재 위치를 알려준다

  - mkdir : 폴더 생성

  - cd : 체인지 디렉토리(이동하기)

  - ls -al 파일 확인

  - git init : 깃 start 방법 중 하나


<br>

- #### git add

  - vim f1.txt
    - i 로 insert 모드, esc로 편집모드 종료
    - :wq를 적으면 저장(w) 후 나가기(q)
    
    - cat f1.txt
      - 파일 안에 내용 보기
    

  - git status

  - git add f1.txt


<br>

- #### 버전 만들기

  - 한번만 하면 되는 것 
    - git config --global user.name [user name]
    - git config --global user.email [user email]
    
    - git commit
      - vim 화면 출력
      - :wq 엔터
    

  - git log


​	<br>

- #### git stage area

  - cp f1.txt f2.txt : f1.txt를 카피해서 f2.txt를 만든다

  - stage area - commit 대기상태


​	<br>

- #### 변경 사항 확인하기 (log & diff)

  - git log

  - git log -p : 각각의 커밋에서 소스 차이를  보여준다

  - git log [commit id] : 커밋id 이전의 메세지만 보여준다

  - git diff [commit id1]..[commit id2] : id1의 커밋과 id2의 커밋의 소스 차이를 보여준다


​	<br>

- #### 과거로 돌아가기 (reset)

  - reset
    - git log 후 돌아가고 싶은 commit의 id를 확인
    - git reset [commit id] --hard : hard는 좀 위험, 나중가서 다른 옵션도 배움

  - revert
    - 커밋을 취소하면서 새로운 버전을 생성한다


​	<br>

- #### 스스로 공부하는 법

  - git commit --help 후 options 살펴보기
    - git commit -a : 수정하거나 삭제한 파일을 자동으로 스테이지에 올린다
    - git commit -am "message" : 자동으로 스테이지에 올리면서 커밋메세지를 입력한다


​	<br>

​	<br>

## 02. git의 원리

- #### 분석도구 gistory 소개

  - python 설치

  - windows : pip install gistory

  - max : sudo pip or pip3 install gistory

  - 실습폴더 git bash에서 gistory 입력 후 포트번호 확인

  - 로컬호스트 포트번호에 접속


<br>

- #### git add

  - 새로운 실습폴더 생성 후 git init

  - .git이 있는 폴더에서 gistory 실행
    - 파일 생성후 add 하면 2개의 파일이 바뀐다
      - index
      - objects
      - 파일의 이름은 index에 담겨있고 내용은 objects에 담겨 있다
      - objects 앞의 2자리는 디렉토리 라고 말하는듯???


  - f1.txt와 f3.txt의 내용이 같을 때 
    - git은 파일 제목이 달라도 내용이 같으면 같은 objects 주소를 가르킨다


<br>

- #### objects 파일명의 원리

  - 구글에서 sha1 onlie 쳐보기 [SHA1 online](#http://www.sha1-online.com/)

  - objects의 이름은 내용을 sha1 이라는 해쉬를 통과한 내용에 뭔가를 덧붓여서 정해지는 듯함


<br>

- #### commit의 원리

  - commit을 실행하면 여러개의 파일이 바뀜
    - objects 
      - tree : SHA1 으로 만들어진 값 : 스테이지에 올라온 파일들과 내용
      - author
      - message

    - logs/refs/heads/master
    - logs/HEAD
    - COMMIT_EDITMSG
    - refs/heads/master


  - 파일을 수정 후 add, commit 을 실행하면 objects 객체에 parent 정보(이전 커밋 정보)가 담긴다


<br>

- #### 정리

  - commit의 objects에는 중요한 정보 2개가 있다
    1. tree
    2. parent

  - objects는 3가지 정도로 나뉜다
    1. blob : 파일의 내용
       1. tree : blob에 대한 정보를 담고 있다
       2. commit : commit객체 주소를 담고 있다


<br>

- #### status의 원리

  - 파일이 변경 되었을 때

    - index 안 파일 내용과 working directory 내용이 다르면 git status에 변경사항이 있다고 본다

    - 파일을 add 했을 때 
      - index의 파일과 add된 파일의 내용이 같으면 commit 대기 상태라고 보는듯?
      - 또한, index의 내용과 마지막 commit의  tree에서 가르키는 파일의 내용이 다르다면 commit 대기상태


  - commit을 하면 index, objects의 tree, 디렉토리의 파일 안 내용까지 세 가지가 같아진다

  - 이 때 git status를 하면 더이상 commit 할 것이 없다고 알려준다

  - 복잡한 개념은 구글 이미지 검색으로 찾아보기
    - git working directory vs index vs repository 검색


<br>

<br>

## 03. git의 혁신 - branch

- #### branch 만들기

  - git branch : 현재 branch 확인 
    - git branch [branchName] : 브랜치 생성

      - 생성한 브랜치는 **생성했던 브랜치의 정보**를 그대로 가지고 온다


  - git checkout [branchName] : 브랜치 변경


<br>

- #### branch 정보확인

<br>

- #### branch 병합

<br>

- #### branch 수련

<br>

- #### stach

<br>

<br>

## 04. 생활코딩 강의 컨셉

- #### 끝이 열려 있는 강의

<br>

<br>

## 05. git의 원리

- #### branch

- #### branch 충돌 해결

- #### reset checkout

- #### working copy & index & repository

- ####  merge & conflict

- #### 3 way merge

<br>

<br>

## 06. 원격저장소

- #### 원격 저장소 소개

- #### 원격 저장소 생성

- #### github 소개

- #### 원격 저장소 만들기 (Github)

- #### 동기화 방법 (Github)

- #### ssh를 이용해서 로그인없이 원격저장소 사용하기 (Github)

- #### 자기 서버에 원격 저장소 만들기

- #### push & pull

- #### 자동 로그인

- #### 원격 저장소의 원리

- #### pull VS fetch의 원리

<br>

<br>

## 07. 태그

- #### 2 tag 1 (기본사용법)

- #### tag 2 (원리)

<br>

<br>

## 08. Rebase

- #### Rebase 1/3

- #### Rebase 2/3

- #### Revase 3/3

<br>

<br>

## 09. git을 이용한 프로젝트의 흐름

- #### Git Flow1

- #### Git Flow2

<br>

<br>

## 10. 수업을 마치며

- #### 수업을 마치며...

<br>

<br>



