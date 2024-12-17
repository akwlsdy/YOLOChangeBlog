from django.http import JsonResponse

def home(request):
    """
    根路径视图，返回欢迎信息或说明。
    """
    return JsonResponse({"message": "Welcome to PhotoBlogServer API!"})
