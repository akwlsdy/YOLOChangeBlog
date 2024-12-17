from rest_framework import viewsets, filters
from servicesystem.models import Image
from .serializers import ImageSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend

class ImageViewSet(viewsets.ModelViewSet):
    """
    ViewSet for handling Image model CRUD operations.
    """
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['title']  # 允许按 'title' 字段搜索


class JWTLoginView(APIView):
    """
    用户登录视图：验证用户名和密码，返回 JWT Token。
    """
    def post(self, request):
        # 获取请求中的用户名和密码
        username = request.data.get("username")
        password = request.data.get("password")

        # 打印调试信息，确保收到请求中的数据
        print(f"Username: {username}, Password: {password}")

        # 用户验证
        user = authenticate(username=username, password=password)

        # 打印调试信息，检查 authenticate() 是否找到用户
        print(f"Authenticated User: {user}")
        
        if user:
            # 生成 JWT Token
            refresh = RefreshToken.for_user(user)
            return Response({
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            }, status=status.HTTP_200_OK)

        # 认证失败返回错误
        return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
