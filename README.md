# AIFFEL 백엔드 개발 사전 과제

## 1. 기본 설정

**해당 프로젝트를 실행하려면, 'direnv', 'make', 'python', 'pip' 가 필요합니다.**

## 1-1. direnv, make, python 설치

- macOS
    ```
    brew install direnv && brew install make && brew install python
    ```

- Ubuntu
    ```
    apt-get install direnv && apt-get install make && apt-get install python3
    ```

- Windows
    1. 'https://github.com/direnv/direnv/releases' 로 이동
    2. 운영 체제 bit에 따라 'direnv.windows' 로 시작하는 exe 파일 설치
    3. 'http://gnuwin32.sourceforge.net/packages/make.htm' 로 이동
    4. 'Complete package, except sources' 옆에 있는 'Setup' 을 클릭하여 설치
    5. 'https://www.python.org/downloads/' 로 이동
    6. 'Download Python 3.x.x' 를 클릭하여 설치

## 1-2. pip 설치

```
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py && python3 get-pip.py
```

# 2. Django 앱 실행

**우선, 해당 저장소에서 내려받은 소스 코드가 있는 경로로 이동해야 합니다.**

- 정상적인 앱 실행을 위한 의존성 패키지 설치 및 환경 변수 설정

```
make install && make env
```

- SQLite 동기화  
  `(아래의 '로컬 데이터베이스 진입' 명령어로 SQLite 에 접속한 후 아래 명령어 실행)`

```
.read dump.txt
```

- 앱 실행

```
make run
```

- Django Shell 진입

```
make shell
```

- 로컬 데이터베이스 진입

```
make db
```

# 3. API 안내

<details><summary>create_post</summary>

```
질문(게시글) 생성 요청을 받아, 처리하는 엔드포인트입니다.
```

- URL(endpoint)

```
/service/post/create/
```

- Method

```
POST
```

- URL Params

```
None
```

- Request Header

```
Authorization: <token from signin response>
```

- Sample Call

```
curl  -XGET "http://localhost:8000/service/post/create/" \
      -X "POST" \
      -H "Authorization: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxfQ.7LCrddETrRL6H7JcXYigQORpm5559EJOmPknKwrILF4" \
      -d "{ \
          \"title\" : \"curl 요청으로 생성된 게시글입니다.\", \
          \"content\" : \"curl 요청으로 생성된 게시글의 본문 내용입니다.\" \
      }"
```

- Success Response

```
code = 201
body = {"message": "successfully created post."}
```

- Error Response

```
> case 1

code = 400
body = {"message": "this method is not allowed."}

> case 2

code = 401
body = {"message": "token is not valid."}

> case 3

code = 400
body = {"message": "there is problem with the request body."}

> case 4

code = 400
body = {"message": "'title' is not provided."}

> case 5

code = 400
body = {"message": "'content' is not provided."}
```

</details>

<details><summary>get_post_list</summary>

```
질문(게시글) 목록 확인 요청을 받아, 처리하는 엔드포인트입니다.
```

- URL(endpoint)

```
/service/posts/
```

- Method

```
GET
```

- URL Params

```
None
```

- Request Header

```
None
```

- Sample Call

```
echo "$(curl -XGET "http://localhost:8000/service/posts/")"
```

- Success Response

```
code = 200
body = {
  "posts": [
    {
      "id": <게시글 pk>,
      "title": <게시글 제목>,
      "created_at": <게시글 작성일>,
      "author_id": <작성자 pk>,
      "author_nickname": <작성자 닉네임>,
      "likes": <좋아요 수>,
      "comments": <댓글 수>
    },
    ...
  ]
}
```

- Error Response

```
> case 1

code = 400
body = {"message": "this method is not allowed."}
```

</details>

<details><summary>search_post</summary>

```
질문(게시글) 검색 요청을 받아, 처리하는 엔드포인트입니다.
```

- URL(endpoint)

```
/service/post/search/
```

- Method

```
POST
```

- URL Params

```
None
```

- Request Header

```
None
```

- Sample Call

```
echo "$(curl  -XGET "http://localhost:8000/service/post/search/" \
      -X "POST" \
      -d "{ \
          \"type\" : \"title\", \
          \"keyword\" : \"curl 요청\" \
      }"
)"
```

