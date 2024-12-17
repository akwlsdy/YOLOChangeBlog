from rest_framework import serializers
from .models import ImageBlog

class ImageBlogSerializer(serializers.ModelSerializer):
    """
    序列化器：将 ImageBlog 模型数据转换为 JSON 格式
    """
    class Meta:
        model = ImageBlog
        fields = ['id', 'user', 'title', 'image', 'description', 'created_at']
