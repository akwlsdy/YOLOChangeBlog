"""
URL configuration for servicesystem project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import home, image_gallery  # 从 servicesystem/views.py 导入 home 和 image_gallery 视图

urlpatterns = [
    path('', home, name='home'),                       # 首页视图
    path('gallery/', image_gallery, name='image_gallery'),  # 图片展示视图
    path('admin/', admin.site.urls),                   # Django 管理后台
    path('api/', include('apis.urls')),                # 包含 apis 应用的 URL
]
