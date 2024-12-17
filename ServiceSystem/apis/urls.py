from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ImageViewSet, JWTLoginView  # 导入 ImageViewSet 和 JWTLoginView

# 创建默认的 Router 并注册 ViewSet
router = DefaultRouter()
router.register(r'images', ImageViewSet, basename='image')

# 路由配置
urlpatterns = [
    path("auth/login/", JWTLoginView.as_view(), name="jwt-login"),  # JWT 登录接口
    path("", include(router.urls)),  # 注册 ImageViewSet 路由
]
