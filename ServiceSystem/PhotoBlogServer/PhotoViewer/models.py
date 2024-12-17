from django.db import models
from django.contrib.auth.models import User

class Detection(models.Model):
    """
    用于存储检测结果的模型
    """
    image = models.ImageField(upload_to='images/detections/')  # 存储上传的检测图像
    results = models.JSONField()  # 存储检测结果（JSON 格式）
    detected_at = models.DateTimeField(auto_now_add=True)  # 检测时间

    def __str__(self):
        return f"Detection {self.id} at {self.detected_at}"


class ImageBlog(models.Model):
    """
    图像博客模型，存储上传的图像及其信息
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # 关联用户
    title = models.CharField(max_length=100)  # 图像标题
    image = models.ImageField(upload_to='images/blogs/')  # 图像文件，保存在 media/images/blogs/ 目录
    description = models.TextField(blank=True)  # 图像描述，允许为空
    created_at = models.DateTimeField(auto_now_add=True)  # 上传时间

    def __str__(self):
        return self.title
