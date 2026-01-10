# My Website - Django 회원 관리 시스템

Django와 MySQL을 사용한 회원가입, 로그인, 게시판, 의약정보 조회 웹 애플리케이션

## 주요 기능

- ✅ **회원가입**: 사용자명, 이메일, 비밀번호로 회원가입
- ✅ **로그인/로그아웃**: 안전한 인증 시스템
- ✅ **게시판**: 게시글 목록 페이지 (추후 확장 가능)
- ✅ **의약정보 조회**: 의약품 정보 검색 페이지 (추후 확장 가능)
- ✅ **About Us**: 서비스 소개 페이지
- ✅ **반응형 디자인**: Bootstrap 5 기반

## 기술 스택

- **Backend**: Django 4.2
- **Database**: MySQL (개발 환경에서는 SQLite 사용 가능)
- **Frontend**: HTML5, CSS3, Bootstrap 5
- **Authentication**: Django Auth System

## 설치 및 실행

### 1. 저장소 클론

```bash
git clone <repository-url>
cd my-website
```

### 2. 가상환경 생성 및 활성화

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3. 패키지 설치

```bash
pip install -r requirements.txt
```

### 4. 데이터베이스 설정

**SQLite 사용 (개발용, 기본 설정)**
- 별도 설정 불필요

**MySQL 사용 (프로덕션)**
1. MySQL 설치 및 데이터베이스 생성:
```sql
CREATE DATABASE mywebsite_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

2. `mysite/settings.py`에서 DATABASES 설정 수정:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mywebsite_db',
        'USER': 'your_username',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

### 5. 마이그레이션 실행

```bash
python manage.py migrate
```

### 6. 개발 서버 실행

```bash
python manage.py runserver
```

브라우저에서 http://127.0.0.1:8000/ 접속

## 프로젝트 구조

```
my-website/
├── manage.py
├── requirements.txt
├── README.md
├── mysite/                 # 메인 프로젝트 설정
│   ├── settings.py        # 설정 파일
│   ├── urls.py            # URL 라우팅
│   └── wsgi.py
├── accounts/               # 인증 앱
│   ├── forms.py           # 회원가입 폼
│   ├── views.py           # 로그인/회원가입/로그아웃 뷰
│   └── urls.py
├── board/                  # 게시판 앱
│   ├── views.py
│   └── urls.py
├── medicine/               # 의약정보 앱
│   ├── views.py
│   └── urls.py
└── templates/              # 템플릿 파일
    ├── base.html          # 기본 템플릿
    ├── index.html         # 홈페이지
    ├── about.html         # About Us
    ├── accounts/
    │   ├── login.html
    │   └── signup.html
    ├── board/
    │   └── board_list.html
    └── medicine/
        └── medicine_info.html
```

## 사용 방법

### 회원가입
1. 상단 네비게이션에서 "회원가입" 클릭
2. 사용자명, 이메일, 비밀번호 입력
3. 회원가입 버튼 클릭
4. 자동으로 로그인되어 홈페이지로 이동

### 로그인
1. 상단 네비게이션에서 "로그인" 클릭
2. 사용자명과 비밀번호 입력
3. 로그인 버튼 클릭

### 로그아웃
- 로그인 후 상단 네비게이션에서 "로그아웃" 클릭

## 개발 참고사항

### 관리자 계정 생성

```bash
python manage.py createsuperuser
```

관리자 페이지: http://127.0.0.1:8000/admin/

### 추가 개발 가능 기능

- 게시판: 게시글 작성, 수정, 삭제, 댓글 기능
- 의약정보: 데이터베이스 연동 및 검색 기능
- 회원 프로필 페이지
- 비밀번호 재설정 기능

## 라이선스

이 프로젝트는 MIT 라이선스 하에 있습니다.
