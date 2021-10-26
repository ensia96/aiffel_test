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
