# My Website - Django 게시판 홈페이지

Django와 MySQL을 사용한 로그인 및 게시판 기능이 있는 웹사이트입니다.

## 📋 프로젝트 소개

이 프로젝트는 Django 4.2를 기반으로 한 게시판 시스템입니다. 사용자 인증, 게시글 CRUD(작성, 읽기, 수정, 삭제) 기능을 제공하며, 깔끔한 UI로 구성되어 있습니다.

## 🛠 기술 스택

- **Backend**: Django 4.2.26
- **Database**: MySQL
- **Language**: Python 3.x
- **Frontend**: HTML5, CSS3

## ✨ 주요 기능

### 회원 관리
- ✅ 회원가입 (사용자명, 이메일, 비밀번호)
- ✅ 로그인/로그아웃
- ✅ Django 기본 인증 시스템 사용

### 게시판
- ✅ 게시글 목록 조회 (모든 사용자)
- ✅ 게시글 상세 조회 (모든 사용자)
- ✅ 게시글 작성 (로그인한 사용자만)
- ✅ 게시글 수정 (작성자만)
- ✅ 게시글 삭제 (작성자만)
- ✅ 테이블 형식의 게시글 목록 (border 스타일링)
- ✅ 작성자 권한 관리

## 📦 설치 방법

### 1. 레포지토리 클론
```bash
git clone https://github.com/ywhcho/my-website.git
cd my-website
```

### 2. 가상환경 설정
```bash
# 가상환경 생성
python -m venv venv

# 가상환경 활성화
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
```

### 3. 패키지 설치
```bash
pip install -r requirements.txt
```

### 4. MySQL 데이터베이스 설정

#### MySQL 데이터베이스 생성
```sql
# MySQL에 로그인
mysql -u root -p

# 데이터베이스 생성
CREATE DATABASE mywebsite_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

# 사용자 생성 및 권한 부여 (선택사항)
CREATE USER 'your_mysql_user'@'localhost' IDENTIFIED BY 'your_mysql_password';
GRANT ALL PRIVILEGES ON mywebsite_db.* TO 'your_mysql_user'@'localhost';
FLUSH PRIVILEGES;
```

#### settings.py 설정
`mywebsite/settings.py` 파일에서 데이터베이스 설정을 수정하세요:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mywebsite_db',
        'USER': 'your_mysql_user',      # MySQL 사용자명
        'PASSWORD': 'your_mysql_password',  # MySQL 비밀번호
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

### 5. 데이터베이스 마이그레이션
```bash
# 마이그레이션 파일 생성
python manage.py makemigrations

# 마이그레이션 실행
python manage.py migrate
```

### 6. 관리자 계정 생성
```bash
python manage.py createsuperuser
```
사용자명, 이메일, 비밀번호를 입력하세요.

### 7. 서버 실행
```bash
python manage.py runserver
```

웹 브라우저에서 http://127.0.0.1:8000/ 로 접속하세요.

## 📱 사용법

### 홈페이지
- 메인 페이지: http://127.0.0.1:8000/
- 프로젝트 소개 및 주요 기능 안내
- 게시판 링크 제공

### 회원가입 및 로그인
1. 홈페이지에서 "회원가입" 버튼 클릭
2. 사용자명, 이메일, 비밀번호 입력
3. 회원가입 완료 후 자동 로그인
4. 이후 "로그인" 버튼으로 로그인 가능

### 게시판 사용
1. 홈페이지 또는 상단 메뉴에서 "게시판 보기" 클릭
2. 게시글 목록 확인 (테이블 형식)
3. 제목 클릭하여 게시글 상세 보기
4. 로그인 후 "글쓰기" 버튼으로 새 게시글 작성
5. 본인이 작성한 게시글은 수정/삭제 가능

### 관리자 페이지
- URL: http://127.0.0.1:8000/admin/
- 관리자 계정으로 로그인
- 사용자 및 게시글 관리

## 🌐 URL 구조

```
/                              # 홈페이지
/accounts/register/            # 회원가입
/accounts/login/               # 로그인
/accounts/logout/              # 로그아웃
/board/                        # 게시글 목록
/board/<int:pk>/               # 게시글 상세
/board/create/                 # 게시글 작성
/board/<int:pk>/update/        # 게시글 수정
/board/<int:pk>/delete/        # 게시글 삭제
/admin/                        # Django 관리자
```

## 📁 프로젝트 구조

```
my-website/
├── manage.py                  # Django 관리 스크립트
├── requirements.txt           # Python 패키지 목록
├── README.md                  # 프로젝트 문서
├── .gitignore                 # Git 제외 파일
├── mywebsite/                 # 메인 프로젝트 디렉토리
│   ├── __init__.py
│   ├── settings.py           # 프로젝트 설정 (MySQL 설정 포함)
│   ├── urls.py               # URL 라우팅
│   ├── wsgi.py
│   └── asgi.py
├── accounts/                  # 회원 관리 앱
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py              # 회원가입 폼
│   ├── models.py
│   ├── urls.py               # accounts URL
│   ├── views.py              # 회원가입, 로그인, 로그아웃 뷰
│   └── templates/
│       └── accounts/
│           ├── home.html     # 홈페이지
│           ├── login.html    # 로그인 페이지
│           └── register.html # 회원가입 페이지
└── board/                     # 게시판 앱
    ├── __init__.py
    ├── admin.py              # Post 모델 admin 등록
    ├── apps.py
    ├── forms.py              # 게시글 작성/수정 폼
    ├── models.py             # Post 모델
    ├── urls.py               # board URL
    ├── views.py              # 게시판 CRUD 뷰
    └── templates/
        └── board/
            ├── list.html     # 게시글 목록 (테이블 형식)
            ├── detail.html   # 게시글 상세
            ├── create.html   # 게시글 작성
            └── update.html   # 게시글 수정
```

## 🎨 UI 특징

- **색상 테마**: 초록색 계열 (#4CAF50)
- **게시판 목록**: 테이블 형식에 명확한 border 스타일링
- **반응형 디자인**: 다양한 화면 크기 지원
- **Hover 효과**: 버튼 및 테이블 행에 인터랙티브 효과
- **메시지 시스템**: 성공/에러 메시지 표시

## 🔒 보안 고려사항

- CSRF 토큰 사용
- 로그인 필수 기능에 `@login_required` 데코레이터 적용
- 작성자 권한 검증
- 비밀번호 검증 (Django 기본 검증 사용)

## ⚠️ 주의사항

- `settings.py`의 `SECRET_KEY`는 프로덕션 환경에서 환경변수로 관리하세요
- `DEBUG = False`로 설정하고 배포하세요
- MySQL 사용자 계정의 비밀번호는 안전하게 관리하세요
- 프로덕션 환경에서는 `ALLOWED_HOSTS`를 적절히 설정하세요

## 📝 라이센스

이 프로젝트는 교육 목적으로 만들어졌습니다.

## 👤 작성자

GitHub: [@ywhcho](https://github.com/ywhcho)

