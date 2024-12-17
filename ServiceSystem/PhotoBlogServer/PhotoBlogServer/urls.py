from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from PhotoViewer.views import (
    JWTLoginView, 
    ImageBlogCreateView, ImageBlogListView
)

urlpatterns = [
    # 管理后台
    path('admin/', admin.site.urls),

    # JWT 登录 API
    path('api/auth/login/', JWTLoginView.as_view(), name='jwt-login'),

    # 检测数据 API：上传和获取
    path('api/detection/', include('PhotoViewer.urls')),  

    # 图像博客 API：上传和获取
    path('api/images/upload/', ImageBlogCreateView.as_view(), name='image-upload'),
    path('api/images/list/', ImageBlogListView.as_view(), name='image-list'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)