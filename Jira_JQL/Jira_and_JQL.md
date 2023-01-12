# Jira 및 JQL

<br>

## JQL

### JQL이란? 

- Jira Query Language
- Jira Issue를 구조적으로 검색 하기 위해 제공하는 언어
- SQL과 비슷한 문법
- Jira의 각 필드들에 맞는 특수한 예약어들을 제공
- 쌓인 Issue 들을 재가공해 유의미한 데이터를 도출해 내는데 활용



### Basic Query & Advanced Query



### Operators

- =, !=, >, >=
- in, not in
- ~ (contains), !~ (not contains)
- is empty, is not empty, is null, is not null



### JQL Keywords

- AND
- OR
- NOT
- EMPTY
- NULL
- ORDER BY



### JQL Dates

- 날짜를 상대적으로 표시 가능 !!
  - ex)어제는 -1d



### JQL Functions

- endOfDay(), startOfDay()
- endOfWeek() (Saturday), startOfWeek() (Sunday)
- endOfMonth(), startOfMonth(), endOfYear(), startOfYear()
- currentUser()



### JQL 활용 예시

- ```
  project = "DP" and assignee = currentUser() and resolution = Unresolved
  ```



### Filters 

- 뷰 권한, 편집 권한 부여 가능
- 즐겨찾기 기능 제공



### Dashboards

- 필터와 같이 공유 가능
- 레이아웃 변경 가능
- Gadget 추가 가능



### Agile Board

- kanban 보드 사용



### 현업에서의 Jira 활용

- 깃랩, 깃허브 이슈와 연동 가능
- 이슈의 key를 commit 메세지에 추가하면 링크가 걸림