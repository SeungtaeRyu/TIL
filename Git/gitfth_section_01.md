# section01 버전관리의 본질

<br>

## git init

- pwd : 현재 위치를 알려준다
- mkdir : 폴더 생성
- cd : 체인지 디렉토리(이동하기)
- ls -al 파일 확인
- git init : 깃 start 방법 중 하나

<br>

## git add

- vim f1.txt
  - i 로 insert 모드, esc로 편집모드 종료
  - :wq를 적으면 저장(w) 후 나가기(q)
- cat f1.txt
  - 파일 안에 내용 보기
- git status
- git add f1.txt

<br>

## 버전 만들기

- 한번만 하면 되는 것 
  - git config --global user.name [user name]
  - git config --global user.email [user email]
- git commit
  - vim 화면 출력
  - :wq 엔터
- git log

​	<br>

## git stage area

- cp f1.txt f2.txt : f1.txt를 카피해서 f2.txt를 만든다
- stage area - commit 대기상태

​	<br>

## 변경 사항 확인하기 (log & diff)

- git log
- git log -p : 각각의 커밋에서 소스 차이를  보여준다
- git log [commit id] : 커밋id 이전의 메세지만 보여준다
- git diff [commit id1]..[commit id2] : id1의 커밋과 id2의 커밋의 소스 차이를 보여준다

​	<br>

## 과거로 돌아가기 (reset)

- reset
  - git log 후 돌아가고 싶은 commit의 id를 확인
  - git reset [commit id] --hard : hard는 좀 위험, 나중가서 다른 옵션도 배움
- revert
  - 커밋을 취소하면서 새로운 버전을 생성한다

​	<br>

## 스스로 공부하는 법

- git commit --help 후 options 살펴보기
  - git commit -a : 수정하거나 삭제한 파일을 자동으로 스테이지에 올린다
  - git commit -am "message" : 자동으로 스테이지에 올리면서 커밋메세지를 입력한다

​	<br>













