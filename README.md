# YOLOChangeBlog

## 프로젝트 개요
YOLOChangeBlog는 YOLOv5 기반 객체 탐지, 변경 탐지(Change Detection), Django 서버 및 Android 클라이언트를 통합한 시스템입니다. 시스템은 세 가지 주요 모듈로 구성됩니다:
1. **EdgeSystem**: YOLOv5를 사용한 실시간 객체 탐지 및 변경 추적.
2. **ServiceSystem**: Django로 구현된 서버로, 탐지 데이터를 저장하고 RESTful API를 제공합니다.
3. **AndroidClient**: Android 애플리케이션으로, 탐지된 이미지와 변경 기록을 표시합니다.

---

## 시스템 모듈

### 1. EdgeSystem
- **기능**: 카메라를 통해 실시간 객체 탐지를 수행하고, SORT 알고리즘으로 변경 사항을 추적하며, 결과를 서버로 업로드합니다.
- **주요 기술**:
  - YOLOv5
  - SORT 알고리즘
  - OpenCV 및 Python REST API
- **위치**: `C:\Users\HHHH\YOLOChangeBlog\EdgeSystem`

### 2. ServiceSystem
- **기능**: 탐지된 이미지 및 데이터를 저장하고, RESTful API를 통해 클라이언트가 데이터를 조회할 수 있도록 합니다.
- **주요 기술**:
  - Django
  - SQLite 데이터베이스
  - Django REST Framework
- **위치**: `C:\Users\HHHH\YOLOChangeBlog\ServiceSystem`

### 3. AndroidClient
- **기능**: 탐지된 이미지와 변경 사항을 Android 애플리케이션에서 표시하고, RESTful API를 통해 서버와 통신합니다.
- **주요 기술**:
  - Java
  - Android Studio
- **위치**: `C:\Users\HHHH\YOLOChangeBlog\AndroidClient`

---

## 실행 방법

### 1. EdgeSystem 실행
```bash
cd C:\Users\HHHH\YOLOChangeBlog\EdgeSystem
python edge_system.py
