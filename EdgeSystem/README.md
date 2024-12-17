# EdgeSystem

## 개요
EdgeSystem은 YOLOv5를 활용하여 실시간 객체 탐지와 SORT 알고리즘을 통한 변경 사항 추적 기능을 제공합니다. 탐지된 결과는 Django 기반 서버로 RESTful API를 통해 업로드됩니다.

## 주요 기능
1. **객체 탐지**: YOLOv5를 사용하여 실시간으로 카메라에서 객체를 탐지합니다.
2. **변경 사항 추적**: SORT 알고리즘으로 객체 상태(추가/삭제)를 추적합니다.
3. **결과 업로드**: 탐지 결과와 이미지를 Django 서버로 전송합니다.

## 주요 기술
- **YOLOv5**: 사전 학습된 객체 탐지 모델.
- **SORT**: 간단한 온라인 실시간 추적 알고리즘(Simple Online Realtime Tracking).
- **OpenCV**: 카메라 입력 및 이미지 처리를 위한 라이브러리.
- **Python REST API**: 결과를 서버로 업로드하기 위한 HTTP 요청.

## 실행 방법
1. 필수 패키지 설치:
```bash
pip install -r requirements.txt
