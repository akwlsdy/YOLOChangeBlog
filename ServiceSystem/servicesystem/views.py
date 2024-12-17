from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    """
    渲染首页视图
    """
    return render(request, 'home.html')

def image_gallery(request):
    """
    渲染图片展示页面
    """
    return render(request, 'images.html')
