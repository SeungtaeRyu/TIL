# SQL



#### 목차

- Database
- SQL
- DDL (Data Definition Language)
- DML (Data Manipulation Language)



## Database

#### RDB 기본 구조

1. 스키마
   - 테이블의 구조(Structure)
   - 데이터베이스에서 자료의 구조, 표현 방법, 관계 등 전반적인 명세를 기술한 것
2. 테이블
   - 필드
     - 속성, 컬럼 (Column)
   - 레코드
     - 튜플, 행 (Row)
   - 기본 키 (PK)
     - 기술적으로 다른 항목과 절대로 중복될 수 없는 **단일 값 (unique)**



#### 관계형 데이터베이스의 이점

- 데이터를 직관적으로 표현할 수 있음
- 관련한 각 데이터에 쉽게 접근할 수 있음
- 대량의 데이터도 효율적으로 관리 가능



#### RDBMS

- 관계형 데이터베이스를 만들고 업데이트하고 관리하는 데 사용하는 프로그램
  - SQLite, MySQL, PostgreSQL, Microsoft SQL Server, Oracle Database 등





<br>

## SQL

#### SQL 이란?

- 데이터를 관리하기 위해 설게된 **특수 목적의 프로그래밍 언어**



#### SQL Commands 종류

- DDL : 데이터 정의어
  - CREATE
  - DROP
  - ALTER
- DML : 데이터 조작어
  - INSERT
  - SELECT
  - UPDATE
  - DELETE
- DCL : 데이터 제어어
  - GRANT
  - REVOKE
  - COMMIT
  - ROLLBACK



#### SQL Syntax

- 모든 SQL 문은 키워드로 시작하고, 하나의 statement는 세미콜론(;) 으로 끝남
- SQL 키워드는 대소문자를 구분하지 않지만 대문자 권장



#### Statement & Clause

- Statement (문)
  - 독립적으로 실행할 수 있는 완전한 코드 조각
  - statement는 clause로 구성됨
- Clause (절)
  - statement의 하위 단위





<br>

## DDL

#### 사전 준비

- **SQLite3 설치**
- vs code 확장 프로그램 **SQLite 설치**
- 데이터베이스 mydb.sqlite3 파일 생성
- DDL.sql 파일 생성
- vs xcode 실행 후 DDL.sql 화면에서 마우스 우클릭, Use Database 선택

<br>

#### CREATE TABLE

- DDL.sql 파일에 statement 작성

```
CREATE TABLE contacts {
  name TEXT NOT NULL,
  age INTEGER NOT NULL,
  email TEXT NOT NULL UNIQUE
};
```

- Query 실행하기
  - 실행하고자 하는 명령문에 커서를 두고 마우스 우측 버튼
  - Run Selected Query 선택
- Data Types 종류
  1. NULL
  2. INTEGER
  3. REAL
  4. TEXT
  5. BLOB
- Constraints
  1. NOT NULL
  2. UNIQUE
  3. PRIMART KEY
  4. AUTOINCREMENT
  5. 그 외

<br>

#### ALTER TABLE

1. RENAME a table

   ```
   ALTER TABLE table_name RENAME TO new_table_name;
   ```

2. RENAME a column

   ```
   ALTER TABLE table_name RENAME CoLUMN column_name TO new_column_name;
   ```

3. ADD a new column to a table

   - 기존에 데이터가 있는 경우 DEFAULT 제약 조건을 사용해야 할 수도 있음!

   ```
   ALTER TABLE table_name ADD COLUMN column_definition;
   ```

4. DELETE a column

   - 컬럼이 다른 부분에서 참조되는 경우 (FOREIGN KEY) 삭제 못함
   - PRIMARY KEY인 경우 삭제 못함
   - UNIQUE 제약 조건이 있는 경우 삭제 못함

   ```
   ALTER TABLE table_name DROP COLUMN column_name;
   ```

<br>

#### DROP TABLE

- 데이터베이스에서 테이블을 제거

  - 실행 취소하거나 복구할 수 없음
  - 한 번에 하나의 테이블만 삭제가능

  ```
  DROP TABLE table_name;
  ```

  

<br>

## DML

#### sqlite3 사용하기

- 시작하기 : 터미널에 sqlite3 입력
- 데이터베이스 파일 열기 : .open mydb.sqlite3 입력
- 종료하기 : .exit

#### Filtering data

- SELECT

  - DISTINCT : 중복 제거
  - ORDER BY : 정렬
    - ASC
    - DESC
  - WHERE : 조건
    - LIMIT, OFFSET
    - LIKE
      - % : 0개 이상의 문자가 올 수 있음을 의미
      - _ : 단일(1개) 문자가 있음을 의미
    - IN (NOT IN)
    - BETWEEN A AND B : A이상 B 이하

  - GROUP BY

    - Aggregate Function

      - AVG
      - MAX
      - MIN
      - SUM
      - COUNT

      ``` 
      SELECT country, COUNT(*) FROM users GROUP BY country;
      ```



#### Changing data

- INSERT : 새 행을 삽입

  ```
  INSERT INTO table_name (column1, column2, ...)
  VALUES (value1, value2, ...);
  ```

- UPDATE : 수정

  ```
  UPDATE table_name
  SET column_1 = new_value_1,
      column_2 = new_value_2,
  WHERE search_condition;
  ```
  
- DELETE : 테이블에서 행 제거

  ```
  DELETE FROM table_name
  WHERE search_condition;
  ```

  































