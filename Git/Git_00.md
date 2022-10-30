# GIT

<br>

## 목차

- GUI와 CLI
- GIt Bash
- 절대경로와 상대경로
- GIt Bash 명령어
- GIt 기본기
- user setup

<br>

<br>

## GUI와 CLI

- Graphic User Interface
- Command Line Interface

<br>

<br>

## GIt Bash

- ~ : 홈 디렉토리
- 루트 디렉토리: computer 가장 상위 디렉토리

<br>

<br>

## 절대경로와 상대경로

- 절대경로: 루트 디렉토리부터 목적 파일까지 모든 경로가 전부 포함
- 상대경로: 현재 작업중인 디렉토리를 기준으로 계산한 상대적 경로
  - ./ : 현재 폴더
  - ../ : 상위 폴더

<br>

<br>

## GIt Bash 명령어

- touch : 파일을 생성하는 명령어

  - 여러개의 파일을 띄워쓰기로 생성 가능

- start . : 현재 파일에서 GUI 

- mkdir (make directory) : 폴더를 생성하는 명령어

  - 폴더 이름에 띄워쓰기가 존재하는 경우
    - ex) mkdir 'forder a'

- ls : 현재 폴더의 파일 목록 보여주는 명령어

  - ls -a : 숨긴 파일까지 모두 보여준다 
  - ls -l : 파일 정보 더 자세히 보기

- pwd (print working directory) : 현재 폴더의 절대 경로를 보여주는 명령어

- cd (change directory) : 현재 폴더에서 위치를 변경하는 명령어

- mv (move)

  - 같은 폴더 간 move => rename
  - 다른 폴더 간 move => 이동

- rm (remove) : 파일을 삭제하는 명령어

  - 복구가 되지 않는다.

<br>

<br>

## GIt 기본기

- 커밋(commit)은 이 3가지 영역을 바탕으로 동작한다
  
  - Working Directory
  - Staging Area
  - Repository

- `git add`  명령어
  - working Directory 파일의 untracked 파일을 Staging Area로 옮긴다
  
- `git commit -m"message적는곳"`  명령어
  - 버전을 확정해준다
  
- 작업 폴더 첫 setup 방법
  
  1. git bash 터미널 열기
  2. `git init` 입력
  3. `git config --global user.name SeungtaeRyu` 입력
  4. `git config --global user.name dbtmdxo1992@naver.com` 입력
  5. `git config --global --list`  (확인용)

- `git status` 명령어
  - 현재 commit 상태와 Untracked files를 보여준다
  
- `git rm --cached <filename>`  명령어
  
  - add 했던 file을 취소해준다

- `git log` 명령어
  
  - commit 내용을 추적해준다
  - `git log --oneline` : 한 commit당 한 줄로 요약해준다. (cashe도 줄여서 보여줌)

- `git push` 명령어
  
  - 로컬 저장소에서 원격 저장소로 보낼 때

- `git pull` 명령어
  
  - 원격 저장소에서 로컬 저장소로 받아올 때

- `git clone` 명령어
  
  - 원격 저장소에서 로컬 저장소로 받아올 때
  - 로컬 저장소에 아무것도 없을 때만 가능하다.

- `git remote add origin <원격 저장소 주소>`  명령어
  
  - 로컬 저장소와 원격 저장소를 연결한 후 `git remove -v` 로 확인

- 로컬 저장소에서 원격 저장소로 보내는 예시
  
  1. `git init`
  2. `git add <file name>`
  3. `git commit -m "commit messeage"`
  4. `git remote add origin <원격 저장소 주소>` 
  5. `git push -u origin master` 

- `git clone <원격 저장소 주소>` 명령어 
  
  - 폴더를 만들고 싶은 위치의 상위 폴더에서 써야 한다

<br>

<br>

## user setup

- user.name 삭제

  ```bash
  -- 사용자 이름을 선택하여 삭제
  git config --global --unset user.name 사용자이름
  -- 전체 사용자 이름 삭제
  git config --global --unset-all user.name
  ```

<br>

- uesr.email 삭제

  ```bash
  -- 사용자 이메일을 선택하여 삭제
  git config --global --unset user.email 사용자이메일
  -- 전체 사용자 이메일 삭제
  git config --global --unset-all user.email
  ```

<br>

- 리스트 확인

  ```bash
  git config --global --list
  ```

<br>

- 사용자 이름과 사용자 이메일을 다시 추가하고 싶다면

  ```bash
  git config --global user.name 사용자이름
  git config --global user.email 사용자이메일
  ```

  
