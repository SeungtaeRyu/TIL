# :purple_heart: 03_PJT

## 01_nav_footer.html

- #### Navigation Bar
  
  1. Bootstrap Navbar Component를 참고합니다.
     :key: `bootstrap의 navbar 사용`
  
  2. 스크롤을 하더라도 항상 화면 상단에 고정되어 있습니다.
     :key: `fixed-top 클래스 적용`
  
  3. 로고 이미지는 제공된 logo.png를 사용합니다.
     :key: `<img src="./images/logo.png" alt="#" style="width: 100px" /> 삽입`
  
  4. 로고 이미지는 하이퍼링크 역할도 가능하며 클릭 시 02_home.html로 이동해야 합니다.
     :key: `3번 답을 <a></a> 태그로 감싸기`
  
  5. 내비게이션 메뉴 중 Home, Community는 하이퍼링크 역할도 가능하며 클릭 시 각각02_home.html, 03_community.html로 이동해야 합니다.
     :key: `<a class="nav-link" aria-current="page" href="/02_home.html">Home</a>`
     :key: `<a class="nav-link" href="/03_community.html">Community</a>`
  
  6. 내비게이션 메뉴 중 Login은 클릭 시 Bootstrap Modal Component가 나타납니다.
     • Modal Component 내부에는 HTML form 요소를 배치합니다.
     :key: `bootstrap의 modal 사용`
     :warning: `modal의 target부분은 중첩해서 사용하면 안됨!! body레벨에서 사용 권장!!`
  
  7. Viewport의 가로 크기 별 반응형 디자인은 스크린 샷 예시를 참고하여 일치하도록 합니다

- #### Footer
  
  1. 스크롤을 하더라도 항상 화면 하단에 고정되어 있습니다.
     :key: `footer에 fixed-bottom 적용`
  2. Footer에 작성된 내용은 수직·수평 가운데 정렬되어 있습니다.
     :key: `footer에 d-flex 적용후 justify-content-center, align-items-center적용`

## 02_home.html

- #### Header
  
  1. Bootstrap Carousel Component로 구성합니다.
     :key: `bootstrap의 casousel component 사용`
  2. 이미지는 최소 3장 이상 사용하며 자동으로 전환됩니다.
     :key: `header1,2,3 image 적용`

- #### Section
  
  1. Section 내부의 개별 요소(article)들은 Bootstrap Card Component로 구성합니다.
     • 이미지, 제목, 설명을 포함합니다.
     • 이미지는 제공된 영화 포스터 이미지를 사용합니다.
     :key: `bootstrap의 card component를 사용`
  
  2. 개별 요소들은 좌우 일정한 간격을 가집니다. (간격은 자유롭게 설정 가능)
     :key: `css 파일로 margin을 준다!`
     
     ```css
     .section-style {
     margin-left: 10%;
     margin-right: 10%;
     }
     ```
  
  3. Viewport의 가로 크기가 576px 미만일 경우 한 행에 1개씩 표시됩니다.
  
  4. Viewport의 가로 크기가 576px 이상일 경우 한 행에 2개 이상 표시됩니다.
     (자유롭게 설정 가능)
     :key: `576미만 1개, 576이상 3개로 설정!`
     
     ```html
     <div class="row row-cols-1 row-cols-sm-3 g-4">
     <!-- 기본값으로 한줄에 1개씩 보이도록 설정한 후 
     sm 사이즈 이상일 때 한줄에 3개씩 보이도록 설정. 
     gap을 설정하여 여백을 준 -->
     ```
  
  5. Viewport의 가로 크기 별 반응형 디자인은 스크린 샷 예시를 참고하여 일치하도록
     합니다.

## 03_community.html

- #### Aside (게시판 목록)
  
  1. HTML aside 요소로 이루어져 있습니다.
  2. Bootstrap List group Component로 구성합니다.
     :key: `bootstrap의 list group을 사용`
  3. 내부의 각 항목은 클릭이 가능한 하이퍼링크이지만, URL은 별도로 없습니다.
     :key: `<a> 태그로 작성`
  4. Viewport의 가로 크기가 992px 미만일 경우HTML main 요소 영역 전체만큼의 너비를 가집니다.
     :key: `grid container를 사용하여 default 값으로 col-12를 적용`
  5. Viewport의 가로 크기가 992px 이상일 경우HTML main 요소 영역 기준으로 좌측 1/6 만큼의 너비를 가집니다.
     :key: `992px 이상의 크기에서 1/6을 적용해주는 col-lg-2를 적용`
  6. Viewport의 가로 크기 별 반응형 디자인은 스크린 샷 예시를 참고하여 일치하도록 합니다.

