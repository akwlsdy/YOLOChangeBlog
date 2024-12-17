# ServiceSystem

## 개요
ServiceSystem은 Django 기반의 서버로, EdgeSystem에서 전송된 탐지 데이터를 저장하고 RESTful API를 통해 클라이언트가 데이터를 조회할 수 있도록 지원합니다.

## 주요 기능
1. **데이터 저장**:
   - 업로드된 탐지 이미지와 결과 데이터를 데이터베이스에 저장.
2. **RESTful API 제공**:
   - **탐지 데이터 업로드**: `/api/detection/upload/` (POST 요청).
   - **탐지 데이터 조회**: `/api/detection/list/` (GET 요청).

## 주요 기술
- **Django**: 웹 서버 및 API 구현.
- **Django REST Framework**: RESTful API 구현을 위한 프레임워크.
- **SQLite**: Django에서 기본적으로 제공되는 데이터베이스.

## 실행 방법
1. Django 서버 실행:
```bash
cd PhotoBlogServer
python manage.py runserver