- Success Response

```
code = 200
body = {
  "posts": [
    {
      "id": <게시글 pk>,
      "title": <게시글 제목>,
      "created_at": <게시글 작성일>,
      "author_id": <작성자 pk>,
      "author_nickname": <작성자 닉네임>,
      "likes": <좋아요 수>,
      "comments": <댓글 수>
    },
    ...
  ]
}
```

- Error Response

```
> case 1

code = 400
body = {"message": "this method is not allowed."}

> case 2

code = 400
body = {"message": "there is problem with the request body."}

> case 3

code = 400
body = {"message": "'type' is not provided."}

> case 4

code = 400
body = {"message": "'keyword' is not provided."}

> case 5

code = 400
body = {"message": "this search type is not supported."}
```

</details>

<details><summary>get_top_post</summary>

```
이번 달(조회 시점 기준) 의 최고 인기 질문(게시글) 에 대한 요청을 받아, 처리하는 엔드포인트입니다.
```

- URL(endpoint)

```
/service/post/top/
```

- Method

```
GET
```

- URL Params

```
None
```

- Request Header

```
None
```

- Sample Call

```
echo "$(curl  -XGET "http://localhost:8000/service/post/top/")"
```

- Success Response

```
code = 200
body = {
  "post": {
    "id": <게시글 pk>,
    "title": <게시글 제목>,
    "created_at": <게시글 작성일>,
    "updated_at": <게시글 수정일>,
    "author_id": <작성자 pk>,
    "author_nickname": <작성자 닉네임>,
    "likes": <좋아요 수>,
    "comments": <댓글 수>,
    "month": <집계 기준 달>
  }
}
```

- Error Response

```
> case 1

code = 400
body = {"message": "this method is not allowed."}
```

</details>


<details><summary>get_post</summary>

```
질문(게시글) 확인 요청을 받아, 처리하는 엔드포인트입니다.
```

- URL(endpoint)

```
/service/post/:post_id
```

- Method

```
GET
```

- URL Params

```
> required

post_id=[integer]
```

- Request Header

```
None
```

- Sample Call

```
echo "$(curl -XGET "http://localhost:8000/service/post/1")"
```

- Success Response

```
code = 200
body = {
  "post": {
    "id": <게시글 pk>,
    "title": <게시글 제목>,
    "content": <게시글 내용>,
    "created_at": <게시글 작성일>,
    "updated_at": <게시글 수정일>,
    "author_id": <작성자 pk>,
    "author_nickname": <작성자 닉네임>,
    "likes": <좋아요 수>
  }
}
```

- Error Response

```
> case 1

code = 400
body = {"message": "this method is not allowed."}

> case 2

code = 404
body = {"message": "post does not exist."}
```

</details>

<details><summary>update_post</summary>

```
질문(게시글) 수정 요청을 받아, 처리하는 엔드포인트입니다.
```

- URL(endpoint)

```
/service/post/update/
```

- Method

```
POST
```

- URL Params

```
None
```

- Request Header

```
Authorization: <token from signin response>
```

- Sample Call

```
curl  -XGET "http://localhost:8000/service/post/update/" \
      -X "POST" \
      -H "Authorization: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxfQ.7LCrddETrRL6H7JcXYigQORpm5559EJOmPknKwrILF4" \
      -d "{ \
          \"id\" : 7, \
          \"title\" : \"curl 요청으로 수정된 게시글입니다.\", \
          \"content\" : \"curl 요청으로 수정된 게시글의 본문 내용입니다.\" \
      }"
```

- Success Response

```
code = 200
body = {"message": "successfully updated post."}
```

- Error Response

```
> case 1

code = 400
body = {"message": "this method is not allowed."}

> case 2

code = 401
body = {"message": "token is not valid."}

> case 3

code = 400
body = {"message": "there is problem with the request body."}

> case 4

code = 400
body = {"message": "'id' is not provided."}

> case 5

code = 400
body = {"message": "'title' is not provided."}

> case 6

code = 400
body = {"message": "'content' is not provided."}

> case 7

code = 403
body = {"message": "this user can not update this post."}
```