- #### Section (게시판)
  
  1. 게시판은 HTML section 요소로 이루어져 있습니다.
  
  2. 게시판은 Viewport의 가로 크기에 따라 전혀 다른 요소를 표시합니다.
      • Viewport의 가로 크기가 992px 미만일 경우 게시판은 HTML article 요소의 집합으로 표시되며, HTML main 요소 영역 전체만큼의 너비를 가집니다.
      • Viewport의 가로 크기가 992px 이상일 경우게시판은 Bootstrap Tables Content로 구성되며, HTML main 요소 영역 기준으로 우측 5/6 만큼의 너비를 가집니다.
      :key: `풀이`
     
     ```html
     <!--
     992px 이상의 크기에서 aside가 할당하는 1/6을 제외한 5/6을 section에 할당해준다 
     -->
     <section class="col-lg-10">
     
     <!--
     section에는 table과 article 을 각각 만들어
     992px 이상의 크기에서는 table을, 미만의 크기에서는 article을 보여주게 설정했다.
      -->
     <div class="d-none d-lg-block"> <!-- 테이블의 div -->
     <div class="d-lg-none"> <!-- 아티클의 div -->
     ```

- #### Pagination
  
  1. Bootstrap Pagination Component로 구성합니다.
  2. 게시판 하단에 위치하며 너비는 자유롭게 설정합니다.
     :key: `bootstrap의 pagination component을 사용`
  3. 자신의 영역 안에서 수평 중앙 정렬되어 있습니다.
     :key: `<ul class="pagination d-flex justify-content-center">를 적용`
  4. 내부의 각 항목은 클릭이 가능한 하이퍼링크이지만, URL은 별도로 없습니다
     :key: `li 내부를 <a> 태그로 작성`

## 전체 코드

- #### :yellow_heart: nav_footer.html
  
  ```html
  <!-- navbar 영역 -->
  <nav class="navbar navbar-expand-md bg-dark navbar-dark fixed-top">
  <div class="container-fluid">
    <!-- 로고 이미지 -->
    <a href="/02_home.html">
      <img src="./images/logo.png" alt="#" style="width: 100px" />
    </a>
    <!-- 토글 버튼 -->
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav"
      aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <!-- navbar item -->
    <div class="collapse navbar-collapse" id="navbarNav">
      <ul class="navbar-nav">
        <!-- home.html 으로 이동 -->
        <li class="nav-item">
          <a class="nav-link active" aria-current="page" href="/02_home.html">Home</a>
        </li>
        <!-- community.html 으로 이동 -->
        <li class="nav-item">
          <a class="nav-link" href="/03_community.html">Community</a>
        </li>
        <!-- Login Modal -->
        <li class="nav-item">
          <a class="nav-link" href="#" data-bs-toggle="modal" data-bs-target="#exampleModal"
            data-bs-whatever="@getbootstrap">Login</a>
        </li>
      </ul>
    </div>
  </div>
  </nav>
  
  <!-- Login Modal 코드 -->
  <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
  <div class="modal-dialog">
    <form>
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="exampleModalLabel">Modal title</h5>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
          <div class="mb-3">
            <label for="email" class="col-form-label">Email Address</label>
            <input type="text" class="form-control" id="email" />
            <p>We'll never share your email with anyone else.</p>
          </div>
          <div class="mb-3">
            <label for="password" class="col-form-label">Password</label>
            <input type="text" class="form-control" id="password" />
          </div>
          <div class="form-check">
            <input class="form-check-input" type="checkbox" value="" id="flexCheckDefault" />
            <label class="form-check-label" for="flexCheckDefault">
              Check me out
            </label>
          </div>
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-secondary text-white" data-bs-dismiss="modal">
            Close
          </button>
          <button type="button" class="btn btn-primary text-white">
            Submit
          </button>
        </div>
      </div>
    </form>
  </div>
  </div>
  
  <!-- Footer 영역 -->
  <footer class="d-flex justify-content-center align-items-center fixed-bottom bg-white">
  <span>Web-bootstrap PJT, by 류승태</span>
  </footer>
  ```

