import cv2
import torch
import requests
from sort import Sort  # 用于变更检测的 SORT 算法

# 加载 YOLOv5 模型
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')  # 使用预训练模型

# 初始化 SORT 跟踪器
tracker = Sort()

# 初始化摄像头
cap = cv2.VideoCapture(0)  # 0 代表默认摄像头

# 检测结果上传函数
def upload_results(detections):
    api_url = "http://your-django-url.com/api/detection"  # 替换为实际的 Django API 地址
    data = {"detection_results": []}
    for det in detections:
        x1, y1, x2, y2, obj_id = map(int, det)
        data["detection_results"].append({
            "id": obj_id,
            "bbox": [x1, y1, x2, y2]
        })
    response = requests.post(api_url, json=data)
    print(f"Upload status: {response.status_code}")

# 主检测循环
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("摄像头读取失败")
        break

    # YOLOv5 检测
    results = model(frame)
    detections = results.xyxy[0].numpy()[:, :4]  # 提取 (xmin, ymin, xmax, ymax)

    # SORT 跟踪
    tracked_objects = tracker.update(detections)

    # 绘制检测框和 ID
    for obj in tracked_objects:
        x1, y1, x2, y2, obj_id = map(int, obj)
        label = f"ID {obj_id}"
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # 上传检测结果
    upload_results(tracked_objects)

    # 显示结果
    cv2.imshow('YOLOv5 + SORT Detection', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
