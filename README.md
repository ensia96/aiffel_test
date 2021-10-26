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
    apt-get install direnv && apt-get install direnv && apt-get install python3
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

- 앱 실행

```
make run
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
code = 200
body = {"message": "post creation success"}
```

- Error Response

```
> case 1

code = 400
body = {"message": "this method is not allowed."}

> case 2

code = 400
body = {"message": "token is not valid"}

> case 3

code = 200
body = {"message": "'title' is not provided."}

> case 4

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
      "likes": <좋아요 수>
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

<details><summary>get_post</summary>

```
질문(게시글) 확인 요청을 받아, 처리하는 엔드포인트입니다.
```

- URL(endpoint)

```
/service/post/:id
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
echo "$(curl -XGET "http://localhost:8000/service/post/1/")"
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
body = {'message': 'post does not exists.'}
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
body = {"message": "post update success"}
```

- Error Response

```
> case 1

code = 400
body = {"message": "this method is not allowed."}

> case 2

code = 400
body = {"message": "token is not valid"}

> case 3

code = 400
body = {"message": "'id' is not provided."}

> case 4

code = 400
body = {"message": "'title' is not provided."}

> case 5

code = 400
body = {"message": "'content' is not provided."}

> case 6

code = 403
body = {"message": "this user can not update this post."}
```

</details>