- #### :blue_heart: home.html
  
  ```html
  <header class="header-style">
  <!-- 회전목마 이미지 -->
  <div id="carouselExampleControls" class="carousel slide" data-bs-ride="carousel">
    <div class="carousel-inner">
      <div class="carousel-item active">
        <img src="./images/header1.jpg" class="d-block w-100" alt="..." />
      </div>
      <div class="carousel-item">
        <img src="./images/header2.jpg" class="d-block w-100" alt="..." />
      </div>
      <div class="carousel-item">
        <img src="./images/header3.jpg" class="d-block w-100" alt="..." />
      </div>
    </div>
    <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleControls"
      data-bs-slide="prev">
      <span class="carousel-control-prev-icon" aria-hidden="true"></span>
      <span class="visually-hidden">Previous</span>
    </button>
    <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleControls"
      data-bs-slide="next">
      <span class="carousel-control-next-icon" aria-hidden="true"></span>
      <span class="visually-hidden">Next</span>
    </button>
  </div>
  </header>
  
  <!-- 그리드 컨테이너 -->
  <section class="d-flex flex-column justify-content-center align-items-center section-style">
  <h1 style="margin: 30px">Boxoffice</h1>
  <div class="row row-cols-1 row-cols-sm-3 g-4">
    <div class="col">
      <div class="card">
        <img src="./images/movie1.jpg" class="card-img-top" alt="..." />
        <div class="card-body">
          <h5 class="card-title">Card title</h5>
          <p class="card-text">
            This is a longer card with supporting text below as a natural
            lead-in to additional content. This content is a little bit
            longer.
          </p>
        </div>
      </div>
    </div>
    <div class="col">
      <div class="card">
        <img src="./images/movie2.jpg" class="card-img-top" alt="..." />
        <div class="card-body">
          <h5 class="card-title">Card title</h5>
          <p class="card-text">
            This is a longer card with supporting text below as a natural
            lead-in to additional content. This content is a little bit
            longer.
          </p>
        </div>
      </div>
    </div>
    <div class="col">
      <div class="card">
        <img src="./images/movie3.jpg" class="card-img-top" alt="..." />
        <div class="card-body">
          <h5 class="card-title">Card title</h5>
          <p class="card-text">
            This is a longer card with supporting text below as a natural
            lead-in to additional content.
          </p>
        </div>
      </div>
    </div>
    <div class="col">
      <div class="card">
        <img src="./images/movie4.jpg" class="card-img-top" alt="..." />
        <div class="card-body">
          <h5 class="card-title">Card title</h5>
          <p class="card-text">
            This is a longer card with supporting text below as a natural
            lead-in to additional content. This content is a little bit
            longer.
          </p>
        </div>
      </div>
    </div>
    <div class="col">
      <div class="card">
        <img src="./images/movie5.jpg" class="card-img-top" alt="..." />
        <div class="card-body">
          <h5 class="card-title">Card title</h5>
          <p class="card-text">
            This is a longer card with supporting text below as a natural
            lead-in to additional content. This content is a little bit
            longer.
          </p>
        </div>
      </div>
    </div>
    <div class="col">
      <div class="card">
        <img src="./images/movie6.jpg" class="card-img-top" alt="..." />
        <div class="card-body">
          <h5 class="card-title">Card title</h5>
          <p class="card-text">
            This is a longer card with supporting text below as a natural
            lead-in to additional content. This content is a little bit
            longer.
          </p>
        </div>
      </div>
    </div>
  </div>
  </section>
  ```

- #### :green_heart: community.html
  
  ```html
  <main class="main-style">
  <div class="container">
    <h1>Community</h1>
    <div class="row">
      <!-- Aside - 게시판 목록 -->
      <aside class="col-12 col-lg-2">
        <div class="list-group">
          <a href="#" class="list-group-item list-group-item-action text-primary" aria-current="true">
            Boxoffice</a>
          <a href="#" class="list-group-item list-group-item-action text-primary">Movies</a>
          <a href="#" class="list-group-item list-group-item-action text-primary">Genres</a>
          <a href="#" class="list-group-item list-group-item-action text-primary">Actors</a>
        </div>
      </aside>
  
      <!-- Section - 게시판 -->
      <section class="col-lg-10">
        <div class="d-none d-lg-block">
          <table class="table table-striped">
            <thead class="table-dark text-white">
              <tr>
                <th scope="col">영 화제목</th>
                <th scope="col">글 제목</th>
                <th scope="col">작성자</th>
                <th scope="col">작성 시간</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <th scope="row">Great Movie title</th>
                <td>Best Movie Ever</td>
                <td>user</td>
                <td>1 minute ago</td>
              </tr>
              <tr>
                <th scope="row">Great Movie title</th>
                <td>Movie Test</td>
                <td>user</td>
                <td>1 minute ago</td>
              </tr>
              <tr>
                <th scope="row">Great Movie title</th>
                <td>Movie Test</td>
                <td>user</td>
                <td>1 minute ago</td>
              </tr>
              <tr>
                <th scope="row">Great Movie title</th>
                <td>Movie Test</td>
                <td>user</td>
                <td>1 minute ago</td>
              </tr>
            </tbody>
          </table>
        </div>
  
        <!-- article 영역 -->
        <div class="d-lg-none">
          <hr />
          <article>
            <h1>Best Movie Ever</h1>
            <h2>Great Movie Title</h2>
            <p>user</p>
            <p>1 minute ago</p>
          </article>
          <hr />
          <article>
            <h1>Movie Test</h1>
            <h2>Great Movie Title</h2>
            <p>user</p>
            <p>1 minute ago</p>
          </article>
          <hr />
          <article>
            <h1>Movie Test</h1>
            <h2>Great Movie Title</h2>
            <p>user</p>
            <p>1 minute ago</p>
          </article>
          <hr />
          <article>
            <h1>Movie Test</h1>
            <h2>Great Movie Title</h2>
            <p>user</p>
            <p>1 minute ago</p>
          </article>
        </div>
      </section>
    </div>
  </div>
  
  <nav aria-label="Page navigation example">
    <ul class="pagination d-flex justify-content-center">
      <li class="page-item"><a class="page-link" href="#">Previous</a></li>
      <li class="page-item"><a class="page-link" href="#">1</a></li>
      <li class="page-item"><a class="page-link" href="#">2</a></li>
      <li class="page-item"><a class="page-link" href="#">3</a></li>
      <li class="page-item"><a class="page-link" href="#">Next</a></li>
    </ul>
  </nav>
  </main>
  ```