# Git from the hell

<br>

#### 목차

- [01강 - 버전관리의 본질](#01-버전관리의-본질)
- [02강 - git의 원리](#02-git의-원리)
- [03강 - git의 혁신 - branch](#03-git의-혁신---branch)
- [04강 - git의 원리](#04-git의-원리)
- [05강 - 원격저장소](#05-원격저장소)
- [06강 - 태그](#06-태그)
- [07강 - Rebase](#07-Rebase)
- [08강 - git을 이용한 프로젝트의 흐름](#08-git을-이용한-프로젝트의-흐름)
- [09강 - 수업을 마치며](#09-수업을-마치며)

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

<br>

- #### 버전 만들기

  - 한번만 하면 되는 것 
    - git config --global user.name [user name]
    - git config --global user.email [user email]
    


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
    2. tree : blob에 대한 정보를 담고 있다
    3. commit : commit객체 주소를 담고 있다


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

  - ```
    git log --branches --decorate --graph --oneline
    ```

    - `--branches` : 모든 브랜치 확인
    - `--graph` : 눈으로 확인
    - `--oneline` : commit 하나 당 한 줄로 보기

  - ```
    git log master..exp
    ```

    - master에는 없고 exp 에는 있는 것들 확인

  - ```
    git diff master..exp
    ```


<br>

- #### branch 병합

  1. 합쳐지는 곳의 branch로 checkout 하기

  2. ```
     git merge [합칠 branch name]
     ```

  3. ```
     git branch -d [합친 branch name]
     ```

<br>

- #### stash

  - 브랜치에서 작업이 끝나지 않았는데 다른 브랜치에서 해결할 일이 있을 경우 사용!
  - 그런 일이 발생했을 때 공부해도 늦지 않다!


<br>

<br>

## 04. git의 원리

- #### branch

<br>

- #### branch 충돌 해결

  1. Auto-merging [파일이름] 에러가 발생!

  2. 충돌한 파일을 연다!

  3. 사용자가 직접 파일을 수정 후 add, commit 하기!

<br>

- #### reset checkout

  - reset이란 checkout 된 branch의 최신 커밋을 바꾸는 행위

    - ```
      git reset --hard [commit id]
      ```

  - reset을 취소하는 법

    - ```
      git reset --hard ORIG_HEAD
      ```

    - ```
      git reflog
      ```

  - commit id로도 체크아웃을 할 수 있음!

    - ```
      git checkout [commit id]
      ```

    - HEAD는 branch 폴더 없이 commit을 직접 가르킴!


<br>

- #### working copy & index & repository

  - reset 옵션이 건드리는 작업 영역

    - ![image-20221030172039783](Git_from_the_hell.assets/image-20221030172039783.png)
    - **옵션을 지정하지 않으면 `--mixed` 옵션이 지정된다**

  - working directory 와 staging area의 상태를 비교하는 명령어

    - ```
      git diff
      ```


<br>

- ####  merge & conflict

  - kdiff3 오픈소스 사용하여 충돌 해결하기

    1. 오픈소스 설치

    2. ```
       git config --global merge.tool kdiff3
       ```

    3. ```
       git mergetool
       ```

    4. 화면의 A(조상), B(checkout branch), C(병합될 branch) 중 선택

    5. 수정을 하고 싶다면 아무거나 선택하고 아래쪽에서 작업 

<br>

- #### 3 way merge

  - 2 way merge 시 Base를 신경 쓰지 않음
    - ![image-20221030180450293](Git_from_the_hell.assets/image-20221030180450293.png)
  - 3 way merge 시 결과
    - ![image-20221030180344684](Git_from_the_hell.assets/image-20221030180344684.png)



<br>

<br>

## 05. 원격저장소

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

## 06. 태그

- #### 2 tag 1 (기본사용법)

- #### tag 2 (원리)

<br>

<br>

## 07. Rebase

- #### Rebase 1/3

- #### Rebase 2/3

- #### Revase 3/3

<br>

 
<br>

## 08. git을 이용한 프로젝트의 흐름

- #### Git Flow1

- #### Git Flow2

<br>

<br>

## 09. 수업을 마치며

- #### 수업을 마치며...

<br>

<br>



