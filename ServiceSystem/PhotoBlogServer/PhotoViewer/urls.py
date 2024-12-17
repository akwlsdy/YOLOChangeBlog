from django.urls import path
from .views import (
    JWTLoginView, 
    DetectionUploadView, DetectionListView,
    ImageBlogCreateView, ImageBlogListView
)

urlpatterns = [
    # JWT 登录 API
    path('login/', JWTLoginView.as_view(), name='jwt-login'),  

    # 检测数据 API
    path('upload/', DetectionUploadView.as_view(), name='detection-upload'),  
    path('list/', DetectionListView.as_view(), name='detection-list'),        

    # 图像博客 API
    path('images/upload/', ImageBlogCreateView.as_view(), name='image-upload'),  
    path('images/list/', ImageBlogListView.as_view(), name='image-list'),        
]