</details>

<details><summary>like_post</summary>

```
질문(게시글) 에 대한 좋아요 표시 요청을 받아, 처리하는 엔드포인트입니다.
```

- URL(endpoint)

```
/service/post/like/:post_id
```

- Method

```
PUT
```

- URL Params

```
> required

post_id=[integer]
```

- Request Header

```
Authorization: <token from signin response>
```

- Sample Call

```
curl  -XGET "http://localhost:8000/service/post/like/1" \
      -X "PUT" \
      -H "Authorization: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxfQ.7LCrddETrRL6H7JcXYigQORpm5559EJOmPknKwrILF4"
```

- Success Response

```
code = 200
body = {"message": "liked the post."} or {"message": "unliked the post."}
```

- Error Response

```
> case 1

code = 400
body = {"message": "this method is not allowed."}

> case 2

code = 401
body = {"message": "token is not valid."}

> case 3

code = 404
body = {"message": "post does not exist."}
```

</details>

<details><summary>delete_post</summary>

```
질문(게시글) 삭제 요청을 받아, 처리하는 엔드포인트입니다.
```

- URL(endpoint)

```
/service/post/delete/:post_id
```

- Method

```
DELETE
```

- URL Params

```
> required

post_id=[integer]
```

- Request Header

```
Authorization: <token from signin response>
```

- Sample Call

```
curl  -XGET "http://localhost:8000/service/post/delete/7" \
      -X "DELETE" \
      -H "Authorization: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxfQ.7LCrddETrRL6H7JcXYigQORpm5559EJOmPknKwrILF4"
```

- Success Response

```
code = 200
body = {"message": "successfully deleted post."}
```

- Error Response

```
> case 1

code = 400
body = {"message": "this method is not allowed."}

> case 2

code = 401
body = {"message": "token is not valid."}

> case 3

code = 400
body = {"message": "this user can not delete this post."}
```

</details>

<details><summary>add_comment</summary>

```
질문(게시글) 에 대한 댓글 생성 요청을 받아, 처리하는 엔드포인트입니다.
```

- URL(endpoint)

```
/service/comment/add/
```

- Method

```
POST
```

- URL Params

```
None
```

- Request Header

```
Authorization: <token from signin response>
```

- Sample Call

```
curl  -XGET "http://localhost:8000/service/comment/add/" \
      -X "POST" \
      -H "Authorization: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxfQ.7LCrddETrRL6H7JcXYigQORpm5559EJOmPknKwrILF4" \
      -d "{ \
          \"post_id\" : 2, \
          \"content\" : \"curl 요청으로 생성된 댓글 내용입니다.\" \
      }"
```

- Success Response

```
code = 200
body = {"message": "successfully added comment."}
```

- Error Response

```
> case 1

code = 400
body = {"message": "this method is not allowed."}

> case 2

code = 401
body = {"message": "token is not valid."}

> case 3

code = 400
body = {"message": "there is problem with the request body."}

> case 4

code = 400
body = {"message": "'post_id' is not provided."}

> case 5

code = 400
body = {"message": "'content' is not provided."}

> case 6

code = 404
body = {"message": "post does not exist."}
```

</details>

<details><summary>get_comment_list</summary>

```
질문(게시글) 에 대한 댓글 목록 확인 요청을 받아, 처리하는 엔드포인트입니다.
```

- URL(endpoint)

```
/service/comments/:post_id
```

- Method

```
GET
```

- URL Params

```
> required

post_id=[integer]
```

- Request Header

```
None
```

- Sample Call

```
echo "$(curl  -XGET "http://localhost:8000/service/comments/1")"
```

- Success Response

```
code = 200
body = {
  "comments": [
    {
      "id": <댓글 pk>,
      "content": <댓글 내용>,
      "created_at": <댓글 작성일>,
      "updated_at": <댓글 수정일>,
      "author_id": <작성자 pk>,
      "author_nickname": <작성자 닉네임>,
      "likes": <좋아요 수>,
    },
    ...
  ]
}
```

- Error Response

```
> case 1

code = 400
body = {"message": "this method is not allowed."}
```

</details>
